from RUCKUS_ICX_API_calls import ICX_API_calls
ICX = ICX_API_calls()

host = '10.0.0.213'
username = 'admin'
password = 'password'
lagID = 30
lagName = 'lag'

response = ICX.createDynLAG(host, username, password, lagName, lagID)
print (response)

if str(response) == '<Response [201]>':
	ICX.writeMemory(host, username, password)