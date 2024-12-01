from tkinter import *
import najat_client as client
root=Tk()
root.title("menu")
button_clicked=False
request_type=""
sub_menue_choise=""
msg=""
send_button=False
enter_button=False
def clear():
      for widget in root.grid_slaves():
        widget.destroy()

def view_data(value):
    w=value
    clear()
    Label(root, text="Data Received:").grid(row=0, column=0)
    print(" choose from ",w)
    c=0
    m=StringVar()
    n=len(list)
    for i in range(0,n):
        k=list[i]
        Radiobutton(root,text=str(k),variable=m,value=str(k)).grid(row=c,column=0)
        c=c+1
    client.send(m.get())
    full_data=recv_full_data()
    Label(root,text=str(full_data), wraplength=300 ).grid(row=1,column=0)
    Button(root, text="Back to Main Menu", command=main_menu).grid(row=2, column=0)
def submit(value):
    b=value
    send_username(b)
    clear()
    welcom="welcom",str(value)
    Label(root,text=welcom).grid(row=0, column=0)
    Button(root, text=" Go to main menu", command=main_menu).grid(row=2, column=0)
def send(value):
    global button_clicked,msg,send_button
    print("vlaue,",value)
    msg=value
    clear()
    # root.after(100, handle_send)
    button_clicked = True
    send_button=True
    myy_labale1=Label(root,text=" you choosed ").grid(row=0,column=0,columnspan=2)
    myy_labale=Label(root,text=value)
    # msg=value
    myy_labale.grid(row=1,column=0,columnspan=2)
    if is_clicked():
        m=send_request()
        print(" request  is sent to server")
        # p,returned_data=return_data()
        # view_data(p)
        # print("this is p ",p)
        # print("this is returned_data",returned_data)
    
    Button(root,text=" The data ",command=lambda:view_data(m)).grid(row=3,column=0,columnspan=2)
    b5=Button(root,text="back to the main menu",command=main_menu,padx=68).grid(row=7,column=0,columnspan=2)

def enter_input():
    global button_clicked,msg,request_type,sub_menue_choise,enter_button
    button_clicked = True
    enter_button=True
    my3=Label(root,text=box.get()).grid(row=5,column=0)
    request_type="headlines"
    sub_menue_choise="key_word"
    h=box.get()
    Button(root,text="send",command=lambda:send(h)).grid(row=6,column=0)
    b5=Button(root,text="back to the main menu",command=main_menu,padx=68).grid(row=7,column=0,columnspan=2)
def search_for_key_words():
    clear()
    my_labal3=Label(root,text="Enter the key word").grid(row=0,column=0)
    global box
    box=Entry(root,width=35,borderwidth=5)
    box.grid(row=1,column=0)
    my_button2=Button(root,text="done",command=enter_input).grid(row=6,column=0)    
