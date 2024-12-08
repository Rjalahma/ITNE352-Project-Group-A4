from tkinter import *
import client as client

root=Tk()

# defining variables
root.title("menu")
request_type=""
sub_menue_choise=""
msg=""
global userName
userName=""
choice=""

#this function clears the gui from widget
def clear():
      for widget in root.grid_slaves():
        widget.destroy()

#The selected article details are passed as the value to this method. The GUI then displays it.
def view_full_data(value):
    data=value
    clear()
    root.geometry("1500x500")
    Label(root,text=str(data),font=("Times New Roman", 12),fg="dark green").grid(row=0, column=0,columnspan=5)
    Button(root, text="Back to Main Menu", command=main_menu,font=("Times New Roman", 14),fg="dark green").grid(row=1, column=0,columnspan=5)

# This method send the chosen title and recieves artical details and pass it to the view_full_data as it parameter
def send_choice(value):
    global choice
    choice=value
    clear()
    root.geometry("200x120")
    print(" choice is sent \n")
    print(" the choice is ",choice,"\n")
    #pass artical details to the view_full_data as it parameter
    full_data=send_gui_choice()
    print(" this is the full data :", full_data)
    # desgining the GUI page 
    empyt_lable1=Label(root,text=""*5).grid(row=0,column=0)
    Label(root,text="  your choice is sent ",font=("Times New Roman", 16),fg="dark green").grid(row=1,column=0,columnspan=2)
    empty_lable2=Label(root,text=""*5).grid(row=2,column=0)
    Button(root,text=" view full data", command=lambda:view_full_data(full_data) ,font=("Times New Roman", 14),fg="dark green").grid(row=3,column=1)

# take the title list as parameter then it creates a radio button for each (title,name) 
def creat_titles_radioButoones(value):
    titles=value
    clear()
    if not titles:
        Error_labale=Label(root,text=" error at reciving the titles ").grid(rotitles=0, column=0)
        return main_menu()
    print(" choose from ",titles)
    # counter to indicat the place the radio butoones will be attached in using grid 
    counter=0
    option_value=StringVar()
    if request_type=="headlines":  
        root.geometry("1500x1000")
    else:
        root.geometry("300x650")
    my_list=titles.split("\n")
    titles_length=len(my_list)
    print(" myyyy list",my_list)
    print("="*25)
    no_artical= False
    empty_lable1=Label(root,text=""*5).grid(row=0,column=0)
    if titles_length is None:
        clear()
        
    else:
        clear()
        for i in range(0,titles_length):
            title=my_list[i]
            # if title equal empty string it will ignore it 
            if title=="":
                continue 
            elif title=="[Removed]":
                continue
            # if no artical available from the server it will show a meesage to client and give it the options to go back to the main menu 
            if title=='No articles available':
                clear()
                no_artical=True
                erroe_labale=Label(root,text="No articles available",font=("Times New Roman", 16),fg="dark green").grid(row=0,column=0)
                Button(root, text="Back to Main Menu", command=main_menu,font=("Times New Roman", 14),fg="dark green").grid(row=counter+3, column=0)
             # if no sources available from the server it will show a meesage to client and give it the options to go back to the main menu 
            elif title=="No sources available":
                clear()
                no_artical=True
                erroe_labale=Label(root,text="No articles available",font=("Times New Roman", 16),fg="dark green").grid(row=0,column=0)
                Button(root, text="Back to Main Menu", command=main_menu,font=("Times New Roman", 14),fg="dark green").grid(row=counter+3, column=0)
            else:    
                Radiobutton(root,text=str(title),variable=option_value,value=str(title),font=("Times New Roman", 14),fg="dark green",anchor="w").grid(row=counter,column=0)
                counter=counter+1
        # if there is an artical it will allow the user to send it choice to server
        if no_artical==False:
            Button(root,text=" send your choice ",command=lambda:send_choice(option_value.get().strip()),font=("Times New Roman", 14),fg="dark green",padx=50).grid(row=counter+2,column=0,columnspan=2)
            print(" your choice is sent ")
            empty_lable2=Label(root,text=""*5).grid(row=counter+1,column=0,columnspan=2)
            print(" the choice is ",option_value.get()) 

