import socket
from os import path
from sys import exit

# create and configure socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.settimeout(60)

# set default host and port number
HOST = 'localhost'
PORT = 9999
BUFFER = 1024


def upload_file(file_name):
    """
    Upload local file to server
    """

    print("UPLOAD MODE SELECTED")
    if not path.isfile(file_name):
        print("FILE NOT FOUND in local directory. \n")
        c.send(bytes("terminate", "utf-8"))
        return None

    c.send(bytes(file_name, "utf-8"))
    file = open(file_name, "rb")
    data = file.read(BUFFER)

    while data:
        print("Sending. . .")
        c.send(data)
        data = file.read(BUFFER)
    else:
        print("Upload successful!!!")

    file.close()
    c.send(b"DONE")
    print("SUCCESS\n")


def download_file(file_name):
    """
    Download file from server
    """

    print("DOWNLOAD MODE SELECTED")
    c.send(bytes(file_name, "utf-8"))
    recv_ack = c.recv(BUFFER)
    recv_ack = recv_ack.decode("utf-8")

    if recv_ack == "terminate":
        print("FILE NOT FOUND in Server \n")
        return None

    if path.isfile(file_name):
        file_name = "_duplicate_{}".format(file_name)
        print("DUPLICATE FILE RECEIVED. FILE RENAMED. \n")

    file = open(file_name, "wb")
    while True:
        data = c.recv(BUFFER)
        if data == b"DONE":
            print("File received successfully !!!")
            break
        print("Receiving. . . ")
        file.write(data)

    file.close()
    print("SUCCESS \n")


def main():
    try:
        c.connect((HOST, PORT))
    except Exception as e:
        print(e)
        return

    try:
        ack = c.recv(BUFFER)
    except Exception as e:
        print(e)
        c.close()
        return

    while True:
        print(ack.decode())

        option = input("Enter your choice: ")
        c.send(bytes(option, "utf-8"))

        if option == "1":
            file_name = input("Enter file name to upload: ")
            upload_file(file_name)
        elif option == "2":
            file_name = input("Enter file name to download: ")
            download_file(file_name)
        elif option == "quit":
            break
        else:
            print("wrong choice !!!")

    print("EXITING!!!")
    c.close()
    exit()


if __name__ == "__main__": main()