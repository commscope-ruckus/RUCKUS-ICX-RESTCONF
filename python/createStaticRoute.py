from RUCKUS_ICX_API_calls import ICX_API_calls
ICX = ICX_API_calls()

host = '10.0.0.213'
username = 'admin'
password = 'password'
prefix = '33.33.33.0/24'
netxhop = '10.0.0.1'

response = ICX.createStaticRoute(host, username, password, prefix, netxhop)
print (response)

if str(response) == '<Response [201]>':
	ICX.writeMemory(host, username, password)