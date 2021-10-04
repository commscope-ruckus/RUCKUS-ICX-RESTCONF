import requests
import warnings
import time
import paramiko
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

class ICX_API_calls:
	def createVLAN(self, host, username, password, vlanID, vlanName):
		url = "https://" + host + "/restconf/data/network-instances/network-instance/default-vrf/vlans"
		headers = headers = {
			'Accept': 'application/yang-data+json',
			'Content-Type': 'application/json'
		}
		body = {
			"vlan": [
				{
					"vlan-id": vlanID,
					"config": {
						"vlan-id": vlanID,
						"name": vlanName
					}
				}
			]
		}
		r = requests.post(url, headers=headers, auth=(username, password), json = body, verify=False)
		return r

	def addUntaggedPortsToVLAN(self, host, username, password, vlanID, interface):
		interface = interface.replace("/", "%2F")
		url = "https://" + host + "/restconf/data/interfaces/interface/ethernet " + interface + "/ethernet"
		headers = headers = {
			'Accept': 'application/yang-data+json',
			'Content-Type': 'application/json'
		}
		body = {
			"openconfig-vlan:switched-vlan": {
				"config": {
					"access-vlan": vlanID
				}
			}
		}
		r = requests.post(url, headers=headers, auth=(username, password), json = body, verify=False)
		return r

	def addTaggedPortsToVLAN(self, host, username, password, vlanID, interface):
		interface = interface.replace("/", "%2F")
		url = "https://" + host + "/restconf/data/interfaces/interface/ethernet " + interface + "/ethernet"
		headers = headers = {
			'Accept': 'application/yang-data+json',
			'Content-Type': 'application/json'
		}
		body = {
			"openconfig-vlan:switched-vlan": {
				"config": {
					"trunk-vlans": [
						vlanID
					]
				}
			}
		}
		r = requests.post(url, headers=headers, auth=(username, password), json = body, verify=False)
		return r

	def createDynLAG(self, host, username, password, lagName, lagID):
		url = "https://" + host + "/restconf/data/interfaces"
		headers = headers = {
			'Accept': 'application/yang-data+json',
			'Content-Type': 'application/json'
		}
		body = {
			"interface": [
				{
				"name": lagName + ' ' + str(lagID),
				"config": {
					"name": lagName + ' ' + str(lagID),
					"type": "iana-if-type:ieee8023adLag",
					"enabled": True
				},
				"openconfig-if-aggregate:aggregation": {
					"config": {
						"lag-type": "LACP"
					}
				}
			}
		]
		}
		r = requests.post(url, headers=headers, auth=(username, password), json = body, verify=False)
		return r

	def addPortsToLAG(self, host, username, password, lagID, interface):
		interface = interface.replace("/", "%2F")
		url = "https://" + host + "/restconf/data/interfaces/interface/ethernet " + interface + "/ethernet/config"
		headers = headers = {
			'Accept': 'application/yang-data+json',
			'Content-Type': 'application/json'
		}
		body = {
			"openconfig-if-aggregate:aggregate-id": "lag " + str(lagID)
		}
		r = requests.post(url, headers=headers, auth=(username, password), json = body, verify=False)
		return r

	def enableRSTP(self, host, username, password, vlanID):
		url = "https://" + host + "/restconf/data/stp/rapid-pvst"
		headers = headers = {
			'Accept': 'application/yang-data+json',
			'Content-Type': 'application/json'
		}
		body = {
			"vlan": [
				{
					"vlan-id": vlanID,
					"config": {
						"vlan-id": vlanID
					}
				}
			]
		}
		r = requests.post(url, headers=headers, auth=(username, password), json = body, verify=False)
		return r

	def disableRSTP(self, host, username, password, vlanID):
		url = "https://" + host + "/restconf/data/stp/rapid-pvst/vlan/" + str(vlanID)
		headers = headers = {
			'Accept': 'application/yang-data+json',
			'Content-Type': 'application/json'
		}
		r = requests.delete(url, headers=headers, auth=(username, password), verify=False)
		return r

	def createStaticRoute(self, host, username, password, prefix, nexthop):
		url = "https://" + host + "/restconf/data/network-instances/network-instance/default-vrf/protocols"
		headers = headers = {
			'Accept': 'application/yang-data+json',
			'Content-Type': 'application/json'
		}
		body = {
			"protocol": {
				"identifier": "openconfig-policy-types:STATIC",
				"name": "icx-static",
				"config": {
					"identifier": "openconfig-policy-types:STATIC",
					"name": "icx-static"
				},
				"static-routes": {
					"static": [
						{
							"prefix": prefix,
							"config": {
								"prefix": prefix
								},
							"next-hops": {
								"next-hop": [
									{
										"index": nexthop,
										"config": {
											"index": nexthop,
											"next-hop": nexthop
										}
									}
								]
							}
						}
					]
				}	
			}
		}
		r = requests.post(url, headers=headers, auth=(username, password), json = body, verify=False)
		return r

	def deleteStaticRoute(self, host, username, password, prefix):
		prefix = prefix.replace("/", "%2F")
		url = "https://" + host + "/restconf/data/network-instances/network-instance/default-vrf/protocols/protocol/STATIC/icx-static/static-routes/static/" + prefix
		headers = headers = {
			'Accept': 'application/yang-data+json',
			'Content-Type': 'application/json'
		}
		r = requests.delete(url, headers=headers, auth=(username, password), verify=False)
		return r

	def createOSPFarea(self, host, username, password, area):
		url = "https://" + host + "/restconf/data/network-instances/network-instance/default-vrf/protocols"
		headers = headers = {
			'Accept': 'application/yang-data+json',
			'Content-Type': 'application/json'
		}
		body = {
			"protocol": [
				{
					"identifier": "OSPF",
					"name": "icx-ospf",
					"config": {
						"identifier": "OSPF",
						"name": "icx-ospf"
					},
					"ospfv2": {
						"areas": {
							"area": [
								{
									"identifier": area,
									"config": {
										"identifier": area
										}
									}
								]
							}
						}
					}
				]
			}
		r = requests.post(url, headers=headers, auth=(username, password), json = body, verify=False)
		return r

	def addOSPFareaToInterface(self, host, username, password, area, interface):
		url = "https://" + host + "/restconf/data/network-instances/network-instance/default-vrf/protocols/protocol/OSPF/icx-ospf/ospfv2/areas/area/" + area + "/interfaces"
		headers = headers = {
			'Accept': 'application/yang-data+json',
			'Content-Type': 'application/json'
		}
		body = {
			"interface": [
				{
					"id": 'ethernet ' + interface,
					"config": {
						"id": 'ethernet ' + interface
						}
					}
				]
			}
		r = requests.post(url, headers=headers, auth=(username, password), json = body, verify=False)
		return r

	def createVirtualInterfaceAndIpAddress(self, host, username, password, vlanID, prefix, mask):
		url = "https://" + host + "/restconf/data/interfaces"
		headers = headers = {
			'Accept': 'application/yang-data+json',
			'Content-Type': 'application/json'
		}
		body = {
			"interface": [
				{
					"name": 've ' + str(vlanID),
					"config": {
						"name": 've ' + str(vlanID),
						"type": "iana-if-type:l3ipvlan"
					},
					"openconfig-vlan:routed-vlan": {
						"config": {
							"vlan": str(vlanID)
						},
						"openconfig-if-ip:ipv4": {
							"addresses": {
								"address": [
									{
										"ip": prefix,
										"config": {
											"ip": prefix,
											"prefix-length": str(mask)
											}
										}
									]
								}
							}
						}
					}
				]
			}
		r = requests.post(url, headers=headers, auth=(username, password), json = body, verify=False)
		return r

	def writeMemory(self, host, SSHusername, SSHpassword):
		ssh = paramiko.SSHClient()
		ssh.load_system_host_keys()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(host, username = SSHusername, password = SSHpassword)
		channel = ssh.invoke_shell()

		channel.sendall('enable\n')
		time.sleep(3)
		s = channel.recv(4096)
		print (s)

		channel.sendall('write mem\n')
		time.sleep(3)
		s = channel.recv(4096)
		print (s)

		ssh.close()