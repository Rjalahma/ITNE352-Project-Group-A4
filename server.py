import socket
import threading
import time
import requests

def handle_client(sock, clientID):  
   
     print(30 * "-")
     print("New connection from", clientID[0], "is accepted", "with the port number:", clientID[1])
     print("Wait for the client to send a request")
     apikey="d07953f1256b41a6a39f2429c02f0d0e"

     while True:
      
       try:  
            data =sock.recv(2084).decode()
            values = data.split("|")
            print(" this is the server values ",values)
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
         
        
       elif request=="headlines": 
        url="https://newsapi.org/v2/top-headlines"
        params = { "apiKey": apikey, "pageSize": 15 }
        try:
           # searching by a keyword 
           if subRequest=="key-word": 
             params["q"] = dataRequested

            # searching by category 
           elif subRequest=="by_catogry":
                categories = {
                        "business_news": "business",
                        "general_news": "general",
                        "health_news": "health",
                        "science_news": "science",
                        "sport_news": "sports",
                        "technology_news": "technology"  }
                category= categories.get(dataRequested)
                if category:
                     params["category"] = category
                else:
                   print("inavlid catogery by the user")
                   sock.sendall("Invalid headline category code entered by the client.".encode('ascii'))

            # searching by country 
           elif subRequest=="by_country": 
                 countries = {  "au_news": "au",
                                "ca_news": "ca",
                                "jp_news": "jp",
                                "ae_news": "ae",
                                "sa_news": "sa",
                                "kr_news": "kr",
                                "us_news": "us",
                                "ma_news": "ma"   }
        
                 country=countries.get(dataRequested)
                 if country:
                    params["country"] = country

                 else:
                   print("the client enterd wrong headline country code, wait fot the client to enter again")
                   sock.sendall("Invalid headline country code entered by the client.".encode('ascii'))
                   break
                   #.......return or break?

            # if client chose to list all headlines
           elif subRequest=="list_all":  
              pass
              
           else:
                    sock.sendall("Invalid subRequest type.".encode('ascii'))
                    break
           
        except Exception as e :
           print("error handling headlines subrequests", e)   

            #sending the results  :
        print("now we will start getting the request")   # for testing purposes 
        response = requests.get(url, params=params)

        print("now we will save it into json file")   # for testing purposes         
        results=response.json()

        articles=results.get('articles')
        print("we will extract titles to send them ")   # for testing purposes    

        titles = []
        for article in articles:
         title= article.get('title')
         if title:  
               titles.append(title)

        print("titles are extracted , now they will be sent ") # for testing purposes  
        titles_str = "\n".join(titles)  
        print(titles_str)  # for testing purposes  

        sock.sendall(titles_str.encode('ascii'))
        print("titles already sent ")   # for testing purposes  
 
       elif request=="sources":
        url="https://newsapi.org/v2/top-headlines/sources"
        params = { "apiKey": apikey, "pageSize": 15 }

        try: 
           if subRequest=="by_catogry":
                
                categories = {
                        "business_sources": "business",
                        "genral_sources": "general",
                        "health_sources": "health",
                        "seince_source": "science",
                        "sport_sources": "sports",
                        "technology_sources": "technology"  }
                category= categories.get(dataRequested)

                if category:
                     params["category"] = category

                else:
                   print("inavlid source catogery by the user")
                   sock.sendall("Invalid source category code entered by the client.".encode('ascii'))

           elif subRequest=="by_country":
                 countries = {
                        "au_sources": "au",
                        "ca_sources": "ca",
                        "jp_sources": "jp",
                        "ae_sources": "ae",
                        "sa_sources": "sa",
                        "kr_sources": "kr",
                        "us_sources": "us",
                        "ma_sources": "ma"
                        }
                 country=countries.get(dataRequested)

                 if country:
                    params["country"] = country

                 else:
                   print("the client enterd wrong source country code, wait fot the client to enter again")
                   sock.sendall("Invalid  source country code entered by the client.".encode('ascii'))
                   break
                 
           elif subRequest=="by_language":
                    
                    languages = {  "ar": "arabic","en": "english"  }
                    language = languages.get(dataRequested)
                    if language:
                        params["language"] = dataRequested
                    else:
                        print("the client enterd unavaliable language, wait fot the client to enter again")
                        sock.sendall("Invalid language code entered by the client.".encode('ascii'))
                        break

            # if client chose to list all sources
           elif subRequest=="list_all":
              pass
           else:
                    sock.sendall("Invalid subRequest type.".encode('ascii'))
                    break

                 #sending the results   
           print("now we will start getting the request")   # for testing purposes 
           response=requests.get(url, params=params)
           if response.status_code == 200:
                results=response.json()
                print("now we will save it into json file")   # for testing purposes
                titles=results ['title']
                print("titles are extracted , now they will be sent ")   # for testing purposes
                sock.sendall(titles.encode('ascii'))
                print("titles already sent ")   # for testing purposes 
           else:
                sock.sendall("Error: Failed to fetch sources data. Status code :".encode('ascii'),response.status_code)

        except Exception as e:
                print("Error processing sources request: ",e)

                
       sock.close()
    
     
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