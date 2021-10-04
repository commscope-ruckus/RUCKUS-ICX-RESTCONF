from RUCKUS_ICX_API_calls import ICX_API_calls
ICX = ICX_API_calls()

host = '10.0.0.213'
username = 'admin'
password = 'password'
prefix = '33.33.33.0/24'

response = ICX.deleteStaticRoute(host, username, password, prefix)
print (response)

if str(response) == '<Response [204]>':
	ICX.writeMemory(host, username, password)