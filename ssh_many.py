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

ios_device = {
    'device_type': 'cisco_ios',
    'ip': devices[0],
    'username': username,
    'password': password,
}

print ios_device
