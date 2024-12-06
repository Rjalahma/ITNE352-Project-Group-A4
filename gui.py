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
global userName_is_sent 
userName_is_sent=False
global userName
userName=""
request_counter=0
choice=""
global m
def clear():
      for widget in root.grid_slaves():
        widget.destroy()
def view_full_data(value):
    data=value
    clear()
    root.geometry("900x500")
    Label(root,text=str(data),font=("Times New Roman", 12),fg="dark green").grid(row=0, column=0,columnspan=5)
    Button(root, text="Back to Main Menu", command=main_menu,font=("Times New Roman", 14),fg="dark green").grid(row=1, column=0,columnspan=5)

def send_choice(value):
    global choice
    choice=value
    clear()
    root.geometry("300x105")
    full_data=send_gui_choice()
    print(" choice is sent ")
    print("$"*50)
    print(" the choice is ",choice)
    print("*"*77)
    print(" this is the full data ", full_data)
    my_lable1=Label(root,text=""*5).grid(row=0,column=0)
    Label(root,text="your choice is sent ",font=("Times New Roman", 16),fg="dark green").grid(row=1,column=0,columnspan=2)
    my_lable1=Label(root,text=""*5).grid(row=2,column=0)
    Button(root,text=" view full data", command=lambda:view_full_data(full_data) ,font=("Times New Roman", 14),fg="dark green").grid(row=3,column=1)
    Button(root, text="Back to Main Menu", command=main_menu,font=("Times New Roman", 14),fg="dark green").grid(row=3, column=0)

def view_data(value):
    w=value
    clear()
    if not w:
        Error_labale=Label(root,text=" error at reciving the titles ").grid(row=0, column=0)
        return main_menu()
    print(" choose from ",w)
    c=0
    m=StringVar()
    root.geometry("1000x1000")
    my_list=w.split("\n")
    n=len(my_list)
    print(" myyyy list",my_list)
    print("="*25)
    no_artical= False
    my_lable1=Label(root,text=""*5).grid(row=0,column=0)
    if n is None:
        clear()
        
    else:
        clear()
        for i in range(0,n):
            k=my_list[i]
            if k=="":
                continue 
            elif k=="[Removed]":
                continue
            if k=='No articles available':
                clear()
                no_artical=True
                erroe_labale=Label(root,text="No articles available",font=("Times New Roman", 16),fg="dark green").grid(row=0,column=0)
                Button(root, text="Back to Main Menu", command=main_menu,font=("Times New Roman", 14),fg="dark green").grid(row=c+3, column=0)
            elif k=="No sources available":
                clear()
                no_artical=True
                erroe_labale=Label(root,text="No articles available",font=("Times New Roman", 16),fg="dark green").grid(row=0,column=0)
                Button(root, text="Back to Main Menu", command=main_menu,font=("Times New Roman", 14),fg="dark green").grid(row=c+3, column=0)
            else:    
                Radiobutton(root,text=str(k),variable=m,value=str(k),font=("Times New Roman", 14),fg="dark green",anchor="w").grid(row=c,column=0)
                c=c+1
      
        if no_artical==False:
            Button(root,text=" send your choice ",command=lambda:send_choice(m.get().strip()),font=("Times New Roman", 14),fg="dark green",padx=50).grid(row=c+2,column=0)
            print("*"*25)
            my_lable1=Label(root,text=""*5).grid(row=c+1,column=0,columnspan=2)
            print(" the choice is ",m.get()) 
            Button(root, text="Back to Main Menu", command=main_menu,font=("Times New Roman", 14),fg="dark green" ,padx=50).grid(row=c+3, column=0)

def send(value):
    global button_clicked,msg,send_button
    print("vlaue,",value)
    msg=value
    clear()
    root.geometry("460x150")
    button_clicked = True
    send_button=True
    my_lable1=Label(root,text=""*5).grid(row=0,column=0,columnspan=2)
    myy_labale1=Label(root,text=" you choosed",font=("Times New Roman", 16),fg="dark green").grid(row=1,column=0,columnspan=2)
    myy_labale=Label(root,text=value,font=("Times New Roman", 16)) .grid(row=2,column=0,columnspan=2)
    my_lable1=Label(root,text=""*5).grid(row=3,column=0,columnspan=2)
    global request_counter
    m=send_request()
    print("-"*25)
    print(" this is m ",m)
    print(" request  is sent to server")
    Button(root,text=" view recived titles ",command=lambda:view_data(m),font=("Times New Roman", 14),fg="dark green",padx=20).grid(row=4,column=1)
    b5=Button(root,text="back to the main menu",command=main_menu,padx=30,font=("Times New Roman", 14),fg="dark green").grid(row=4,column=0)

