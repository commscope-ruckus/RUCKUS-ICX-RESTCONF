import time
import paramiko

host = '10.0.0.213'
SSHusername = 'admin'
SSHpassword = 'password'

def writeMemory(host, SSHusername, SSHpassword):
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

writeMemory(host, SSHusername, SSHpassword)