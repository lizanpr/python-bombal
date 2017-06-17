from netmiko import ConnectHandler

# Script for sending a single command or a list of commands
# using a loop to a single device

ios = {
    'device_type': 'cisco_ios',
	'ip': '172.25.178.10',
	'username': 'cisco',
	'password': 'cisco',
}

net_connect = ConnectHandler(**ios)
output = net_connect.send_command('show ip int brief')
print output

config_commands = ['int loop 100', 'description PY_LOOP-100']
output = net_connect.send_config_set(config_commands)
print output

for n in range(101,111):
    print "Creating loopback " + str(n)
    config_commands = ['int loop ' + str(n), 'description PY_LOOP-' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print output