import socket
import threading


def send():
    msg = True

    while msg:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # get local machine name
        host = "192.168.0.36"
        #host = socket.gethostname()
        port = 8080
        # connection to hostname on the port.
        s.connect((host, port))
        msg = input("Say >> ")
        s.send(msg.encode())
        s.close()

def recv():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = "192.168.0.33"

    port = 8080

    # bind to the port
    s.bind((host, port))

    # queue up to 5 requests
    s.listen(5)

    while True:
        # establish a connection

        clientsocket, addr = s.accept()

        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = clientsocket.recv(1024).decode()
        print("\nUser >> " + str(data))
        clientsocket.close()

try:
    thread_send = threading.Thread(target=send)
    thread_recieve = threading.Thread(target=recv)
    thread_recieve.start()
    thread_send.start()

except Exception as e:
   print ("Error: unable to start thread")


