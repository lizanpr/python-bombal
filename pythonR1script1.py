import getpass
import sys
import telnetlib

HOST = "172.25.179.2"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("config t\n")
tn.write("int loop 3\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()