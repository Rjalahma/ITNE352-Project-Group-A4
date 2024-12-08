import socket
server_add=("127.0.0.1",49999)
username_sent=False
clinet_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clinet_sock.connect(("127.0.0.1",49999))
# send the the name or title to server
def send_choice(message):
    try:
        print(f"Sending choice to server: {message}")
        clinet_sock.send(message.encode('utf-8'))

    except Exception as e:
        print("Error in sending:", e)
# send the request to client
def send_username_request(username,request_type,sub_menue_choise,msg):

    try:
        message = "|".join([username,request_type,sub_menue_choise,msg])
        clinet_sock.send(message.encode("ascii"))
        print(" user name and request is  sent from najat client ")
        print(" the message is ",message)
    except Exception as e:
        print("  error at sending username and request from najat client ")
# recv the data from the server
def recv():
    try :

        data = clinet_sock.recv(10000).decode('utf-8')
        return data
    except Exception as e:
        print("Error in reciving:", e)
# close the client socket 
def client_close():
    try :
         if clinet_sock:
            clinet_sock.close()
            print(" conaction is closed ")
    except Exception as e :
        print(" eroor at closing the client ")