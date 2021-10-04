from RUCKUS_ICX_API_calls import ICX_API_calls
ICX = ICX_API_calls()

host = '10.0.0.213'
username = 'admin'
password = 'password'
area = '100'
interface = '1/3/1'

response = ICX.addOSPFareaToInterface(host, username, password, area, interface)
print (response)

if str(response) == '<Response [201]>':
	ICX.writeMemory(host, username, password)