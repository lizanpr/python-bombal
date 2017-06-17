import getpass
import sys
import telnetlib
from sys import argv

script, filename, commands = argv

user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

with open(filename) as targets:

    for line in targets:

        print "Backing up configuration for " + line

        host = line.strip()

        tn = telnetlib.Telnet(host)

        tn.read_until("Username: ")
        tn.write(user + "\n")

        if password:
            tn.read_until("Password: ")
            tn.write(password + "\n")

        with open(commands) as instructions:

            for line in instructions:
                tn.write(line)

        tn.write("exit\n")

        readoutput = tn.read_all()
        saveoutput = open("switch_" + host, "w")
        saveoutput.write(readoutput)
        saveoutput.close()
