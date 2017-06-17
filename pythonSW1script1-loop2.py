import getpass
import sys
import telnetlib

user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

for n in range(1,5):

    host = "172.25.99." + str(n)

    tn = telnetlib.Telnet(host)

    tn.read_until("Username: ")
    tn.write(user + "\n")

    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("config t\n")

    for n in range (7,11):
        tn.write("interface loop " + str(n) + "\n")
        tn.write("description PY_LOOP-" + str(n) + "\n")

    tn.write("end\n")
    tn.write("wr\n")
    tn.write("exit\n")

    print tn.read_all()
