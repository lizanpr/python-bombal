import os
import sys
from sys import argv
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException

script, devices_file, commands_file = argv

with open(devices_file) as f:
    devices = [line.strip() for line in f]

with open(commands_file) as f:
    commands = [line.strip() for line in f]

username = raw_input("Enter your username: ")
password = raw_input("Enter your password: ")

if os.path.exists("C:\connection_failure.txt"):
    os.remove('C:\connection_failure.txt')
else:
    pass

for device in devices:

    print 'Trying device ' + device + "..."

    ios_device = {
        'device_type': 'cisco_ios',
        'ip': device,
        'username': username,
        'password': password,
    }

    try:
        net_connect = ConnectHandler(**ios_device)

    except (SSHException, NetMikoTimeoutException, NetMikoAuthenticationException):
        print "Cannot connect to device " + device
        fail = open('C:\connection_failure.txt', 'a')
        fail.write("Cannot connect to device " + device + '\n')
        fail.close()

    else:
        # Backup current sys.stdout
        old_stdout = sys.stdout
        # Class for redirecting stdout to both terminal and file
        class Logger(object):
            def __init__(self):
                self.terminal = sys.stdout
                self.log = open('C:\config-' + device + '.txt','w')

            def write(self, message):
                self.terminal.write(message)
                self.log.write(message)

        sys.stdout = Logger()
        # send_config_set enters and exits config mode automatically. Use 'do'
        # to execute exec-mode commands such as show
        output = net_connect.send_config_set(commands)
        print output

        # Restore sys.stdout with the backup
        sys.stdout = old_stdout

print "The script has completed."
