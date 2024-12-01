import socket
import threading
import requests
import json
from newsapi import NewsApiClient

apikey = "d07953f1256b41a6a39f2429c02f0d0e"
newsapi = NewsApiClient(api_key=apikey)

def get_headlines(params):
    try:
        response = newsapi.get_top_headlines(**params)  # Call the API with params
        return response 
    except Exception as e:
        print("Error fetching headlines: ", e)
        #return None

def get_sources(params):
    try:
        response = newsapi.get_sources(**params)  # Call the API with params
        return response  
    except Exception as e:
        print("Error fetching sources:", e)
        

def handle_client(sock, clientID):  
    print(30 * "-")
    print("New connection from", clientID[0], "is accepted", "with the port number:", clientID[1])
    print("Wait for the client to send a request")

    while True:
        try:
            user_name=socke.recv(2048).decode()  
            print("this user is",user_name)
            data = sock.recv(2084).decode()  # Receive data from client
            values = data.split("|")
            print("This is the server values:", values)
            request, subRequest, dataRequested = values

            print("Requested service type is:", request)
            print("Requested sub is:", subRequest)
            print("Requested data is:", dataRequested)

        except Exception as e:
            print("Error receiving data: ", e)
            break

        # If client chose to quit
        if request == "quit":        
            print("Client", clientID, "has quit the connection")
            sock.sendall("Goodbye!".encode('ascii'))
            break

        elif request == "headlines": 
            params = { "apiKey": apikey, "pageSize": 15 }
            try:
                # Searching by a keyword 
                if subRequest == "key-word": 
                    params["q"] = dataRequested

                # Searching by category 
                elif subRequest == "by_category":
                    categories = {
                        "business_news": "business",
                        "general_news": "general",
                        "health_news": "health",
                        "science_news": "science",
                        "sport_news": "sports",
                        "technology_news": "technology"
                    }
                    category = categories.get(dataRequested)
                    if category:
                        params["category"] = category
                    else:
                        print("Invalid category entered by the user")
                        sock.sendall("Invalid headline category code entered by the client.".encode('ascii'))
                        continue

                # Searching by country 
                elif subRequest == "by_country": 
                    countries = {  
                        "au_news": "au", "ca_news": "ca", "jp_news": "jp", "ae_news": "ae",
                        "sa_news": "sa", "kr_news": "kr", "us_news": "us", "ma_news": "ma"
                    }
                    country = countries.get(dataRequested)
                    if country:
                        params["country"] = country
                    else:
                        print("Invalid country code entered by the user")
                        sock.sendall("Invalid headline country code entered by the client.".encode('ascii'))
                        continue

                # If client chose to list all headlines
                elif subRequest == "list_all":  
                    pass
                else:
                    sock.sendall("Invalid subRequest type.".encode('ascii'))
                    continue

            except Exception as e:
                print("Error handling headlines subrequests", e)   

            # Extracting the headlines 
            results = get_headlines(params)
            if results:
                titles = []
                articles = results.get('articles', [])
                for article in articles:
                    if article.get('title'):
                        titles.append(article['title'])
                titles_str = "\n".join(titles)  # Join all titles into a string 
            else:
                titles_str = "No results found."

            # Send the titles
            sock.sendall(titles_str.encode('ascii'))

        elif request == "sources":
            params = { "apiKey": apikey, "pageSize": 15 }
            try: 
                if subRequest == "by_category":
                    categories = {
                        "business_sources": "business",
                        "general_sources": "general",
                        "health_sources": "health",
                        "science_sources": "science",
                        "sport_sources": "sports",
                        "technology_sources": "technology"
                    }
                    category = categories.get(dataRequested)
                    if category:
                        params["category"] = category
                    else:
                        print("Invalid source category entered by the user")
                        sock.sendall("Invalid source category code entered by the client.".encode('ascii'))
                        continue

                elif subRequest == "by_country":
                    countries = {
                        "au_sources": "au", "ca_sources": "ca", "jp_sources": "jp", "ae_sources": "ae",
                        "sa_sources": "sa", "kr_sources": "kr", "us_sources": "us", "ma_sources": "ma"
                    }
                    country = countries.get(dataRequested)
                    if country:
                        params["country"] = country
                    else:
                        print("Invalid source country code entered by the user")
                        sock.sendall("Invalid source country code entered by the client.".encode('ascii'))
                        continue

                elif subRequest == "by_language":
                    languages = { "ar": "arabic", "en": "english" }
                    language = languages.get(dataRequested)
                    if language:
                        params["language"] = dataRequested
                    else:
                        print("Invalid language code entered by the user")
                        sock.sendall("Invalid language code entered by the client.".encode('ascii'))
                        continue

                # If client chose to list all sources
                elif subRequest == "list_all":
                    pass
                else:
                    sock.sendall("Invalid subRequest type.".encode('ascii'))
                    continue

                # Sending the results 
                results = get_sources(params)
                if results:
                    sources = []
                    articles = results.get('sources', [])
                    for source in articles:
                        if source.get('name'):
                            sources.append(source['name'])
                    sources_str = "\n".join(sources)
                else:
                    sources_str = "No results found."


            
            except Exception as e:
                print("Error processing sources request: ", e)

            # Sending the sources
            sock.sendall(sources_str.encode('ascii'))

        # Close the socket after sending response
        sock.close()

def handle_server():
    print(30 * "-")
    print("The server is running")
    ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssocket.bind(("127.0.0.1", 49999))
    ssocket.listen(5)
    print("The server is now waiting for client")
    while True:
        sock, clientID = ssocket.accept()
        clientthread = threading.Thread(target=handle_client, args=(sock, clientID))
        clientthread.start()

# Start the server
handle_server()