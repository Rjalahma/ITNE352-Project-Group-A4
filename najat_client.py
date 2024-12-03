import socket
server_add=("127.0.0.1",49999)
# clinet_sock=None
username_sent=False
# changed 
clinet_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clinet_sock.connect(("127.0.0.1",49999))


# def client_connaction():
#     global clinet_sock
#     try :
#         if clinet_sock:
#              clinet_sock.close()
#         clinet_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#         clinet_sock.connect(server_add)
#         print("conaction is esablished")
#     except Exception as e:
#         print(" error at esablishing the connaction")
def send_choice(message):
    try:
        clinet_sock.send(message.encode('utf-8'))
        # print(" inside send client ")
        # clinet_sock.send(request_type.encode("ascii"))
        # print("")
        # clinet_sock.send(sub_menue_choise.encode("ascii"))
        # print("")
        # clinet_sock.send(msg.encode("ascii"))
        # data = clinet_sock.recv(1024).decode("ascii")
        # clinet_sock.close()
        # return data
    except Exception as e:
        print("Error in sending:", e)
        # client_connaction()

def send_username_request(username,request_type,sub_menue_choise,msg):
    # global username_sent
    # if not username_sent:
    try:
        message = "|".join([username,request_type,sub_menue_choise,msg])
        clinet_sock.send(message.encode("ascii"))
        # username_sent = True
        print(" user name and request is  sent from najat client ")
        print(" the message is ",message)
    # else:
    except Exception as e:
        print("  error at sending username and request from najat client ")
def recv():
    try :

        data = clinet_sock.recv(1024).decode('utf-8')
        return data
    except Exception as e:
        print("Error in reciving:", e)
def client_close():
    try :
         if clinet_sock:
            clinet_sock.close()
            print(" conaction is closed ")
    except Exception as e :
        print(" eroor at closing the client ")
# import Najat_gui as f
# n=True
# while n==True:
# f.start_gui()

# if f.is_clicked():
#     print(" this is my client ")    
#     # request_type,sub_menue_choise,msg=f.return_data()
#     print("inside is clicked")
#     if request_type =="error":
#         print("")
#     elif request_type=="quit":
#         n=False
#     else:
#         print("")
       
        
#         print( "data recived",data)
#         print("")
#         f.view_data(data)    
# else:
#     print("")
# f.root.mainloop()
# client_connaction()   
