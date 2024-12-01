import socket
import threading
import time

def handle_client(sock, clientID):  
   
    print(30 * "-")
    print("New connection from", clientID[0], "is accepted", "with the port number:", clientID[1])
    print("Wait for the client to send a request")

    while True:
      
          
        try:  
            # request=sock.recv(2048).decode('ascii')
            data =sock.recv(2084).decode()
            values = data.split("|")
            print(" this is the server values ",values)
            # print("requested service type is: ", request)
            # request=sock.recv(2048).decode('ascii')
            # print("requested sub is: ", subRequest)
            # dataRequested=sock.recv(2048).decode('ascii')    
            # print("requested data is: ", dataRequested)
            request, subRequest,dataRequested = values

            print("requested service type is: ", request)
            print("requested sub is: ", subRequest)
            print("requested data is: ", dataRequested)
        except Exception as e:
            print("Error receiving data: ",e)
            break
        

            # if client chose to quit
        if request=="quit":        
            print("Client ",clientID,"has quit the connection")
            sock.sendall("Goodbye!".encode('ascii'))
            break
        
            # if client chose to search by headings
        elif request=="headlines":  
            
            try:
                if subRequest=="key-word": 
                    msg="keyword headings"
                elif subRequest=="by_catogry":
                    if dataRequested=="business_news":
                        msg="business headings"
                    elif dataRequested=="genral_news":
                        msg="general headings"
                    elif dataRequested=="health_news":
                        msg="health headings"
                    elif dataRequested=="seince_news":
                        msg="science headings"
                    elif dataRequested=="sport_news":
                        msg="sport headings"
                    elif dataRequested=="technology_news":
                        msg="technology headings"
                    else:
                        print("the client enterd wrong input, wait fot the client to enter again")

                elif subRequest=="by_country": 
                    if dataRequested=="au_news":
                        msg="Australia headings"
                    elif dataRequested=="ca_news":
                        msg="Canada headings"
                    elif dataRequested=="jp_news":
                        msg="japan headings"
                    elif dataRequested=="ae_news":
                        msg="United Arab Emirates headings"
                    elif dataRequested=="sa_news":
                        msg="Saudi Arabia headings"
                    elif dataRequested=="kr_news":
                        msg="South Korea headings"
                    elif dataRequested=="us_news":
                        msg="United States headings"
                    elif dataRequested=="ma_news":
                        msg="Morocco headings"
                    else:
                        print("the client enterd wrong country code, wait fot the client to enter again")

                elif subRequest=="list_all":  
                    msg="all headings"   
                #????? in client code shouldnt we add else option for if the user enterd somrthing is not in the list? after line 94
            except Exception as e:
                    print(f"Error processing headlines request: {e}")
                    msg = "Error processing headlines request"

           # if client chose to list all sources
        elif request=="sources":  
            try: 
                if subRequest=="by_catogry":
                    if dataRequested=="business_sources":
                        msg="all business sources"
                    elif dataRequested=="genral_sources":
                        msg="all general sources"
                    elif dataRequested=="health_sources":
                        msg="all health sources"
                    elif dataRequested=="seince_sources":
                        msg="all scince sources"
                    elif dataRequested=="sport_sources":
                        msg="all sport sources"
                    elif dataRequested=="technology_sources":
                        msg="all technology sources"
                    else:
                        print("the client wrote unvlaid catogry, wait fot the client to enter again")
                elif subRequest=="by_country":
                    if dataRequested=="au_sources":
                        msg="Australia sources"
                    elif dataRequested=="ca_sources":
                        msg="Canada sources"
                    elif dataRequested=="jp_sources":
                        msg="japan sources"
                    elif dataRequested=="ae_sources":
                        msg="United Arab Emirates sources"
                    elif dataRequested=="sa_sources":
                        msg="Saudi Arabia sources"
                    elif dataRequested=="kr_sources":
                        msg="South Korea sources"
                    elif dataRequested=="us_sources":
                        msg="United States sources"
                    elif dataRequested=="ma_sources":
                        msg="Morocco sources"
                    else:
                        print("the client enterd wrong country code, wait fot the client to enter again")
                elif subRequest=="by_language":
                    if dataRequested=="ar":
                        msg="arabic sources"
                    elif dataRequested=="en":
                        msg="english sources" 
                    else:
                        print("the client enterd unavaliable language, wait fot the client to enter again")
                elif subRequest=="list_all":
                    if dataRequested=="all_sources": 
                        msg="all sources" 

            except Exception as e:
                    print("Error processing sources request: ",e)

       #try:          
        print("data sent already",sock.send(msg.encode('ascii'))  ) 
    sock.close()
       #except Exception as e:
        #print(f"Error sending data: {e}")
     
def handle_server():
   print(30 * "-")
   print("the server is running")
   ssocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
   ssocket.bind(("127.0.0.1", 49999))
   ssocket.listen(5)
   print("the server now is waiting for client")
   while True:
    sock,clientID=ssocket.accept()
    clientthread=threading.Thread(target=handle_client, args=(sock,clientID))
    clientthread.start()

 

            
handle_server()