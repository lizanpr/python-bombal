import getpass
import sys
import telnetlib

HOST = ["172.25.99.1", "172.25.99.2", "172.25.99.3", "172.25.99.4"]

user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

for ip in HOST[:]:

    tn = telnetlib.Telnet(ip)

    tn.read_until("Username: ")
    tn.write(user + "\n")

    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("config t\n")

    for n in range (1,6):
        tn.write("interface loop " + str(n) + "\n")
        tn.write("description PY_LOOP-" + str(n) + "\n")

    tn.write("end\n")
    tn.write("wr\n")
    tn.write("exit\n")

    print tn.read_all()
