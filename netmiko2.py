from netmiko import ConnectHandler

# Script for sending a list of commands using a loop
# to a list of devices

ios_1 = {
    'device_type': 'cisco_ios',
    'ip': '172.25.99.1',
    'username': 'cisco',
    'password': 'cisco',
}

ios_2 = {
    'device_type': 'cisco_ios',
    'ip': '172.25.99.2',
    'username': 'cisco',
    'password': 'cisco',
}

ios_3 = {
    'device_type': 'cisco_ios',
    'ip': '172.25.99.3',
    'username': 'cisco',
    'password': 'cisco',
}

ios_4 = {
    'device_type': 'cisco_ios',
    'ip': '172.25.99.4',
    'username': 'cisco',
    'password': 'cisco',
}

all_devices = [ios_1, ios_2, ios_3, ios_4]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range(21,36):
       print "Creating Loopback " + str(n)
       config_commands = ['interface loopback ' + str(n), 'description Python_LOOP-' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print output
