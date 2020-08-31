from tkinter import *
from tkinter import messagebox,Toplevel
import pyqrcode
import os

######################### Main Functions #########################
def Generate_Qr():
    Qr_Name = Qr_Name_Entry_box.get()
    Qr_ID = Qr_ID_Entry_box.get()
    Qr_Message = Qr_Message_Entry_box.get()
    Message_Qr = 'Name: '+Qr_Name+'\n'+'Id: '+Qr_ID+'\n'+'Message: '+Qr_Message
    url = pyqrcode.create(Message_Qr)
    pp = r'F:\Hard-disk\Project\Works\QR Code Maker\Qr Codes'
    cc = '{}\{}{}.png'.format(pp,Qr_ID,Qr_Name)
    ll = os.listdir(pp)
    if('{}{}.png'.format(Qr_ID,Qr_Name)in ll):
        messagebox.showinfo('Notification','Please change your Id or Name')
    else:
        url.png(cc,scale=8)
        mm = 'Qr Code saved as: '+Qr_ID+Qr_Name+'.png'
        Qr_Notification_Message_Label.configure(text=mm)
        res = messagebox.askyesno('Notification','Your Qr Code is Generated. Do you want to see it?')
        if (res == True):
            top = Toplevel()
            top.geometry('400x400')
            top.configure(bg='white')
            img = PhotoImage(file=cc)
            label1 = Label(top,image=img,bg='white')
            label1.place(x=10,y=10)
            top.mainloop()

def Clear_ID_Name():
    Qr_ID_Entry_box.delete(0,'end')
    Qr_Message_Entry_box.delete(0,'end')
    Qr_Name_Entry_box.delete(0,'end')
    Qr_Notification_Message_Label.configure(text='')

def Quit_root():
    res = messagebox.askyesno('Notification','Are you sure that you want to quit?')
    if(res == True):
        root.destroy()
    else:
        pass

######################### Hover Effect Functions #########################
def Generate_Qrimage_ButtonEnter(e):
    Generate_Qrimage_Button['bg'] = 'purple2'
def Generate_Qrimage_ButtonLeave(e):
    Generate_Qrimage_Button['bg'] = 'powder blue'

def Clear_ID_Name_ButtonEnter(e):
    Clear_ID_Name_Button['bg'] = 'purple2'
def Clear_ID_Name_ButtonLeave(e):
    Clear_ID_Name_Button['bg'] = 'powder blue'

def Quit_root_ButtonEnter(e):
    Quit_root_Button['bg'] = 'purple2'
def Quit_root_ButtonLeave(e):
    Quit_root_Button['bg'] = 'powder blue'

######################### Root Method #########################
root = Tk()
root.geometry('570x400')
root.title('JAK QR Code Maker')
root.configure(bg='blue')
root.resizable(False,False)
root.iconbitmap('Icons8-Windows-8-Ecommerce-Qr-Code.ico')

######################### Label Method #########################
Qr_ID_Label = Label(master=root,text='Enter Your ID:',bg='Powder blue',fg='red',width=20,height=2,font=('times',12,'bold'))
Qr_ID_Label.place(x=10,y=20)

Qr_Name_Label = Label(master=root,text='Enter Your Name:',bg='Powder blue',fg='red',width=20,height=2,font=('times',12,'bold'))
Qr_Name_Label.place(x=10,y=80)

Qr_Message_Label = Label(master=root,text='Enter Your Message:',bg='Powder blue',fg='red',width=20,height=2,font=('times',12,'bold'))
Qr_Message_Label.place(x=10,y=140)

Qr_Notification_Label = Label(master=root,text='Notification: ',bg='Powder blue',fg='red',width=11,height=2,font=('times',12,'bold'))
Qr_Notification_Label.place(x=10,y=350)

Qr_Notification_Message_Label = Label(master=root,text='',bg='Powder blue',fg='red',width=30,height=2,font=('times',15,'bold'))
Qr_Notification_Message_Label.place(x=200,y=350)

######################### Entry Boxes #########################
Qr_ID_Entry_box = Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'bold'))
Qr_ID_Entry_box.place(x=250,y=20)

Qr_Name_Entry_box = Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'bold'))
Qr_Name_Entry_box.place(x=250,y=80)

Qr_Message_Entry_box = Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'bold'))
Qr_Message_Entry_box.place(x=250,y=140)

######################### Buttons #########################
Generate_Qrimage_Button = Button(master=root,text='Generate',width=15,font=('times',10,'bold'),bd=10,command=Generate_Qr,activebackground='purple',bg='powder blue')
Generate_Qrimage_Button.place(x=10,y=250)

Clear_ID_Name_Button = Button(master=root,text='Clear',width=15,font=('times',10,'bold'),bd=10,command=Clear_ID_Name,activebackground='purple',bg='powder blue')
Clear_ID_Name_Button.place(x=210,y=250)

Quit_root_Button = Button(master=root,text='Quit',width=15,font=('times',10,'bold'),bd=10,command=Quit_root,activebackground='purple',bg='powder blue')
Quit_root_Button.place(x=410,y=250)

######################### Hover Effects #########################
Generate_Qrimage_Button.bind('<Enter>',Generate_Qrimage_ButtonEnter)
Generate_Qrimage_Button.bind('<Leave>',Generate_Qrimage_ButtonLeave)

Clear_ID_Name_Button.bind('<Enter>',Clear_ID_Name_ButtonEnter)
Clear_ID_Name_Button.bind('<Leave>',Clear_ID_Name_ButtonLeave)

Quit_root_Button.bind('<Enter>',Quit_root_ButtonEnter)
Quit_root_Button.bind('<Leave>',Quit_root_ButtonLeave)

######################### loop #########################
root.mainloop()
######################### Done #########################