# send the selected options by clint (request type: heldline or sources , sub choice , msg )
def send(value):
    # global button_clicked,msg,send_button
    global msg,send_button
    print("vlaue,",value)
    msg=value
    clear()
    root.geometry("223x150")
    send_button=True
    empty_lable1=Label(root,text=""*5).grid(row=0,column=0,columnspan=2)
    youChoosed=Label(root,text=" you chose",font=("Times New Roman", 16),fg="dark green").grid(row=1,column=0,columnspan=2)
    choosen_vlaue=Label(root,text=value,font=("Times New Roman", 16)) .grid(row=2,column=0,columnspan=2)
    empty_lable2=Label(root,text=""*5).grid(row=3,column=0,columnspan=2)

    # send the option value to the server
    option_value=send_request()
    print("")
    print(" this is option_value ",option_value)
    print(" request  is sent to server")
    print("")
    recivede_titles=Button(root,text=" view recived titles ",command=lambda:creat_titles_radioButoones(option_value),font=("Times New Roman", 14),fg="dark green",padx=20).grid(row=4,column=0,columnspan=2)

# take the entered vlaue and send it to the server
def enter_input():
    root.geometry("315x130")
    global msg,request_type,sub_menue_choise
    choosen_key_word=Label(root,text=box.get()).grid(row=5,column=0)
    request_type="headlines"
    sub_menue_choise="key-word"
    key_word=box.get()
    send_button=Button(root,text="send",command=lambda:send(key_word),padx=40,font=("Times New Roman", 14),fg="dark green").grid(row=6,column=1)
    back_to_main=Button(root,text="back to the main menu",command=main_menu,padx=20,font=("Times New Roman", 14),fg="dark green").grid(row=6,column=0)

# in this method user enter the key word they want   
def search_for_key_words():
    clear()
    root.geometry("230x100")
    my_labal3=Label(root,text="Enter the key word",font=("Times New Roman", 16),fg="dark green").grid(row=0,column=0)
    global box
    box=Entry(root,width=35,borderwidth=5)
    box.grid(row=1,column=0)
    done=Button(root,text="done",command=enter_input,font=("Times New Roman", 14),fg="dark green").grid(row=6,column=0)

