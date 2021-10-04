from RUCKUS_ICX_API_calls import ICX_API_calls
ICX = ICX_API_calls()

host = '10.0.0.213'
username = 'admin'
password = 'password'
vlanID = 45

response = ICX.enableRSTP(host, username, password, vlanID)
print (response)

if str(response) == '<Response [201]>':
	ICX.writeMemory(host, username, password)