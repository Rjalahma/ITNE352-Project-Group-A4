import socket
import threading
import json
import time
import pprint
from newsapi import NewsApiClient

apikey = "75087d7737f64055bf57575247e9a59d"
newsapi = NewsApiClient(api_key=apikey)

# this function will take the requests parameters/data and save them into json file
def save_to_json(client_name, option, group_id, data):
    file_name=f"{client_name}{option}{group_id}.json"
    print("JSON file is created")
    with open (file_name,"w") as f :
        json.dump(data, f , indent=4)
    print("data saved to :", file_name+"\n")
    return data

# this functon will get the headlines from the API
def get_headlines(params):
    try:
        print("the headlines request is processing ")
        APIresponse = newsapi.get_top_headlines(**params)  # Call the API with params
        print("the headline response is saved\n")
        return APIresponse 
    
    except Exception as e:
        print("Error fetching headlines: ", e)
        
# this function will get the sources from the API
def get_sources(params):
    try:
        print("the sources request is processing ")
        APIresponse = newsapi.get_sources(**params)  # Call the API with params
        print("the sources response is saved\n")
        return APIresponse  
    
    except Exception as e:
        print("Error fetching sources:", e)
        
# this function allow handling each client request 
def handle_client(sock, clientID):  
    print(30 * "-")
    print("New connection from", clientID[0], "is accepted", "with the port number:", clientID[1])
    print("Wait for the client to send a request")
   

    while True:
        try:
            #receiving the name of the client + request type(headlines,sources)+ subrequest type(category,country etc..)+ datarequested(general,us etc..)
            dataFromClient = sock.recv(2084).decode()  # Receive data from client
            # beacuse all data recieved in one object now we will split them so we can work with them seperatly 
            values = dataFromClient.split("|")
            user_name,request, subRequest, dataRequested = values

            if request !="quit":
                print("\nnew request from ",user_name," is accepted !\n")
                print("Requested service type is:", request)
                print("Requested sub is:", subRequest)
                print("Requested data is:", dataRequested+"\n")

        except Exception :
            print("Error receiving data: ", e)
            break

        #If client choose to quit 
        if request == "quit":        
            print(user_name,"has quit the connection")
            print(subRequest+dataRequested,"!!!")
            break
        #If client choose headlines option 
        if request == "headlines": 
            params = { "page_size": 15 } # to limit the result of articles to 15 

            try:
                # Searching by a keyword 
                if subRequest == "key-word": 
                    params["q"] = dataRequested

                # Searching by category 
                elif subRequest == "by_category":
                    categories ={ "business_news": "business",
                        "general_news": "general",
                        "health_news": "health",
                        "science_news": "science",
                        "sport_news": "sports",
                        "technology_news": "technology" }
                    # extract the chosen catogery by the client from the dictionary and assign it to the parameter
                    category = categories.get(dataRequested)
                    if category: 
                        params["category"] = category 
                    else:
                        print("Invalid category entered by the user")
                        sock.sendall("Invalid headline category code entered by the client.".encode("ascii"))
                        continue

                # Searching by country 
                elif subRequest == "by_country": 
                    countries = {  
                        "au_news": "au", "ca_news": "ca", "jp_news": "jp", "ae_news": "ae",
                        "sa_news": "sa", "kr_news": "kr", "us_news": "us", "ma_news": "ma"}
                    # extract the chosen country by the client from the dictionary and assign it to the parameter
                    country = countries.get(dataRequested)
                    if country:
                        params["country"] = country
                    else:
                        print("Invalid country code entered by the user")
                        sock.sendall("Invalid headline country code entered by the client.".encode("ascii"))
                        continue

                # If client choose to list all headlines
                elif subRequest == "list_all":  
                    pass
                else:
                    sock.sendall("Invalid subRequest type.".encode("ascii"))
                    continue   

                # call the function that get the headlines from API 
                results = get_headlines(params) 
                if results :
                    # save the results to JSON file (calling the method) and save it 
                    dataFromApi =save_to_json(user_name, "-headlines", "-A4", results)  
                    
                    # extracting articles from the api data 
                    articles = dataFromApi.get("articles",[])

                    # extracting titles from the articles
                    data=[]
                    time.sleep(3)
                    print("the titles of all the articles:")
                    if articles:
                        num=1
                        # for loop to get all titles with there author and source name
                        for article in articles:
                            title= article.get("title","")
                            author=article.get("author","")
                            source=article.get("source")
                            if source:
                                sourcename=source.get("name", "Unknown Source name")
                            else:
                                sourcename="no Source available"
                            # save these vales with keys in a dic
                            item={ "title":title,"author":author,"source_name":sourcename}
                            # put each dic in a list as an item 
                            data.append(item)
                        pprint.pprint(data ,width=100)
                    else: # if there is no articles 
                        print("No articles available")
                        sock.sendall(b"No articles available")  
                        continue

                # if there is no API results
                else: 
                        print("no results from API found")
                        data = "No results found."    
 
            except Exception as e:
                print("Error handling headlines subrequests", e)

            try:
                # convert data to json then send it 
                json_string = json.dumps(data)
                sock.sendall(json_string.encode("utf-8"))
                print("\ntitles,authors,sources are sent sucssefully")

            except Exception as e :
                sock.sendall(b"error sending the titles,authors,sources")
                print("error sending the titles ", e)

            try:
                # receiving the title chosen from the client  
                print("\nwaiting to receive title chosen from the client ")
                chosen_title=sock.recv(2048).decode("utf-8")
                print("\nthe chosen title is received :", chosen_title)

            except Exception as e:
                print("\nerror receiving title chosen:",e)

            # extracting data based on the chosen title
                print("\nnow the details about the title will be collected")
            try:
                for article in articles:
                    if article.get("title") == chosen_title.strip(): #compare the titles then extract the article
                        description=str(article.get("description","no description provided"))
                        author=str(article.get("author","no author provided"))
                        url=str(article.get("url","no url provided"))
                        date=str(article.get("publishedAt", "no time provided" ))
                        sourcedic=(article.get("source"))
                        sourcename=str(sourcedic.get("name", "Unknown"))

                        article_details= (  "\n" +
                                            "Title: " + chosen_title + "\n" +
                                            "source name: " + sourcename + "\n" +
                                            "Description: " + description + "\n" +
                                            "Author: " + author + "\n" +
                                            "URL: " + url + "\n" +
                                            "Date: " + date + "\n" )
                        time.sleep(3)
                        print("\n article details:" ,article_details)
                        sock.sendall(article_details.encode("utf-8"))
                        print("\nthe articles details are sent ")
                        break
                else:
                    print("the title chosen is not in the titles list")
                    sock.sendall(b"the title chosen is not in the titles list")
                    break
                continue
            
            except Exception as e:
                print("error at extracting headline data ", e)
                sock.sendall(b"server has an error with extracting the data ")
        
        #If client choose sources option 
        elif request == "sources":
            params = { }
            try: 
                # Searching by category 
                if subRequest == "by_category":
                    categories = {
                        "business_sources": "business",
                        "general_sources": "general",
                        "health_sources": "health",
                        "science_sources": "science",
                        "sport_sources": "sports",
                        "technology_sources": "technology"}
                    # extract the chosen catogery by the client from the dictionary and assign it to the parameter
                    category = categories.get(dataRequested)
                    if category:
                        params["category"] = category
                    else:
                        print("Invalid source category entered by the user")
                        sock.sendall("Invalid source category code entered by the client.".encode("ascii"))
                        continue

                # Searching by country 
                elif subRequest == "by_country":
                    countries = {
                        "au_sources": "au", "ca_sources": "ca", "jp_sources": "jp", "ae_sources": "ae",
                        "sa_sources": "sa", "kr_sources": "kr", "us_sources": "us", "ma_sources": "ma"}
                    # extract the chosen country by the client from the dictionary and assign it to the parameter
                    country = countries.get(dataRequested)
                    if country:
                        params["country"] = country
                    else:
                        print("Invalid source country code entered by the user")
                        sock.sendall("Invalid source country code entered by the client.".encode("ascii"))
                        continue

                # Searching by language
                elif subRequest == "by_language":
                    languages = { "ar": "arabic", "en": "english" }
                    # extract the chosen language by the client from the dictionary and assign it to the parameter
                    language = languages.get(dataRequested)
                    if language:
                        params["language"] = dataRequested
                    else:
                        print("Invalid language code entered by the user")
                        sock.sendall("Invalid language code entered by the client.".encode("ascii"))
                        continue

                # If client chose to list all sources
                elif subRequest == "list_all":
                    pass
                else:
                    sock.sendall("Invalid subRequest type.".encode("ascii"))
                    continue

                # call the function that get the sources from API  
                results = get_sources(params)
                if results:
                    # save the results to JSON file (calling the method) and save it 
                    dataFromApi =save_to_json(user_name, "-sources", "-A4", results) 

                    # extracting sources from the api data
                    sources = dataFromApi.get("sources", [])

                    # extracting names from the sources
                    names = []
                    time.sleep(3)
                    print("the names of all the sources:")
                    if sources: 
                        count=1
                        for source in sources:
                            if count > 15: # to limit the names to 15 
                                break
                            name = source.get("name")
                            print("name",count,":",name)
                            names.append({"name": name})
                            count += 1
                        names_str = ""
                        for name in names:
                            names_str += name["name"] +"\n"
                    else:
                        print("No sources available")
                        sock.sendall(b"No sources available")  
                        continue

                # if there is no API results
                else: 
                    print("no results found")
                    names_str = "No results found"
            
            except Exception as e:
                print("Error processing sources request: ", e)

            try:
                # Sending the sources
                sock.sendall(names_str.encode("ascii"))
                print("\nnames are sent sucssefully")

            except Exception as e :
                sock.sendall(b"error sending the sources name")
                print("error sending sources",e)

            try:
                # receiving the name chosen from the client
                print("\nwaiting to receive name chosen from the client")
                chosen_name=sock.recv(2048).decode("utf-8")
                print("\nthe chosen name of source is received :", chosen_name)

            except Exception as e :
                print("\nerror receiving name chosen:",e)

            # extracting data based on the chosen name 
                print("\nnow the details about the title will be collected")
            try:
                for source in sources:
                    if source.get("name")==chosen_name:
                        id=str(source.get("id", "no id provided"))
                        sdescription=str(source.get("description","no description provided"))
                        surl=str(source.get("url","no url provided"))
                        scategory=str(source.get("category","no category provided"))
                        slanguage=str(source.get("language","no language provided"))
                        scountry=str(source.get("country","no country provided"))

                        source_details=(    "\n" +
                                            "name of source: " + chosen_name + "\n" +
                                            "id: " + id + "\n" +
                                            "Description: " + sdescription + "\n" +
                                            "category: " + scategory + "\n" +
                                            "URL: " + surl + "\n" +
                                            "language: " + slanguage + "\n"+
                                            "country: " + scountry + "\n" )
                        time.sleep(3)
                        print("\nsource details:" ,source_details)
                        sock.sendall(source_details.encode("utf-8"))
                        print("\nthe sources details are sent ")
                        break
                else:
                    print("the name of source chosen is not in the names list")
                    sock.sendall(b"the name of sourcee chosen is not in the names list")
                    break
                continue
            
            except Exception as e:
                print("error at extracting source data ")
                sock.sendall(b"server has an error with extracting the data ")


        sock.close()

#setting up the server 
def handle_server():
    print(30 * "-")
    print("The server is running")
    #creating the socket
    ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssocket.bind(("127.0.0.1", 49999))
    ssocket.listen(3)
    print("The server is now waiting for client")
    # to accept multiple clients at the same time 
    while True:
        sock, clientID = ssocket.accept()
        clientthread = threading.Thread(target=handle_client, args=(sock, clientID))
        clientthread.start()

# Start the server
handle_server()