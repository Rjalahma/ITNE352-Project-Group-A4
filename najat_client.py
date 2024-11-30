import socket


def send(message):
    clinet_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clinet_sock.connect(("127.0.0.1",49999))
   
    clinet_sock.send(message.encode("ascii"))
    # print(" inside send client ")
    # clinet_sock.send(request_type.encode("ascii"))
    # print("")
    # clinet_sock.send(sub_menue_choise.encode("ascii"))
    # print("")
    # clinet_sock.send(msg.encode("ascii"))
    data = clinet_sock.recv(1024).decode("ascii")
    clinet_sock.close()
    return data

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
    
