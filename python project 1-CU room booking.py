#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pandas


# In[ ]:


pip install tkcalendar


# In[ ]:


pip install tk


# In[55]:


# working code
from tkinter import* 
from tkcalendar import*
from pandas import*
from PIL import*
import time
from tkinter import messagebox
import pandas as pd

rootW=Tk() # main window
rootW.geometry("1000x500") #setting dimension of output window
rootW.config(background="#b3d1ff")#backgroung colour inside the window
url = ' https://docs.google.com/spreadsheets/d/1odiIM5wtitwUgrZYjaB28p_Eu60aHR1G/edit?usp=sharing&ouid=117221464769801657516&rtpof=true&sd=true'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df =  pd.read_excel(path)




def crtW1():    #to create  a new output window that opens when go is clicked
    W1=Toplevel()  # contains the details of the selected room
    W1.geometry("600x600") #assigning measurements
    W1.config(background="#ffcccc")
    W1.title("Selected Room Contains ")#title
    label=Label(W1, text='The requested room has the following details',fg='#800000', font=("Times",22))#declaring a label with font color,style,size
    label.pack()
    if(choice.get()!='CHOOSE ROOM'):  #making sure an option is chosen
        show= df[df['ROOM ID']==choice.get()]
        Label(W1,text=show).pack()
    else:  #if menu option is not chosen
        W1.destroy()
        return
    
        
    def crtW3():
        W1.destroy()
        W3=Toplevel()
        W3.geometry("600x600") #assigning measurements
        W3.config(background="#fcf78d")
        W3.title("choose booking date")
        lab=Label(W3,text="When would you like to book the room?",font=("Times",15))
        lab.pack(pady=20)
        cal= Calendar(W3,selectmode="day",year=2022)   #declare calender as cal to choose date of booking
        cal.pack(pady=20)  #vertical spcae between cal and label
        def gdt(): #to get date from calender
            lab.config(text="Chosen "+cal.get_date())
            x = cal.get_date() # accepting date from W3
            def confirm():
                global i
                y = choice.get() #testing to check if right time slot is being accepted
                i =(df[df['Date'] == x].index[0]) #to find the index of the date column
                if(df.at[i,y]=='Booked'):
                    messagebox.showinfo(title="Error!", message="Booking already exists, please choose another date")
                else:
                    df.at[i,y]='Booked' #changing booking status to from free to booked
                    messagebox.showinfo(title="booking confirmation", message="Your booking has been confirmed")
                    time.sleep(2)
                    W3.destroy()
            Button(W3, text="Confirm", font=("times",14), command=confirm).pack(pady=20) 
        Button(W3,text="Select",font=("Times",15),command=gdt).pack(pady=10)#to select a date from calender for booking
        choice=StringVar()  #for choosing a slot to book
        choice.set("CHOOSE SLOT") 
        selectroom= OptionMenu(W3,choice,"Morning Slot","Afternoon Slot","Evening Slot")  #dropdown menu options
        selectroom.pack(pady=20)
    Button(W1,text="Book Room",font=("Arial",10),command=crtW3).place(x=500,y=200)

    
def crtW2():
    W2=Toplevel()  #contains the search result for availability
    button1=Button(W2, text="BACK", font=("times",14), command=W2.destroy)#get back to the main window.
    button1.place(x=0,y= 0)
    W2.geometry("1000x1000") 
    W2.title("The available rooms as per your criteria are : ")
    label=Label(W2, text='The requested room has the following details',fg='#800000', font=("Times",22))#declaring a label with font color,style,size
    label.pack()
    if(choice0.get()!='CHOOSE SLOT'and cal.get_date()!=None and choice1.get()!='CHOOSE CAPACITY'and choice2.get()!='CHOOSE EQUIPMENT'):
        show= df[df['Date']==cal.get_date()]
        if(show.empty): #if date is not found 
            Label(W2,text="sorry, we couldn't match the date, here are other available choises as per your specifications").pack()
            Label(W2,text="Matching the slot").pack(pady=20) 
            compare= ['ROOM ID','Date',choice0.get()] #outputfor match columns
            show1= df[compare]
            show1=show1.head()
            Label(W2,text=show1).pack()
            Label(W2,text="Matching the capacity").pack(pady=20)#output for match colums
            show2= df[df['Capacity ']==choice1.get()]
            show2=show2.head()
            compare=['ROOM ID','Date',choice0.get(),'Capacity '] 
            show2=show2[compare]
            Label(W2,text=show2).pack()
            Label(W2,text="Matching the equipment").pack(pady=20)#output for match columns
            show3= df[df['Equipment']==choice2.get()]
            show3=show3.head()
            compare=['ROOM ID','Date',choice0.get(),'Equipment']
            show3=show3[compare]
            Label(W2,text=show3).pack()
        else: #if date is found
            Label(W2,text=show).pack()
            Label(W2,text="we've tried to match as many requirements as possible, here are a few more results",fg='#800000', font=("Times",18)).pack(pady=20)
            compare=['ROOM ID','Date',choice0.get(),'Capacity ','Equipment']
            show=show[compare]
            Label(W2,text=show).pack(pady=10)
            
    else:
        W2.destroy()
        return
    
    