def enter_input():
    global button_clicked,msg,request_type,sub_menue_choise,enter_button
    button_clicked = True
    enter_button=True
    my3=Label(root,text=box.get()).grid(row=5,column=0)
    request_type="headlines"
    sub_menue_choise="key-word"
    h=box.get()
    Button(root,text="send",command=lambda:send(h),padx=68,font=("Times New Roman", 14),fg="dark green").grid(row=6,column=0)
    b5=Button(root,text="back to the main menu",command=main_menu,padx=68,font=("Times New Roman", 14),fg="dark green").grid(row=7,column=0)
def search_for_key_words():
    clear()
    root.geometry("230x100")
    my_labal3=Label(root,text="Enter the key word",font=("Times New Roman", 16),fg="dark green").grid(row=0,column=0)
    global box
    box=Entry(root,width=35,borderwidth=5)
    box.grid(row=1,column=0)
    my_button2=Button(root,text="done",command=enter_input,font=("Times New Roman", 14),fg="dark green").grid(row=6,column=0)    
def search_for_catogry_headlines() :
    clear()
    global request_type,sub_menue_choise
    request_type="headlines"
    sub_menue_choise="by_category"
    m=StringVar(value="")
    root.geometry("390x270")
    my_lable1=Label(root,text=""*5).grid(row=0,column=0,columnspan=2)
    Radiobutton(root,text="business",variable=m,value="business_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=1,column=0)
    Radiobutton(root,text="general",variable=m,value="general_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=2,column=0)
    Radiobutton(root,text="health",variable=m,value="health_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=3,column=0)
    Radiobutton(root,text="science",variable=m,value="science_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=4,column=0)
    Radiobutton(root,text="sport",variable=m,value="sport_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=5,column=0)
    Radiobutton(root,text="technology",variable=m,value="technology_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=6,column=0)
    my_lable1=Label(root,text=""*5).grid(row=7,column=0,columnspan=2)
    print(" m",m.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    b1=Button(root,text="send",command=lambda:send(m.get()),padx=50,font=("Times New Roman", 14),fg="dark green").grid(row=8,column=1)
    Button(root,text="back to the main menu",command=main_menu,padx=30,font=("Times New Roman", 14),fg="dark green").grid(row=8,column=0)
def search_for_country_headlines() :
    clear()
    global request_type,sub_menue_choise
    request_type="headlines"
    sub_menue_choise="by_country"
    root.geometry("410x360")
    m=StringVar(value="")
    my_lable1=Label(root,text=""*5).grid(row=0,column=0,columnspan=2)
    Radiobutton(root,text="Australia",variable=m,value="au_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=1,column=0)
    Radiobutton(root,text="Canada",variable=m,value="ca_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=2,column=0)
    Radiobutton(root,text="Japan",variable=m,value="jp_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=3,column=0)
    Radiobutton(root,text="United Arab Emirates ",variable=m,value="ae_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=4,column=0)
    Radiobutton(root,text="Saudi Arabia",variable=m,value="sa_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=5,column=0)
    Radiobutton(root,text="South Korea",variable=m,value="kr_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=6,column=0)
    Radiobutton(root,text="United States of America",variable=m,value="us_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=7,column=0)
    Radiobutton(root,text="Morocco",variable=m,value="ma_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=8,column=0)
    my_lable1=Label(root,text=""*5).grid(row=9,column=0,columnspan=2)
    print(" m",m.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    b1=Button(root,text="send",command=lambda:send(m.get()),font=("Times New Roman", 14),fg="dark green",padx=50).grid(row=10,column=1)
    Button(root,text="back to the main menu",font=("Times New Roman", 14),fg="dark green",command=main_menu,padx=40).grid(row=10,column=0)
def List_all_headlines():
    clear()
    global request_type,sub_menue_choise,msg
    request_type="headlines"
    sub_menue_choise="list_all"
    root.geometry("330x105")
    my_lable1=Label(root,text=""*5).grid(row=0,column=0,columnspan=2)
    Label(root,text=" list all headlines ",font=("Times New Roman", 14),fg="dark green").grid(row=1,column=0,columnspan=2)
    my_lable1=Label(root,text=""*5).grid(row=2,column=0,columnspan=2)
    msg="all_news"
    print(" msg ",msg,"request",request_type,"sub_menue_choise",sub_menue_choise)
    b1=Button(root,text="send",command=lambda:send(msg),padx=50,font=("Times New Roman", 14),fg="dark green").grid(row=3,column=1)
    Button(root,text="back to the main menu",command=main_menu,padx=10,font=("Times New Roman", 14),fg="dark green").grid(row=3,column=0)
def heald_menu():
    clear()
    root.geometry("365x205")
    my_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green").grid(row=0,column=0,columnspan=2)
    my_lable2=Label(root,text="Search headline menu",font=("Times New Roman", 16),fg="dark green").grid(row=1,column=0,columnspan=2)
    my_lable3=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green").grid(row=2,column=0,columnspan=2)  
    b1=Button(root,text="search for key words",padx=8,font=("Times New Roman", 14),fg="dark green",command=search_for_key_words).grid(row=3,column=0)
    b2=Button(root,text="search for cateogry",font=("Times New Roman", 14),fg="dark green",padx=20,command=search_for_catogry_headlines).grid(row=4,column=0)
    b3=Button(root,text="search for country",font=("Times New Roman", 14),fg="dark green",padx=15,command=search_for_country_headlines).grid(row=4,column=1)
    b4=Button(root,text="List all new headline",font=("Times New Roman", 14),fg="dark green",padx=11,command=List_all_headlines).grid(row=3,column=1)
    b5=Button(root,text="back to the main menu",font=("Times New Roman", 14),fg="dark green",command=main_menu,padx=95).grid(row=5,column=0,columnspan=2)
def search_for_catogry_sourc() :
    clear()
    global request_type,sub_menue_choise
    request_type="sources"
    sub_menue_choise="by_category"
    m=StringVar(value="")
    root.geometry("380x290")
    my_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=0,column=0,columnspan=2)
    Radiobutton(root,text="business",variable=m,value="business_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=1,column=0)
    Radiobutton(root,text="general",variable=m,value="general_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=2,column=0)
    Radiobutton(root,text="health",variable=m,value="health_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=3,column=0)
    Radiobutton(root,text="science",variable=m,value="science_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=4,column=0)
    Radiobutton(root,text="sport",variable=m,value="sport_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=5,column=0)
    Radiobutton(root,text="technology",variable=m,value="technology_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=6,column=0)
    print(" m",m.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    my_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=7,column=0,columnspan=2)
    b1=Button(root,text="send",command=lambda:send(m.get()),padx=50,font=("Times New Roman", 14),fg="dark green").grid(row=8,column=1)
    Button(root,text="back to the main menu",command=main_menu,padx=30,font=("Times New Roman", 14),fg="dark green").grid(row=8,column=0)
def search_for_country_sourc() :
    clear()
    global request_type,sub_menue_choise
    request_type="sources"
    sub_menue_choise="by_country"
    m=StringVar(value="")
    root.geometry("380x355")
    my_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=0,column=0,columnspan=2)
    Radiobutton(root,text="Australia",variable=m,value="au_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=1,column=0)
    Radiobutton(root,text="Canada",variable=m,value="ca_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=2,column=0)
    Radiobutton(root,text="Japan",variable=m,value="jp_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=3,column=0)
    Radiobutton(root,text="United Arab Emirates",variable=m,value="ae_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=4,column=0)
    Radiobutton(root,text="Saudi Arabia",variable=m,value="sa_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=5,column=0)
    Radiobutton(root,text="South Korea",variable=m,value="kr_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=6,column=0)
    Radiobutton(root,text="United States of America",variable=m,value="us_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=7,column=0)
    Radiobutton(root,text="Morocco",variable=m,value="ma_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=8,column=0)
    my_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=9,column=0,columnspan=2)
    print(" m",m.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    b1=Button(root,text="send",command=lambda:send(m.get()),font=("Times New Roman", 14),fg="dark green",padx=50).grid(row=10,column=1)
    Button(root,text="back to the main menu",command=main_menu,font=("Times New Roman", 14),fg="dark green",padx=30).grid(row=10,column=0)
def search_by_language_sourc():
    clear()
    global request_type,sub_menue_choise
    request_type="sources"
    sub_menue_choise="by_language"
    root.geometry("235x160")
    k=StringVar(value="")
    my_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=0,column=0,columnspan=2)
    Radiobutton(root,text="arabic",variable=k,value="ar",font=("Times New Roman", 14),fg="dark green").grid(row=1,column=0)
    Radiobutton(root,text="engalish",variable=k,value="en",font=("Times New Roman", 14),fg="dark green").grid(row=2,column=0)
    print(" k",k.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    my_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=3,column=0,columnspan=2)
    b1=Button(root,text="send",font=("Times New Roman", 14),fg="dark green",command=lambda:send(k.get())).grid(row=4,column=1)
    Button(root,text="back to the main menu",font=("Times New Roman", 14),fg="dark green",command=main_menu).grid(row=4,column=0)
def List_all_sourc():
    clear()
    global request_type,sub_menue_choise
    request_type="sources"
    sub_menue_choise="list_all"
    root.geometry("230x130")
    my_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=0,column=0,columnspan=2)
    Label(root,text=" list all sources ",font=("Times New Roman", 16),fg="dark green").grid(row=1,column=0,columnspan=2)
    my_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=2,column=0,columnspan=2)
    msg="all_sources"
    b1=Button(root,text="send",font=("Times New Roman", 14),fg="dark green",command=lambda:send(msg)).grid(row=3,column=1)
    Button(root,text="back to the main menu",font=("Times New Roman", 14),fg="dark green",command=main_menu).grid(row=3,column=0)
def sourcemenue():
    clear()
    root.geometry("370x205")
    my_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=0,column=0,columnspan=2)
    my_lable2=Label(root,text="List of sources menu",font=("Times New Roman", 16),fg="dark green",).grid(row=1,column=0,columnspan=2)
    my_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=2,column=0,columnspan=2)
    b6=Button(root,text="search by cateogry",font=("Times New Roman", 14),fg="dark green",padx=19,command=search_for_catogry_sourc).grid(row=3,column=0)
    b7=Button(root,text="search by country",font=("Times New Roman", 14),fg="dark green",padx=19,command=search_for_country_sourc).grid(row=3,column=1)
    b8=Button(root,text="search by language",font=("Times New Roman", 14),fg="dark green",padx=16,command=search_by_language_sourc).grid(row=4,column=0)
    b9=Button(root,text="List all",font=("Times New Roman", 14),fg="dark green",padx=63,command=List_all_sourc).grid(row=4,column=1)
    b10=Button(root,text="back to the main menu",font=("Times New Roman", 14),fg="dark green",command=main_menu,padx=85).grid(row=5,column=0,columnspan=2)
def closing():
    global request_type,sub_menue_choise,msg,userName
    request_type="quit"
    sub_menue_choise="good"
    msg="bye"
    client.send_username_request(userName,request_type,sub_menue_choise,msg)
    client.client_close()
    root.quit()
def main_menu():
    global request_type,sub_menue_choise,msg,userName
    userName=get_username()
    clear()
    root.geometry("567x116")
    request_type=""
    sub_menue_choise=""
    msg=""
    my_lable2=Label(root,text=" Main menu ",font=("Times New Roman", 16),fg="dark green").grid(row=0,column=2,columnspan=3)
    my_lable=Label(root,text=("wellcome",userName),font=("Times New Roman", 14),fg="dark green").grid(row=1,column=2,columnspan=3)
    h=Button(root,command=heald_menu,text="search for headings",padx=35,pady=10,font=("Times New Roman", 14),fg="dark green").grid(row=2,column=2)
    source=Button(root,command=sourcemenue,text="list all sourses",padx=35,pady=10,font=("Times New Roman", 14),fg="dark green").grid(row=2,column=3)
    quit=Button(root,command=closing,text="quit",padx=55,pady=10,font=("Times New Roman", 14),fg="dark green").grid(row=2,column=4)

    

def enter_user_name():
    root.geometry("230x100")
    my_labal3=Label(root,text="Enter your user name ",font=("Times New Roman", 16),fg="dark green").grid(row=0,column=0)
    global userName_box
    userName_box=Entry(root,width=35,borderwidth=5)
    userName_box.grid(row=1,column=0)
    my_button2=Button(root,text="Done",command=main_menu,padx=30,font=("Times New Roman", 14),fg="dark green")
    my_button2.grid(row=6,column=0)
    return userName

def is_clicked():
    if enter_button or send_button :
        print(" enter_button",enter_button," send_button",send_button)
        print(" clivked vlaue  tru" )
        return True
        
    else:
        print(" clivked vlaue false" )
        return False
def get_username():
    global userName
    if userName=="":
        
        userName=userName_box.get()
        return userName
    else : return userName
def send_request():
    try:
        global  request_type, sub_menue_choise,msg,userName
        if request_type =="" or sub_menue_choise==""or msg=="" or userName=="":
            print (" one of vlaue request is empty" , " username is " , userName, " request type is ", request_type," sub choice is ", sub_menue_choise," massege is ",msg)
            return "no request sent"
        print ("  all vlaues are good " , " username is " , userName, " request type is ", request_type," sub choice is ", sub_menue_choise," massege is ",msg)
        client.send_username_request(userName,request_type,sub_menue_choise,msg)
        titels=client.recv()
        print ("  all vlaues are good " , " username is " , userName, " request type is ", request_type," sub choice is ", sub_menue_choise," massege is ",msg)
        print(" the client list  is " , titels)

        return titels
    except Exception as e:
        print(f"Error in send_request: {e}")
        return "Error", "No response"

def send_gui_choice() :
    global choice
    if choice=="":
        print(" choice is empty")
    else:
        client.send_choice(choice)
        full_data=client.recv()
        return full_data
def recv_full_data():
    try:
        data=client.recv()
        return data
    except Exception as e :
        print(" error at reciving full data")
enter_user_name()
root.mainloop()    