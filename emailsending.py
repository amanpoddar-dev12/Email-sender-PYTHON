#from xml.etree.ElementInclude import include
#from cx_freeze import*
from asyncore import write
from email.mime import audio
from multiprocessing.util import is_exiting
from operator import sub
from secrets import choice
from tkinter import*
import smtplib
from tkinter import messagebox
from numpy import logical_or 
# from pygame import mixer             
# import speech_recognition
# import pyaudio
import smtplib
#this functionalty for exit button  
from email.message import EmailMessage
#includefiles=['','mic.png','email1.png','exit.png','send.png','attach.png','setting.png','attach.png','clear.png','music.wav','file.png']
import tkinter
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def sendingEmail(toaddress,subject,body):
    f=open('userinfo.txt','r')
    for i  in f: 
        userinfo=i.split(',')
    message=EmailMessage()
    message['subject']=subject
    message['to']=toaddress
    message['from']=userinfo[0]
    message.set_content(body)
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(userinfo[0],userinfo[1])
    s.send_message(message)
    messagebox.showinfo('infomormation','Email is sent succesfully')
def send_email():
    if toEntryFeild.get()=='' or subjectEntryFeild.get()=='' or textarea.get(1.0,END)=='\n':
       messagebox.showerror('Error','All feilds are required',parent=root) 
    else:
        if choice.get()=='single':  
            sendingEmail(toEntryFeild.get(),subjectEntryFeild.get(),textarea.get(1.0,END))
def settings():
    def clear1():
        fromEntryFeild.delete(0,END)
        passwordEntryFeild.delete(0,END)
    def save():
        if fromEntryFeild.get()=='' or passwordEntryFeild.get()=='':
            messagebox.showerror('Error','All details are required',parent=root1)
        else:
            f=open('userinfo.txt','w')
            f.write(fromEntryFeild.get()+','+passwordEntryFeild.get())
            f.close()
            messagebox.showinfo('Information','credentails  save succesfully',parent=root1)  
    
    root1=Toplevel()
    
    root1.title('Setting')
    
    root1.geometry('450x340+350+90')
    
    root1.config(bg='black')
    
    Label(root1,text="User setting",image=logoimage,compound=LEFT,font=('goudy old style',40,'bold'),
          fg="red",bg='grey20').grid(padx=60)
    
    
    
    
    fromlabelFrame=LabelFrame(root1,text='From Email Address',font=('times new roman',16,'bold'),bd=5,fg='white',bg='red')
    
    fromlabelFrame.grid(row=1,column='0',pady=20)
    
    fromEntryFeild=Entry(fromlabelFrame,font=('times new roman',18,'bold'),width=30) 
    
    fromEntryFeild.grid(row=0,column='0') 
    
    
    
    passwordlabelFrame=LabelFrame(root1,text='Password',font=('times new roman',16,'bold'),bd=5,fg='white',bg='red')
    
    
    
    passwordlabelFrame.grid(row=2,column='0',pady=20)
    
    passwordEntryFeild=Entry(passwordlabelFrame,font=('times new roman',18,'bold'),width=30,show="*") 
    
    passwordEntryFeild.grid(row=0,column='0') 
    
    Button(root1,text="SAVE",font=('times new roman',18,'bold')
                                   ,cursor='hand2',bg="green",fg='black',command=save).place(x=210,y=280)
    
    Button(root1,text="Clear",font=('times new roman',18,'bold')
                                   ,cursor='hand2',bg="green",fg='black',command=clear1).place(x=340,y=280)
    
    
    root1.mainloop() 
def iexit():
    result=messagebox.askyesno('notification','Do you want to  exit?')
    if  result:
        root.destroy()
    else:
        pass
#this functionality  for clear button for clear text from box
def clear():
    toEntryFeild.delete(0,END)
    
    subjectEntryFeild.delete(0,END)
    
    textarea.delete(1.0,END)
    
#this functionality  for speak button 
# def speak():
#    mixer.init() 
#    mixer.music.load('music.wav') 
#    mixer.music.play()  
#    sr=speech_recognition.Recognizer()
#    with speech_recognition.Microphone() as m:
#        try:
#            sr.adjust_for_ambient_noise(m,duration=0.2)
#            sr.listen(m)
#            audio=sr.listen(m)
#            text=sr.recognize_google(audio)
#            textarea.insert(END,text+'.')
#        except:
#            pass
#project by aman poddar
root=Tk()   #make an object
root.title("E-mail sender app by aman poddar") #i set title bar 
root.geometry('800x700')  #set length and weidth for app

root.resizable(0,0) #from this function user not able to  minimize or maximize this app.
root.config(bg="black") #here,i set bg color of application

