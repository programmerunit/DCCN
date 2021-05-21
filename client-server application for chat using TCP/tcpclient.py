import socket
from sys import exit

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set default host and port number
HOST = 'localhost'
PORT = 9999
SNAME = "SERVER"

# set server username
c_name = input("Enter client nickname (Leave it blank for default): ")
if c_name == "" or c_name == None:
    c_name = "CLIENT"

# try to connect to server using default values
try:
    c.connect((HOST, PORT))

except Exception as e:
    print(e)
    exit()
c.settimeout(60)
# exchange usernames and print acknowledgement
try:
    c.send(bytes(c_name, "utf-8"))
    SNAME = c.recv(1024)
    SNAME = SNAME.decode()
except:
    print("USERNAME FETCHING ERROR. DEFAULT USERNAMES TAKEN !!!")
finally:
    print("Connected with {} \n".format(SNAME))

try:
    while True:
        msg = input("{}: ".format(c_name))
        c.send(bytes(msg, "utf-8"))

        if msg == "quit":
            print("DISCONNECTED BY CLIENT")
            break

        ser_msg = c.recv(1024)
        print("{}: {}".format(SNAME, ser_msg.decode()))

except Exception as e:
    print(e)

finally:
    c.close()
    print("EXITING !!!")