#########messages on mainw window#############

label=Label(rootW, text='WELCOME',fg='#800000', font=("Times",22))#declaring a label with font color,style,size
label.pack()
label=Label(rootW, text='Choose The Specifications Below',fg='black',font=("Arial",15)) #declaring a label with font color,style,size
label.pack(pady=20) #vertical space between two labels
##############################################


#########statement 1##########################
label=Label(rootW, text='View room details and book',fg='black',font=("Cambria",13)) #declaring a label with font color,style,size
label.pack(pady=10)  #vertical space between two labels
label.place(x=30,y=160)  #positioning label wrt. x and y axis.

choice=StringVar()  #capacity menu
choice.set("CHOOSE ROOM")  #menu options
roomid = df['ROOM ID'].to_list()#separate variable for roomid
Remove_duplicate= dict.fromkeys(roomid)
roomid= list(dict.fromkeys(Remove_duplicate))
selectroom= OptionMenu(rootW,choice,*roomid)#dropdown menu
selectroom.pack()
selectroom.place(x=60,y=200) #positioning wrt. x and y axis.
Button(rootW,text="GO",command= crtW1, font=('Arial',11)).place(x=110,y=444) #to get option of chosen room
#############################################

############statement 2######################

label=Label(rootW,text="Want To Check The Availablity Of A Room?", fg='black', font=('Cambria',13))  #label with font style,color and size
label.pack(pady=20)  #vertical space
label.place(x=580,y=140)  #positioning label
label=Label(rootW,text='Enter Your Requirements Below', fg='black', font=('Aria',13))   #label with font style,color and size
label.pack(pady=20)  #vertical space
label.place(x=620,y=170)  #positioning label


cal= Calendar(selectmode="day",year=2022)   #declare calender as cal
cal.pack(pady=10)  #vertical spcae between cal and label
cal.place(x=545,y=210)  #cal positioning
def gd(): #to get date from calender
    label.config(text="chosen:"+cal.get_date(),font=('Times',12))
    label.place(x=520,y=405)     #extracting date
Button(rootW,text="select",command=gd,font=('Times',14) ).place(x=645,y=440)#to select a date from calender


choice0=StringVar()  #default menu options
choice0.set('CHOOSE SLOT') 
selectroom0= OptionMenu(rootW,choice0,"Morning Slot","Afternoon Slot","Evening Slot")  #dropdown menu options
selectroom0.pack()
selectroom0.place(x=835,y=245)  #menu position

choice1=StringVar()  #default menu options for capacity
choice1.set('CHOOSE CAPACITY') 
capacity = df['Capacity '].to_list()
Remove_duplicate= dict.fromkeys(capacity)
capacity= list(dict.fromkeys(Remove_duplicate))
selectroom1= OptionMenu(rootW,choice1,*capacity)  #dropdown menu 

selectroom1.pack()
selectroom1.place(x=835,y=285)  #menu position

choice2=StringVar()   #default menu options for equipment
choice2.set('CHOOSE EQUIPMENT') 
Equipment = df['Equipment'].to_list()
Remove_duplicate= dict.fromkeys(Equipment)
Equipment= list(dict.fromkeys(Remove_duplicate))
selectroom2= OptionMenu(rootW,choice2,*Equipment) 
selectroom2.pack()
selectroom2.place(x=835,y=325)  #menu position
Button(rootW,text="Search",command=crtW2, font=('Times',14) ).place(x=885,y=440)
###################################

rootW.mainloop() 




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