def search_for_catogry_headlines() :
    clear()
    global request_type,sub_menue_choise
    request_type="headlines"
    sub_menue_choise="by_catogry"
    m=StringVar()
    Radiobutton(root,text="business",variable=m,value="business_news").grid(row=0,column=0)
    Radiobutton(root,text="genral",variable=m,value="genral_news").grid(row=1,column=0)
    Radiobutton(root,text="health",variable=m,value="health_news").grid(row=2,column=0)
    Radiobutton(root,text="seince",variable=m,value="seince_news").grid(row=3,column=0)
    Radiobutton(root,text="sport",variable=m,value="sport_news").grid(row=4,column=0)
    Radiobutton(root,text="technology",variable=m,value="technology_news").grid(row=5,column=0)
    print(" m",m.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    b1=Button(root,text="send",command=lambda:send(m.get())).grid(row=6,column=0)
    Button(root,text="back to the main menu",command=main_menu).grid(row=7,column=0)
def search_for_country_headlines() :
    clear()
    global request_type,sub_menue_choise
    request_type="headlines"
    sub_menue_choise="by_country"
    m=StringVar()
    Radiobutton(root,text="au",variable=m,value="au_news").grid(row=0,column=0)
    Radiobutton(root,text="ca",variable=m,value="ca_news").grid(row=1,column=0)
    Radiobutton(root,text="jp",variable=m,value="jp_news").grid(row=2,column=0)
    Radiobutton(root,text="ae",variable=m,value="ae_news").grid(row=3,column=0)
    Radiobutton(root,text="sa",variable=m,value="sa_news").grid(row=4,column=0)
    Radiobutton(root,text="kr",variable=m,value="kr_news").grid(row=5,column=0)
    Radiobutton(root,text="us",variable=m,value="us_news").grid(row=6,column=0)
    Radiobutton(root,text="ma",variable=m,value="ma_news").grid(row=7,column=0)
    print(" m",m.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    b1=Button(root,text="send",command=lambda:send(m.get())).grid(row=8,column=0)
    Button(root,text="back to the main menu",command=main_menu,padx=50).grid(row=9,column=0)
def List_all_headlines():
    clear()
    global request_type,sub_menue_choise,msg
    request_type="headlines"
    sub_menue_choise="list_all"
    Label(root,text=" list all headlines ").grid(row=0,column=0)
    msg="all_news"
    print(" msg ",msg,"request",request_type,"sub_menue_choise",sub_menue_choise)
    b1=Button(root,text="send",command=lambda:send(msg)).grid(row=1,column=0)
    Button(root,text="back to the main menu",command=main_menu,padx=50).grid(row=2,column=0)
def heald_menu():
    clear()
    # request_type="headlines"
    my_lable=Label(root,text="welecom").grid(row=0,column=0,columnspan=2)
    my_lable2=Label(root,text="choose from the ... ").grid(row=1,column=0,columnspan=2)  
    b1=Button(root,text="search for key words",padx=7,command=search_for_key_words).grid(row=3,column=0)
    b2=Button(root,text="search for catogry",padx=14,command=search_for_catogry_headlines).grid(row=2,column=0)
    b3=Button(root,text="search for country",padx=15,command=search_for_country_headlines).grid(row=2,column=1)
    b4=Button(root,text="List all new headline",padx=11,command=List_all_headlines).grid(row=3,column=1)
    b5=Button(root,text="back to the main menu",command=main_menu,padx=68).grid(row=4,column=0,columnspan=2)
def search_for_catogry_sourc() :
    clear()
    global request_type,sub_menue_choise
    request_type="sources"
    sub_menue_choise="by_catogry"
    m=StringVar()
    Radiobutton(root,text="business",variable=m,value="business_sources").grid(row=0,column=0)
    Radiobutton(root,text="genral",variable=m,value="genral_sources").grid(row=1,column=0)
    Radiobutton(root,text="health",variable=m,value="health_sources").grid(row=2,column=0)
    Radiobutton(root,text="seince",variable=m,value="seince_sources").grid(row=3,column=0)
    Radiobutton(root,text="sport",variable=m,value="sport_sources").grid(row=4,column=0)
    Radiobutton(root,text="technology",variable=m,value="technology_sources").grid(row=5,column=0)
    print(" m",m.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    b1=Button(root,text="send",command=lambda:send(m.get())).grid(row=6,column=0)
    Button(root,text="back to the main menu",command=main_menu).grid(row=7,column=0)
def search_for_country_sourc() :
    clear()
    global request_type,sub_menue_choise
    request_type="sources"
    sub_menue_choise="by_language"
    m=StringVar()
    Radiobutton(root,text="au",variable=m,value="au_sources").grid(row=0,column=0)
    Radiobutton(root,text="ca",variable=m,value="ca_sources").grid(row=1,column=0)
    Radiobutton(root,text="jp",variable=m,value="jp_sources").grid(row=2,column=0)
    Radiobutton(root,text="ae",variable=m,value="ae_sources").grid(row=3,column=0)
    Radiobutton(root,text="sa",variable=m,value="sa_sources").grid(row=4,column=0)
    Radiobutton(root,text="kr",variable=m,value="kr_sources").grid(row=5,column=0)
    Radiobutton(root,text="us",variable=m,value="us_sources").grid(row=6,column=0)
    Radiobutton(root,text="ma",variable=m,value="ma_sources").grid(row=7,column=0)
    print(" m",m.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    b1=Button(root,text="send",command=lambda:send(m.get())).grid(row=8,column=0)
    Button(root,text="back to the main menu",command=main_menu,padx=50).grid(row=9,column=0)
def search_by_language_sourc():
    clear()
    global request_type,sub_menue_choise
    request_type="sources"
    sub_menue_choise="by_language"
    m=StringVar()
    Radiobutton(root,text="arabic",variable=m,value="ar").grid(row=0,column=0)
    Radiobutton(root,text="engalish",variable=m,value="en").grid(row=1,column=0)
    print(" m",m.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    b1=Button(root,text="send",command=lambda:send(m.get())).grid(row=2,column=0)
    Button(root,text="back to the main menu",command=main_menu,padx=50).grid(row=3,column=0)
def List_all_sourc():
    clear()
    global request_type,sub_menue_choise
    request_type="sources"
    sub_menue_choise="list_all"
    Label(root,text=" list all sources ").grid(row=0,column=0)
    msg="all_sources"
    b1=Button(root,text="send",command=lambda:send(msg)).grid(row=1,column=0)
    Button(root,text="back to the main menu",command=main_menu,padx=50).grid(row=2,column=0)
def sourcemenue():
    clear()
    my_lable=Label(root,text="welecom").grid(row=0,column=0,columnspan=2)
    my_lable2=Label(root,text="choose from the ... ").grid(row=1,column=0,columnspan=2)
    b6=Button(root,text="search by catogry",padx=7,command=search_for_catogry_sourc).grid(row=2,column=0)
    b7=Button(root,text="search by country",padx=7,command=search_for_country_sourc).grid(row=2,column=1)
    b8=Button(root,text="search by language",command=search_by_language_sourc).grid(row=3,column=0)
    b9=Button(root,text="List all",padx=38,command=List_all_sourc).grid(row=3,column=1)
    b10=Button(root,text="back to the main menu",command=main_menu,padx=50).grid(row=4,column=0,columnspan=2)
def closing():
    global request_type
    request_type="quit"
    client.client_close()
    root.quit()
def main_menu():
    clear()
    global request_type,sub_menue_choise,msg
    root.title("main menu")
    request_type=""
    sub_menue_choise=""
    msg=""
    my_lable=Label(root,text="welecom").grid(row=0,column=1)
    my_lable2=Label(root,text="choose from the ... ").grid(row=1,column=1)
    h=Button(root,command=heald_menu,text="search for headings",padx=35,pady=10).grid(row=2,column=0)
    source=Button(root,command=sourcemenue,text="list all sourses",padx=35,pady=10).grid(row=2,column=1)
    quit=Button(root,command=closing,text="quit",padx=35,pady=10).grid(row=2,column=2)
def enter_input_username():
    # global button_clicked,msg,request_type,sub_menue_choise,enter_button
    # button_clicked = True
    # enter_button=True
    h=userName_box.get()
    clear()
    my3=Label(root,text=(" your user name is ",h))
    my3.grid(row=0,column=0)
    print(" the useer name is ", h )
    # client.send(h)
    print("user name is send")
    b5=Button(root,text=" go to the main menu",command=main_menu,padx=68)
    b5.grid(row=1,column=0,columnspan=2)
    Button(root,text="submit",command=lambda:submit(h)).grid(row=2,column=0,columnspan=2)

    

def enter_user_name():
    my_labal3=Label(root,text="Enter your user name ").grid(row=0,column=0)
    global userName_box
    userName_box=Entry(root,width=35,borderwidth=5)
    userName_box.grid(row=1,column=0)
    my_button2=Button(root,text="done",command=enter_input_username)
    my_button2.grid(row=6,column=0)

def is_clicked():
    if enter_button or send_button :
        print(" enter_button",enter_button," send_button",send_button)
        print(" clivked vlaue  tru" )
        return True
        
    else:
        print(" clivked vlaue fals" )
        return False

# def return_data():
#     # print(" inside return")
#     # message = "|".join([request_type,sub_menue_choise,msg]) 
#     # return client.send(message) , client.recv()
#     # #  return 
#     print("Inside return")
#     try:
#         # Send the message and receive the response
#         message = "|".join([request_type, sub_menue_choise, msg])
#         client.send(message.encode('ascii'))  # Ensure proper encoding
#         data = client.recv(1024).decode('ascii')  # Receive the response
#         return data
#     except Exception as e:
#         print(f"Error in return_data: {e}")
#         return "Error", "No response"

# main_menu()
def send_request():
    try:
        message = "|".join([request_type,sub_menue_choise,msg]) 
        client.send(message) 
        b=client.recv()
        print(" the client list  is " , b)

        return b
    except Exception as e:
        print(f"Error in send_request: {e}")
        main_menu()
        return "Error", "No response"

def send_username(vlaue):
    try:
        client.send(vlaue)
    except Exception as e :
        print(" error at sending user name ")
def recv_full_data():
    try:
        data=client.recv(1024).decode("ascii")
        return data
    except Exception as e :
        print(" error at reciving full data")
def recv_choices(list):
    c=0
    m=StringVar()
    n=len(list)
    for i in range(0,n):
        k=list[i]
        Radiobutton(root,text=str(k),variable=m,value=str(k)).grid(row=c,column=0)
        c=c+1
    client.send(m.get())
enter_user_name()
root.mainloop()    
   
        

# Call start_gui() from the client file.



