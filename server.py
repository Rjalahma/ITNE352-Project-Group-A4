import socket
import threading
import time
#import sys

def handle_server():
   socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.bind(("127.0.0.1", 49999))
   print(30 * "-")
   print("the server is running")
   socket.listen(5)
   print("the server now are waiting for client")
   while True:
    sock,clientID=socket.accept 
    clientthread=threading.thread(target=handle_client, arg=(sock,clientID))
    clientthread.start()


 
def handle_client(sock, clientID):  
   #try:
     print(30 * "-")
     print("New connection from", clientID[0], "is accepted", "with the port number:", clientID[1])
     print("Wait for the client to send a request")
     while True:
        request=sock.recv(2048).decode('ascii')
        print("requested service is: ", request)
        if request=="quit":
         print("Client ",clientID,"has quit the connection")
         sock.sendall("Goodbye!".encode('ascii'))
         break
        elif request==2:
           print("the client want to list all sources")
           msg= ("imagine there is sourcse")
   #finally:
     #print()
           

     

if __name__ == "__main__":
    handle_server()
