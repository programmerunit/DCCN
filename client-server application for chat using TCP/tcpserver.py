import socket
from sys import exit

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set default host and port number
HOST = 'localhost'
PORT = 9999
CNAME = "CLIENT"

# set server username
s_name = input("Enter server nickname (Leave it blank for default): ")
if s_name == "" or s_name == None:
    s_name = "SERVER"

# bind port number to the host
try:
    s.bind((HOST, PORT))
except Exception as e:
    print(e)
    exit()

# configure and start server
s.settimeout(60)
s.listen()
print("WAITING FOR CLIENT. . . ")

try:
    client, addr = s.accept()
except Exception as e:
    print(e)
    s.close()
    exit()

# exchange usernames and print acknowledgement
try:
    CNAME = client.recv(1024)
    CNAME = CNAME.decode()
    client.send(bytes(s_name, "utf-8"))
except:
    print("USERNAME FETCHING ERROR. DEFAULT USERNAMES TAKEN !!!")
finally:
    print('Connected with {} \n'.format(CNAME))

try:
    while True:
        cli_msg = client.recv(1024)

        if cli_msg.decode() == "quit":
            break

        print("{}: {}".format(CNAME, cli_msg.decode()))
        msg = input("{}: ".format(s_name))
        client.send(bytes(msg, "utf-8"))

except Exception as e:
    print(e)

finally:
    client.close()
    print("{} DISCONNECTED".format(CNAME))
    s.close()
    print("EXITING !!!")
