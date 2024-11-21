import socket

clinet_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clinet_sock.connect(("127.2.0.1",49999))
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
           msg=b"banana"
        if number_2==3:
           msg=b"orange"
        if number_2==2:
            msg=b"apple"
        if number_2==4:
           msg=b"mango"
        if number_2==5:
            msg=b"quit"
            continue
        clinet_sock.send(msg)
    if number==2:    
        print("List of sources menu")
        print("1 search by catogry ")
        print("2 search by country ")
        print("3 search by language ")
        print("4 List all ")
        print("5 back to the main menu  ")
        number_3=int(input("  thired enter the required servise number "))
        if number_3==1:
           msg=b"tomato"
        if number_3==3:
           msg=b"cucambere"
        if number_3==2:
            msg=b"mashrom"
        if number_3==4:
           msg=b"water"
        if number_3==5:
            msg=b"quit"
            continue
        clinet_sock.send(msg)
    if number==3:
        msg=b"quit"
        n=False

 
data = clinet_sock.recv(1024)
 
print( "data recived",data.decode("ascii"))

clinet_sock.close()