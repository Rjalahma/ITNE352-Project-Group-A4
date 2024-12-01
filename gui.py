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
    clear()
    Label(root, text="Data Received:").grid(row=0, column=0)
    Label(root,text=str(value), wraplength=300, justify="left").grid(row=0,column=0)
    Button(root, text="Back to Main Menu", command=main_menu).grid(row=2, column=0)
def send(value):
    global button_clicked,msg,send_button
    print("vlaue,",value)
    clear()
    button_clicked = True
    send_button=True
    myy_labale1=Label(root,text=" you choosed ").grid(row=0,column=0,columnspan=2)
    myy_labale=Label(root,text=value)
    msg=value
    myy_labale.grid(row=1,column=0,columnspan=2)
    if is_clicked():

        p=return_data()
        view_data(p)
        print("this is x",p)
    Button(root,text=" The data ",command=view_data).grid(row=3,column=0,columnspan=2)

def enter_input():
    global button_clicked,msg,request_type,sub_menue_choise,enter_button
    button_clicked = True
    enter_button=True
    my3=Label(root,text=box.get()).grid(row=5,column=0)
    request_type="headlines"
    sub_menue_choise="key_word"
    h=box.get()
    Button(root,text="send",command=lambda:send(h)).grid(row=6,column=0)
def search_for_key_words():
    clear()
    my_labal3=Label(root,text="Enter the key word").grid(row=0,column=0)
    global box
    box=Entry(root,width=35,borderwidth=5)
    box.grid(row=1,column=0)
    my_button2=Button(root,text="done",command=enter_input).grid(row=6,column=0)    
def search_for_catogry() :
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

def heald_menu():
    clear()
    my_lable=Label(root,text="welecom").grid(row=0,column=0,columnspan=2)
    my_lable2=Label(root,text="choose from the ... ").grid(row=1,column=0,columnspan=2)  
    b1=Button(root,text="search for key words",padx=7,command=search_for_key_words).grid(row=3,column=0)
    b2=Button(root,text="search for catogry",padx=14,command=search_for_catogry).grid(row=2,column=0)
    b3=Button(root,text="search for country",padx=15).grid(row=2,column=1)
    b4=Button(root,text="List all new headline",padx=11).grid(row=3,column=1)
    b5=Button(root,text="back to the main menu",command=main_menu,padx=68).grid(row=4,column=0,columnspan=2)
def sourcemenue():
    clear()
    my_lable=Label(root,text="welecom").grid(row=0,column=0,columnspan=2)
    my_lable2=Label(root,text="choose from the ... ").grid(row=1,column=0,columnspan=2)
    b6=Button(root,text="search by catogry",padx=7).grid(row=2,column=0)
    b7=Button(root,text="search by country",padx=7).grid(row=2,column=1)
    b8=Button(root,text="search by language").grid(row=3,column=0)
    b9=Button(root,text="List all",padx=38).grid(row=3,column=1)
    b10=Button(root,text="back to the main menu",command=main_menu,padx=50).grid(row=4,column=0,columnspan=2)
def closing():
    global request_type
    request_type="quit"
    root.quit()
def main_menu():
    clear()
    root.title("main menu")
    my_lable=Label(root,text="welecom").grid(row=0,column=1)
    my_lable2=Label(root,text="choose from the ... ").grid(row=1,column=1)
    h=Button(root,command=heald_menu,text="search for headings",padx=35,pady=10).grid(row=2,column=0)
    source=Button(root,command=sourcemenue,text="list all sourses",padx=35,pady=10).grid(row=2,column=1)
    quit=Button(root,command=closing,text="quit",padx=35,pady=10).grid(row=2,column=2)


def is_clicked():
    if enter_button or send_button :
        print(" enter_button",enter_button," send_button",send_button)
        print(" clivked vlaue  tru" )
        return True
        
    else:
        print(" clivked vlaue fals" )
        return False

def return_data():
    print(" inside return")
    message = "|".join([request_type,sub_menue_choise,msg]) 
    return client.send(message)
    #  return 
    

main_menu()
root.mainloop()    
   
        

# Call start_gui() from the client file.



