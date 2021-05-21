import socket
from sys import exit

# create and configure socket
c = socket.socket()
c.settimeout(30)

# set default host and port number
HOST = 'localhost'
PORT = 1999

# try to connect to server using default values
try:
    c.connect((HOST, PORT))
except Exception as e:
    print(e)
    exit()

# upon successful connection print the acknowledgement
try:
    data = c.recv(1024)
    print(data.decode())
except Exception as e:
    print(e)
    c.close()
    exit()

# keep sending data to server and receive the echo from the server
try:
    while True:
        buffer = input("Enter data to be sent: ")
        c.send(bytes(buffer, "utf-8"))

        # is client enters exit then terminate the connection
        if buffer == "exit":
            print("CONNECTION TERMINATED BY CLIENT")
            break

        data = c.recv(1024)
        print("Received data from server: {}".format(data.decode()))
        print("Echo successful")

except Exception as e:
    print(e)

finally:
    c.close()
    print("EXITING !!!")
