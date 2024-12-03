import socket
import threading
import json
from newsapi import NewsApiClient

apikey = "d07953f1256b41a6a39f2429c02f0d0e"
newsapi = NewsApiClient(api_key=apikey)

def save_to_json(client_name, option, group_id, data):
    file_name=f"{client_name}_{option}_{group_id}.json"
    print("file created")
    with open (file_name,'w') as f :
        json.dump(data, f , indent=4)
        print("data saved to :", file_name)
        #data=json.load(f)
        return data 
    print("file data loaded in object data")


def get_headlines(params):
    try:
        print("the headlines request is processing ")
        print("")
        APIresponse = newsapi.get_top_headlines(**params)  # Call the API with params
        print("the headline response is saved")
        print("")
        #print("this is the response from api:",APIresponse)# for testing 
        return APIresponse 
    except Exception as e:
        print("Error fetching headlines: ", e)
        #return None

def get_sources(params):
    try:
        print("the sources request is processing ")
        APIresponse = newsapi.get_sources(**params)  # Call the API with params
        print("the sources response is saved")
        print(APIresponse)# for testing
        return APIresponse 
    except Exception as e:
        print("Error fetching sources:", e)
        

def handle_client(sock, clientID):  
    print(30 * "-")
    print("New connection from", clientID[0], "is accepted", "with the port number:", clientID[1])
    print("Wait for the client to send a request")

    while True:
        try:

            dataFromClient= sock.recv(2084).decode()  # Receive data from client
            values = dataFromClient.split("|")
            print("This is the server values:", values)
            user_name,request, subRequest, dataRequested = values

            print("Requested service type is:", request)
            print("Requested sub is:", subRequest)
            print("Requested data is:", dataRequested)
            print("")

        except Exception as e:
            print("Error receiving data: ", e)
            break

        # If client chose to quit
        if request == "quit":        
            print("Client", clientID, "has quit the connection")
            sock.sendall("Goodbye!".encode('ascii'))
            break

        elif request == "headlines": 
            params = { "page_size": 15 }
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

            # Extracting the headlines from the api 
                results = get_headlines(params) # calling the function  
                if results:
                    dataFromApi =save_to_json(user_name, "headlines", "A4", results)  # save to JSON file (calling the method)
                    articles = dataFromApi.get('articles', [])
                    titles = []
                    print("")
                    print("the titles of all the articles:")
                    for article in articles:
                        title= article.get('title')
                        print(" title :",title)
                        titles.append({"title":title}) # Add the title to the titles list
                    print("")
                    titles_str =" "
                    for title in titles:
                        titles_str+= title["title"]+"\n"
                    #print("the titles of all the articles:"+"\n"+titles_str)
                else:
                    titles_str = "No results found."

            except Exception as e:
                print("Error handling headlines subrequests", e)

            try:
                # Sending the titles to the client to choose from 
                sock.sendall(titles_str.encode('utf-8'))
                print("titles are sent")
            except Exception as e :
                sock.sendall(b"error sending the titles")
                print("error sending the titles ", e)

            # receiving the title chosen from the client  
            chosen_title=sock.recv(2048).decode('utf-8')
            print("")
            print("the chosen title is received :", chosen_title)
            print("")
            print("now the detials about the title will be collected")
            print("")

            # extracting data based on the chosen title
            try:
                for article in articles:
                    #article_title=article.get('title')
                    #print("these are the article titles:",article_title)
                    #print(30 * "-")
                    if article.get('title') == chosen_title:
                        content=article.get('content','no content provided')
                        description=article.get('description','no description provided')
                        author=article.get('author','no author provided')
                        url=article.get('url','no url provided')
                        date=article.get('publishedAt', 'no time provided' )

                        article_details= (  "Title: " + chosen_title + "\n" +
                                            "Content: " + content + "\n" +
                                            "Description: " + description + "\n" +
                                            "Author: " + author + "\n" +
                                            "URL: " + url + "\n" +
                                            "Date: " + date + "\n" )
                        print("")
                        print(" article details:" ,article_details)
                        sock.sendall(article_details.encode('utf-8'))
                        print("")
                        print("the articles details are sent ")
                        break
                else:
                    print("the title chosen is not in the titles list")
                    sock.sendall(b"the title chosen is not in the titles list")
                    break
            except Exception as e:
                print("error at extracting headline data ", e)
                sock.sendall(b"server has an error with extracting the data ")

        elif request == "sources":
            params = {  }
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
                    print("invalid subrequest type")
                    sock.sendall("Invalid subRequest type.".encode('ascii'))
                    continue

                # Extracting the sources from the api  
                results = get_sources(params)
                if results:
                    dataFromApi =save_to_json(user_name, "sources", "A4", results)  # save to JSON file (calling the method)
                    sources = dataFromApi.get('sources', [])
                    names = []
                    print("")
                    print("the names of all the sources:")
                    count=0
                    for source in sources:
                        if count > 15: # to limit the names to 15 
                            break
                        name = source.get('name')
                        print("name:",name)
                        names.append({"name": name})
                        count=count+1
                    print("")
                    names_str = ""
                    for name in names:
                        names_str += name["name"] + "\n"
                    #print("the sources names are:"+"\n"+names_str)
                else:
                    names_str = "No results found"
            
            except Exception as e:
                print("Error processing sources request: ", e)

            try:
                # Sending the sources to the client to choose from 
                sock.sendall(names_str.encode('utf-8'))
                print("names of sources are sent")
            except Exception as e :
                sock.sendall(b"error sending the names of sources")
                print("error sending sources",e)

            # receiving the name chosen from the client
            chosen_name=sock.recv(2048).decode('utf-8')
            print("the chosen name of source is received :", chosen_name)

            # extracting data based on the chosen name 
            try:
                for source in sources:
                    if source.get('name')==chosen_name:
                        id=source.get('id', 'no id provided')
                        sdescription=source.get('description','no description provided')
                        surl=source.get('url','no url provided')
                        scategory=source.get('category','no category provided')
                        slanguage=source.get('language','no language provided')
                        scountry=source.get('country','no country provided')

                        source_details=("name of source: " + chosen_name + "\n" +
                                            "id: " + id + "\n" +
                                            "Description: " + sdescription + "\n" +
                                            "category: " + scategory + "\n" +
                                            "URL: " + surl + "\n" +
                                            "language: " + slanguage + "\n"
                                            "country: " + scountry + "\n" )
                        print(" source details:" ,source_details)
                        sock.sendall(source_details.encode('utf-8'))
                        print("-"*30)
                        print("the articles details are sent ")
                        break
                else:
                    print("the name of source chosen is not in the names list")
                    sock.sendall(b"the name of sourcee chosen is not in the names list")
                    break
            except Exception as e:
                print("error at extracting source data ")
                sock.sendall(b"server has an error with extracting the data ")

        
        # Close the socket after sending response
    sock.close()

def handle_server():
    print(30 * "-")
    print("The server is running")
    ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssocket.bind(("127.0.0.1", 49999))
    ssocket.listen(3)
    print("The server is now waiting for client")
    while True:
        sock, clientID = ssocket.accept()
        clientthread = threading.Thread(target=handle_client, args=(sock, clientID))
        clientthread.start()

# Start the server
handle_server()