import socket

clinet_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clinet_sock.connect(("127.0.0.1",49999))
print(" this is my client ")


n=True
while n==True:
    print("Main menu ")
    print("1 search for headings ")
    print("2 list all sourses ")
    print("3 Quit ")
    number=int(input(" fist enter the required servise number "))
    if number==1:
        print("Search headline menu")
        print("1 search for key words ")
        print("2 search for catogry ")
        print("3 search for country ")
        print("4 List all new headline ")
        print("5 back to the main menu ")
        number_2=int(input(" secound enter the required servise number "))
        if number_2==1:
           key_word=input(" key word to be searched with")
           msg=key_word
        if number_2==2:
            print('select the required catogry')
            print(" 1 business")
            print(" 2 genral")
            print(" 3 health")
            print(" 4 seince")
            print(" 5 sport")
            print(" 6 technology")
            catogry_num=int(input(" enter required catogry number"))
            match catogry_num:
                case 1:
                    msg="business_news"
                case 2:
                    msg="genral_news"
                case 3:
                    msg="health_news"
                case 4:
                    msg="seince_news"
                case 5:
                    msg="sport_news"
                case 6:
                    msg="technology_news"
                case _:
                    print("not vlaid catogry")
                    continue
            

        if number_2==3:
            print('select the required country')
            print(" 1 au")
            print(" 2 ca")
            print(" 3 jp")
            print(" 4 ae")
            print(" 5 sa")
            print(" 6 kr")
            print(" 7 us")
            print(" 6 ma")
            catogry_num=int(input(" enter required catogry number"))


            match catogry_num:
                case 1:
                   msg="au_news"
                case 2:
                    msg="ca_news"
                case 3:
                    msg="jp_news"
                case 4:
                    msg="ae_news"
                case 5:
                    msg="sa_news"
                case 6:
                    msg="kr_news"
                case 7:
                    msg="us_news"
                case 8:
                    msg="ma_news"
                case _:
                    print("not vlaid country")
                    continue
           
        if number_2==4:
           msg="all_news"
        if number_2==5:
            msg="quit"
            continue
        #clinet_sock.send(msg)
    if number==2:    
        print("List of sources menu")
        print("1 search by catogry ")
        print("2 search by country ")
        print("3 search by language ")
        print("4 List all ")
        print("5 back to the main menu  ")
        number_3=int(input("  thired enter the required servise number "))
        if number_3==1:
            print('select the required catogry')
            print(" 1 business")
            print(" 2 genral")
            print(" 3 health")
            print(" 4 seince")
            print(" 5 sport")
            print(" 6 technology")
            catogry_num=int(input(" enter required catogry number"))
            match catogry_num:
                case 1:
                    msg="business_sources"
                case 2:
                    msg="genral_sources"
                case 3:
                    msg="health_sources"
                case 4:
                    msg="seince_sources"
                case 5:
                    msg="sport_sources"
                case 6:
                    msg="technology_sources"
                case _:
                    print("not vlaid catogry")
                    continue
        if number_3==2:
            print('select the required country')
            print(" 1 au")
            print(" 2 ca")
            print(" 3 jp")
            print(" 4 ae")
            print(" 5 sa")
            print(" 6 kr")
            print(" 7 us")
            print(" 6 ma")
            catogry_num=int(input(" enter required catogry number"))


            match catogry_num:
                case 1:
                    msg="au_sources"
                case 2:
                    msg="ca_sources"
                case 3:
                    msg="jp_sources"
                case 4:
                    msg="ae_sources"
                case 5:
                    msg="sa_sources"
                case 6:
                    msg="kr_sources"
                case 7:
                    msg="us_sources"
                case 8:
                    msg="ma_sources"
                case _:
                    print("not vlaid country")
                    continue
           
        if number_3==3:
            print("choose the required language")
            print(" 1 arabic")
            print(" 2 engalish")
            country_num=int(input(" the choosen language number "))
            match country_num:
                case 1:
                    msg="ar"
                case 2 :
                    msg="en"
                case _:
                    print("not vlaid language")
                    continue
        if number_3==4:
           msg="all_language"
        if number_3==5:
           
           
            
            
            msg="quit"
            continue
        
        
    if number==3:
        msg="quit"
        n=False
    clinet_sock.send(msg.encode("ascii"))
 
data = clinet_sock.recv(1024)
 
print( "data recived",data.decode("ascii"))
clinet_sock.close()



