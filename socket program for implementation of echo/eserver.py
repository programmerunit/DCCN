import socket
from sys import exit

# create socket class object
s = socket.socket()

# set default host and port number
HOST = 'localhost'
PORT = 1999

# bind port number to the host
try:
    s.bind((HOST, PORT))
except Exception as e:
    print(e)
    exit()

# set timeout duration
s.settimeout(60)
print("BINDING SUCCESSFUL")

# start server and listen to client connection requests
s.listen()
print("Server is listening. . . ")

try:
    conn, addr = s.accept()
except Exception as e:
    print(e)
    s.close()
    exit()

# on successful connection send an acknowledgement
print('CONNECTION ESTABLISHED with {}'.format(addr))
conn.send(bytes("CONNECTED WITH SERVER", "utf-8"))

# keep receiving data from client and echo it back to the client
try:
    while True:
        data = conn.recv(1024)

        # if server receives exit command then terminate the connection
        if data.decode() == "exit":
            break

        print(data.decode())
        conn.send(bytes(data))

except Exception as e:
    print(e)

finally:
    conn.close()
    print("CONNECTION TERMINATED WITH {}".format(addr))
    s.close()
    print("EXITING !!!")
