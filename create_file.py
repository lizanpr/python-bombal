filename = open("devices.txt", 'w')

for n in range(1,5):

    filename.write("172.25.99." + str(n) + "\n")

filename.close()
