import paramiko
import time

ip_address = "172.25.99.1"
username = "cisco"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("configure terminal\n")
remote_connection.send("int loop 21\n")
remote_connection.send("description PY_LOOP-21\n")
remote_connection.send("int loop 22\n")
remote_connection.send("description PY_LOOP-22\n")
remote_connection.send("int loop 23\n")
remote_connection.send("description PY_LOOP-23\n")
remote_connection.send("int loop 24\n")
remote_connection.send("description PY_LOOP-24\n")
remote_connection.send("int loop 25\n")
remote_connection.send("description PY_LOOP-25\n")

for n in range (26,31):
    print "Creating more loopbacks " + str(n)
    remote_connection.send("int loop " + str(n) + "\n")
    remote_connection.send("description PY_LOOP-" + str(n) + "\n")
    time.sleep(0.5)

remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print output

ssh_client.close
