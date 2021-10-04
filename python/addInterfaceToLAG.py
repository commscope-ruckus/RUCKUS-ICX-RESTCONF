from RUCKUS_ICX_API_calls import ICX_API_calls
ICX = ICX_API_calls()

host = '10.0.0.213'
username = 'admin'
password = 'password'
lagID = 27
interface = '1/1/9'

response = ICX.addPortsToLAG(host, username, password, lagID, interface)
print (response)

if str(response) == '<Response [201]>':
	ICX.writeMemory(host, username, password)