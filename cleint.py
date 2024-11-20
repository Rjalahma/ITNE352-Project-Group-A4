import socket
 
n = 0
 
print(25 * "="+"\nThe client has started" )
 
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cs.connect(("127.0.0.1", 49999))


while n==True:
    print("Main menu ")
    print("1 search for headings ")
    print("2 list all sourses ")
    print("3 Quit ")
    number=int(input(" enter the required servise number "))
    if number==1:
        print("Search headline menu")
        print("1 search for key words ")
        print("2 search for catogry ")
        print("3 search for country ")
        print("4 List all new headline ")
        print("5 back to the main menu ")
        number_2=int(input(" enter the required servise number "))
        if number_2==5:
            continue
    if number==2:    
        print("List of sources menu")
        print("1 search by catogry ")
        print("2 search by country ")
        print("3 search by language ")
        print(" 4List all ")
        print("5 back to the main menu  ")
        number_3=int(input(" enter the required servise number "))
        if number_3==5:
            continue
    if number==3:
        n=False


    msg = input("Send: ")
 
    cs.sendto(msg.encode('ascii'),('127.0.0.1', 4012))
 
    data, address = cs.recv(2048)
 
    print('Received:', data.decode('ascii'))
 
    n += 1
 
cs.close()








#socket_c.send(b"Hello my friend,")