titleFrame=Frame(root,bg='black')
titleFrame.grid(row=0,column=0)
logoimage=PhotoImage(file='email1.png')
titleLabel=Label(titleFrame,text='    Email Sender by Aman Poddar       ',image=logoimage,compound=LEFT,font=('Goudy old style',28,'bold'))
Button(titleFrame,text="setting",bd=0,bg='black',cursor='hand2').grid(row=0,column=1)   #here,i created setting button
titleLabel.grid(row=0,column=0) 
settingImage=PhotoImage(file='setting.png')     #this is for add setting icon 
Button(titleFrame,image=settingImage,bd=0,bg='black',cursor='hand2',activebackground="white",command=settings).grid(row=0,column=1)    #property of setting png                  
chooseFrame=Frame(root,bg='red')
chooseFrame.grid(row=1,column=0,pady=10)
#this is for add radio button for selecting sigle or multiple button
choice=StringVar()

"""singleRadioButton=Radiobutton(chooseFrame,text='Single',font=('times new roman',25,'bold'),variable=choice,value='single',bg='red',activebackground='red')
singleRadioButton.grid(row=0,column=0,padx=20)"""
"""multipleRadioButton=Radiobutton(chooseFrame,text='Multiple',font=('times new roman',25,'bold'),variable=choice,value='multiple',bg='red',activebackground='red')
multipleRadioButton.grid(row=0,column=2,padx=20)"""

choice.set('single') 
#this code for add browse  button 
tolabelFrame=LabelFrame(root,text='To (Email Address)',font=('times new roman',16,'bold'),bd=5,fg='white',bg='red')
tolabelFrame.grid(row=2,column='0',padx=100)

toEntryFeild=Entry(tolabelFrame,font=('times new roman',18,'bold'),width=30) 
toEntryFeild.grid(row=0,column='0') 

"""browseImage=PhotoImage(file='file.png')

Button(tolabelFrame,text='  Browse',image=browseImage,compound=LEFT,font=('arial',12,'bold'),cursor='hand2',bd=0,bg='skyblue',activebackground='red').grid(row=0,column=1,padx=20)          
#here,i add subject column"""
subjectLabelFrame=LabelFrame(root,text='Subject',font=('times new roman',16,'bold'),bd=5,fg='white',bg='red')
subjectLabelFrame.grid(row=3,column=0,pady=10)

subjectEntryFeild=Entry(subjectLabelFrame,font=('times new roman',16,'bold'),width=30)
subjectEntryFeild.grid(row=0,column='0') 


emaillabelFrame=LabelFrame(root,text='Compose E-mail ',font=('times new roman',16,'bold'),bd=10,fg='white',bg='red')
emaillabelFrame.grid(row=4,column=0,padx=20) 

"""micImage=PhotoImage(file='mic.png')
Button(emaillabelFrame,text='  Speak',image=micImage,compound=LEFT,font=('arial',12,'bold'),cursor='hand2',bd=0,bg='red',activebackground='red',command=speak).grid(row=0,column=0)          
"""
"""attachImage=PhotoImage(file='attach.png')    
Button(emaillabelFrame,text='  Attachment',image=attachImage,compound=LEFT,font=('arial',12,'bold'),cursor='hand2',bd=0,bg='red',activebackground='red').grid(row=0,column=1)          
"""
textarea=Text(emaillabelFrame,font=('times new roman',14,),height=7)
textarea.grid(row=1,column=0,columnspan=2)
 
sendImage=PhotoImage(file='mail.png')     #this is for add  icon 
Button(root,image=sendImage,bd=10,bg='black',cursor='hand2',activebackground="white",command=send_email).place(x=190,y=540)
#clear icon added here
clearImage=PhotoImage(file='clear.png')     #this is for add  icon 
Button(root,image=clearImage,bd=10,bg='black',cursor='hand2',activebackground="white",command=clear).place(x=390,y=560)
#refresh icon add here
exit=PhotoImage(file='exit.png')     #this is for add  icon 
Button(root,image=exit,bd=10,bg='black',cursor='hand2',activebackground="white",command=iexit).place(x=550,y=550)
#total mail sent label
"""totalLabel=Label(root,font=('times new roman',18,'bold'),bg='black',fg='black')
totalLabel.place(x=10,y=560)
#sent label
sentLabel=Label(root,font=('times new roman',18,'bold'),bg='black',fg='black')
sentLabel.place(x=100,y=560)
#left label
leftLabel=Label(root,font=('times new roman',18,'bold'),bg='black',fg='black')
leftLabel.place(x=190,y=560)
#failed label
failedLabel=Label(root,font=('times new roman',18,'bold'),bg='black',fg='black')
failedLabel.place(x=280,y=560)"""


root.mainloop() 
 

          
          