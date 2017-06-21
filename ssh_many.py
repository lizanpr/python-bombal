import sys
from sys import argv
from netmiko import ConnectHandler

script, devices_file, commands_file = argv

with open(devices_file) as f:
        devices = [line.strip() for line in f]

with open(commands_file) as f:
        commands = [line.strip() for line in f]

username = raw_input("Enter your username: ")
password = raw_input("Enter your password: ")

for device in devices:

    print 'Configuring device ' + device

    fd = open('C:\config-' + device + '.txt','w')
    # Capture standard output to hidden system output (my interpretation)
    old_stdout = sys.stdout
    # Redirect system output to the file object
    sys.stdout = fd

    ios_device = {
        'device_type': 'cisco_ios',
        'ip': device,
        'username': username,
        'password': password,
    }

    net_connect = ConnectHandler(**ios_device)

    # Loop for sending comands from a list without entering config mode
    # for command in commands:
    #     output = net_connect.send_command(command)
    #     print output

    # send_config_set enters and exits config mode automatically
    output = net_connect.send_config_set(commands)
    print output

    fd.close()
    # Return system output to visible standard output
    sys.stdout = old_stdout
