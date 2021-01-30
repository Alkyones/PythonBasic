from tkinter import * 
from time import sleep
  
  
top = Tk()
top.title('Password Remainder') 
top.configure(background='grey')
top.geometry("250x60")
top.counter= 0 
 
def nwc():
    top = Toplevel()
    top.geometry('300x100')
    top.title("Save Pass")
    
   
   
    user_site = Label(top,  
                  text = "Site")
    user_site.grid(column=0,row=0) 
    
    user_username = Label(top,  
                      text = "Username")
    user_username.grid(column=0,row=1)
    user_password = Label(top,  
                      text = "Password")
    user_password.grid(column=0,row=2)
    user_site_input_area = Entry(top, 
                             width = 30)
    user_site_input_area.grid(column=1,row=0)
    user_username_entry_area = Entry(top, 
                                 width = 30)   
    user_username_entry_area.grid(column=1,row=1)
    user_password_entry_area = Entry(top, 
                                 width = 30)
    user_password_entry_area.grid(column=1,row=2)
    
    def saveInformation():
        with open('test.txt','a+') as test :
            test.write(user_site_input_area.get()+'  |  ')
            test.write(user_username_entry_area.get()+'  |  ')
            test.write(user_password_entry_area.get()+'  |')
            test.write('\n')
        top.destroy()

    userButton=Button(top,text='Save',command=saveInformation)
    userButton.grid(column=0,row=5)
    

        
    

    



    #Buttons

def switch():
    top = Toplevel()
    top.geometry('500x900')
    top.title("Show Passwords")
    with open('test.txt','r') as txt :
        text_box = Text(top,background='grey',font='arial',width=500,height=900)
        text_box.insert(END,txt.read())
        text_box.pack()

    
    
    
frame1=Frame(top)
frame1.pack(side='top')


show_button = Button(top,text = "Show The Passwords",command=switch).pack(in_=frame1,side='left')
save_button = Button(top,text = "Save A New Password",command=nwc).pack(in_=frame1,side='right')

    
top.mainloop()  