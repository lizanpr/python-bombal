from netmiko import ConnectHandler

# Devices are listed specifically, commands are read from files
# and applied to corresponding devices.

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
	'ip': '192.168.122.74',
	'username': 'david',
	'password': 'cisco',
}

with open('iosv_l2_config1') as f:
    lines1 = f.read().splitlines()
print lines1

with open('iosv_l2_config2') as f:
    lines2 = f.read().splitlines()
print lines2

core_devices = [iosv_l2_s1, iosv_l2_s2]

access_devices = [iosv_l2_s3, iosv_l2_s4]

for devices in core_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines1)
    print output

for devices in access_devices:
    net_connect = ConnectHandler(**devices)
	output = net_connect.send_config_set(lines2)
	print output