# in this method user choose the catogrey user want from headlines catogrey then send the vlaue using send button     
def search_for_catogry_headlines() :
    clear()
    global request_type,sub_menue_choise
    request_type="headlines"
    sub_menue_choise="by_category"
    option_value=StringVar(value="")
    root.geometry("390x270")
    empty_lable1=Label(root,text=""*5).grid(row=0,column=0,columnspan=2)
    Radiobutton(root,text="business",variable=option_value,value="business_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=1,column=0)
    Radiobutton(root,text="general",variable=option_value,value="general_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=2,column=0)
    Radiobutton(root,text="health",variable=option_value,value="health_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=3,column=0)
    Radiobutton(root,text="science",variable=option_value,value="science_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=4,column=0)
    Radiobutton(root,text="sport",variable=option_value,value="sport_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=5,column=0)
    Radiobutton(root,text="technology",variable=option_value,value="technology_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=6,column=0)
    empty_lable2=Label(root,text=""*5).grid(row=7,column=0,columnspan=2)
    print(" option_value",option_value.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    send_button=Button(root,text="send",command=lambda:send(option_value.get()),padx=50,font=("Times New Roman", 14),fg="dark green").grid(row=8,column=1)
    back_to_main=Button(root,text="back to the main menu",command=main_menu,padx=30,font=("Times New Roman", 14),fg="dark green").grid(row=8,column=0)

# in this method user choose the country user want from headlines countries then send the vlaue using send button   
def search_for_country_headlines() :
    clear()
    global request_type,sub_menue_choise
    request_type="headlines"
    sub_menue_choise="by_country"
    root.geometry("410x360")
    option_value=StringVar(value="")
    empty_lable1=Label(root,text=""*5).grid(row=0,column=0,columnspan=2)
    Radiobutton(root,text="Australia",variable=option_value,value="au_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=1,column=0)
    Radiobutton(root,text="Canada",variable=option_value,value="ca_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=2,column=0)
    Radiobutton(root,text="Japan",variable=option_value,value="jp_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=3,column=0)
    Radiobutton(root,text="United Arab Emirates ",variable=option_value,value="ae_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=4,column=0)
    Radiobutton(root,text="Saudi Arabia",variable=option_value,value="sa_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=5,column=0)
    Radiobutton(root,text="South Korea",variable=option_value,value="kr_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=6,column=0)
    Radiobutton(root,text="United States of America",variable=option_value,value="us_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=7,column=0)
    Radiobutton(root,text="Morocco",variable=option_value,value="ma_news",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=8,column=0)
    empty_lable2=Label(root,text=""*5).grid(row=9,column=0,columnspan=2)
    print(" option_value",option_value.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    send_button=Button(root,text="send",command=lambda:send(option_value.get()),font=("Times New Roman", 14),fg="dark green",padx=50)
    send_button.grid(row=10,column=1)
    back_to_main=Button(root,text="back to the main menu",font=("Times New Roman", 14),fg="dark green",command=main_menu,padx=40).grid(row=10,column=0)

# this method let user choose the list all option for headlines
def List_all_headlines():
    clear()
    global request_type,sub_menue_choise,msg
    request_type="headlines"
    sub_menue_choise="list_all"
    root.geometry("330x105")
    empty_lable=Label(root,text=""*5).grid(row=0,column=0,columnspan=2)
    list_all_headlines=Label(root,text=" list all headlines ",font=("Times New Roman", 14),fg="dark green").grid(row=1,column=0,columnspan=2)
    empty_lable=Label(root,text=""*5).grid(row=2,column=0,columnspan=2)
    msg="all_news"
    print(" msg ",msg,"request",request_type,"sub_menue_choise",sub_menue_choise)
    send_button=Button(root,text="send",command=lambda:send(msg),padx=50,font=("Times New Roman", 14),fg="dark green").grid(row=3,column=1)
    Button(root,text="back to the main menu",command=main_menu,padx=10,font=("Times New Roman", 14),fg="dark green").grid(row=3,column=0)

#  the sub menu healdlines 
def heald_menu():
    clear()
    root.geometry("365x205")
    empty_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green").grid(row=0,column=0,columnspan=2)
    search_heaadlines=Label(root,text="Search headline menu",font=("Times New Roman", 16),fg="dark green").grid(row=1,column=0,columnspan=2)
    empty_lable2=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green").grid(row=2,column=0,columnspan=2)  
    key_word=Button(root,text="search for key words",padx=12,font=("Times New Roman", 14),fg="dark green",command=search_for_key_words).grid(row=3,column=0)
    catogrey=Button(root,text="search for cateogry",font=("Times New Roman", 14),fg="dark green",padx=18,command=search_for_catogry_headlines).grid(row=4,column=0)
    country=Button(root,text="search for country",font=("Times New Roman", 14),fg="dark green",padx=16,command=search_for_country_headlines).grid(row=4,column=1)
    list_all=Button(root,text="List all new headline",font=("Times New Roman", 14),fg="dark green",padx=11,command=List_all_headlines).grid(row=3,column=1)
    back_to_main=Button(root,text="back to the main menu",font=("Times New Roman", 14),fg="dark green",command=main_menu,padx=95).grid(row=5,column=0,columnspan=2)

#  the sources cateogry choices  , user choose on cateogry and it will be sent using send butoon 
def search_for_catogry_sourc() :
    clear()
    global request_type,sub_menue_choise
    request_type="sources"
    sub_menue_choise="by_category"
    option_value=StringVar(value="")
    root.geometry("380x290")
    empty_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=0,column=0,columnspan=2)
    Radiobutton(root,text="business",variable=option_value,value="business_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=1,column=0)
    Radiobutton(root,text="general",variable=option_value,value="general_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=2,column=0)
    Radiobutton(root,text="health",variable=option_value,value="health_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=3,column=0)
    Radiobutton(root,text="science",variable=option_value,value="science_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=4,column=0)
    Radiobutton(root,text="sport",variable=option_value,value="sport_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=5,column=0)
    Radiobutton(root,text="technology",variable=option_value,value="technology_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=6,column=0)
    print(" option_value",option_value.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    empty_lable2=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=7,column=0,columnspan=2)
    send_button=Button(root,text="send",command=lambda:send(option_value.get()),padx=50,font=("Times New Roman", 14),fg="dark green").grid(row=8,column=1)
    back_to_main=Button(root,text="back to the main menu",command=main_menu,padx=30,font=("Times New Roman", 14),fg="dark green").grid(row=8,column=0)

#  the sources country choices , user choose on counrty and it will be sent using send butoon 
def search_for_country_sourc() :
    clear()
    global request_type,sub_menue_choise
    request_type="sources"
    sub_menue_choise="by_country"
    option_value=StringVar(value="")
    root.geometry("380x355")
    empty_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=0,column=0,columnspan=2)
    Radiobutton(root,text="Australia",variable=option_value,value="au_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=1,column=0)
    Radiobutton(root,text="Canada",variable=option_value,value="ca_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=2,column=0)
    Radiobutton(root,text="Japan",variable=option_value,value="jp_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=3,column=0)
    Radiobutton(root,text="United Arab Emirates",variable=option_value,value="ae_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=4,column=0)
    Radiobutton(root,text="Saudi Arabia",variable=option_value,value="sa_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=5,column=0)
    Radiobutton(root,text="South Korea",variable=option_value,value="kr_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=6,column=0)
    Radiobutton(root,text="United States of America",variable=option_value,value="us_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=7,column=0)
    Radiobutton(root,text="Morocco",variable=option_value,value="ma_sources",font=("Times New Roman", 14),fg="dark green",anchor="w", width=20).grid(row=8,column=0)
    empty_lable2=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=9,column=0,columnspan=2)
    print(" option_value",option_value.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    send_button=Button(root,text="send",command=lambda:send(option_value.get()),font=("Times New Roman", 14),fg="dark green",padx=50).grid(row=10,column=1)
    back_to_main=Button(root,text="back to the main menu",command=main_menu,font=("Times New Roman", 14),fg="dark green",padx=30).grid(row=10,column=0)

# sources languages choices , user choose one language and it will be sent using send butoon 
def search_by_language_sourc():
    clear()
    global request_type,sub_menue_choise
    request_type="sources"
    sub_menue_choise="by_language"
    root.geometry("235x160")
    option_vlaue=StringVar(value="")
    empty_lable1=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=0,column=0,columnspan=2)
    Radiobutton(root,text="arabic",variable=option_vlaue,value="ar",font=("Times New Roman", 14),fg="dark green").grid(row=1,column=0)
    Radiobutton(root,text="engalish",variable=option_vlaue,value="en",font=("Times New Roman", 14),fg="dark green").grid(row=2,column=0)
    print(" option_vlaue",option_vlaue.get(),"request",request_type,"sub_menue_choise",sub_menue_choise)
    empty_lable2=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=3,column=0,columnspan=2)
    send_button=Button(root,text="send",font=("Times New Roman", 14),fg="dark green",command=lambda:send(option_vlaue.get())).grid(row=4,column=1)
    back_to_main=Button(root,text="back to the main menu",font=("Times New Roman", 14),fg="dark green",command=main_menu).grid(row=4,column=0)

# this is the list all sources  and it will be sent using send butoon 
def List_all_sourc():
    clear()
    global request_type,sub_menue_choise
    request_type="sources"
    sub_menue_choise="list_all"
    root.geometry("230x130")
    empty_lable=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=0,column=0,columnspan=2)
    Label(root,text=" list all sources ",font=("Times New Roman", 16),fg="dark green").grid(row=1,column=0,columnspan=2)
    empty_lable=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=2,column=0,columnspan=2)
    msg="all_sources"
    send_button=Button(root,text="send",font=("Times New Roman", 14),fg="dark green",command=lambda:send(msg)).grid(row=3,column=1)
    back_to_main=Button(root,text="back to the main menu",font=("Times New Roman", 14),fg="dark green",command=main_menu).grid(row=3,column=0)

# the sub menu "sources" user choose the wanted button than it take it to choose neded vlaue 
def sourcemenue():
    clear()
    root.geometry("370x205")
    empty_lable=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=0,column=0,columnspan=2)
    my_lable2=Label(root,text="List of sources menu",font=("Times New Roman", 16),fg="dark green",).grid(row=1,column=0,columnspan=2)
    empty_lable=Label(root,text=""*5,font=("Times New Roman", 16),fg="dark green",).grid(row=2,column=0,columnspan=2)
    categry=Button(root,text="search by cateogry",font=("Times New Roman", 14),fg="dark green",padx=19,command=search_for_catogry_sourc).grid(row=3,column=0)
    country=Button(root,text="search by country",font=("Times New Roman", 14),fg="dark green",padx=19,command=search_for_country_sourc).grid(row=3,column=1)
    language=Button(root,text="search by language",font=("Times New Roman", 14),fg="dark green",padx=17,command=search_by_language_sourc).grid(row=4,column=0)
    liast_all=Button(root,text="List all",font=("Times New Roman", 14),fg="dark green",padx=63,command=List_all_sourc).grid(row=4,column=1)
    back_to_main=Button(root,text="back to the main menu",font=("Times New Roman", 14),fg="dark green",command=main_menu,padx=85).grid(row=5,column=0,columnspan=2)

# this method closes the gui, client socket and send good bye to server 
def closing():
    global request_type,sub_menue_choise,msg,userName
    request_type="quit"
    sub_menue_choise="good"
    msg="bye"
    client.send_username_request(userName,request_type,sub_menue_choise,msg)
    client.client_close()
    root.quit()

# this the main menu 
def main_menu():
    global request_type,sub_menue_choise,msg,userName
    userName=get_username()
    clear()
    root.geometry("567x116")
    request_type=""
    sub_menue_choise=""
    msg=""
    main_menu=Label(root,text=" Main menu ",font=("Times New Roman", 16),fg="dark green").grid(row=0,column=2,columnspan=3)
    wellcome_message=Label(root,text=("wellcome",userName),font=("Times New Roman", 14),fg="dark green").grid(row=1,column=2,columnspan=3)
    haedlines=Button(root,command=heald_menu,text="search for headings",padx=35,pady=10,font=("Times New Roman", 14),fg="dark green").grid(row=2,column=2)
    source=Button(root,command=sourcemenue,text="list all sourses",padx=35,pady=10,font=("Times New Roman", 14),fg="dark green").grid(row=2,column=3)
    quit=Button(root,command=closing,text="quit",padx=55,pady=10,font=("Times New Roman", 14),fg="dark green").grid(row=2,column=4)

# this method allow user to enter user name once 
def enter_user_name():
    root.geometry("230x100")
    my_labal3=Label(root,text="Enter your user name ",font=("Times New Roman", 16),fg="dark green").grid(row=0,column=0)
    global userName_box
    userName_box=Entry(root,width=35,borderwidth=5)
    userName_box.grid(row=1,column=0)
    done=Button(root,text="Done",command=main_menu,padx=30,font=("Times New Roman", 14),fg="dark green")
    done.grid(row=6,column=0)
    # return userName

# if the user name variable is empty it will get username from user name box
def get_username():
    global userName
    if userName=="":
        
        userName=userName_box.get()
        return userName
    else : return userName

# this methode sends the requsted choices and recive the titles and return them back 
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
    
# this method sends the choosen title or name to server 
def send_gui_choice() :
    global choice
    if choice=="":
        print(" choice is empty")
    else:
        client.send_choice(choice)
        full_data=client.recv()
        return full_data
    
# call the enter user name to allow the user to enter its name 
enter_user_name()
# keep gui in  a loop
root.mainloop()    