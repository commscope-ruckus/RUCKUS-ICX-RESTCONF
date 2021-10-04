from RUCKUS_ICX_API_calls import ICX_API_calls
ICX = ICX_API_calls()

host = '10.0.0.213'
username = 'admin'
password = 'password'
vlanID = 45

response = ICX.disableRSTP(host, username, password, vlanID)
print (response)

if str(response) == '<Response [204]>':
	ICX.writeMemory(host, username, password)