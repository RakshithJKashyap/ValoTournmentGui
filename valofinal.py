from tkinter import *
import random
from PIL import Image,ImageTk
from tkinter import messagebox



root=Tk()
root.geometry('917x517')
root.title('Valorant Tournment')
root.resizable(False,False)
#icon
icon= PhotoImage(file="G:/valo/icon1.png")
root.iconphoto(False,icon)
#bg
bg = PhotoImage(file = "G:/valo/bg.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
#clg logo
clg_logo = Image.open('G:/valo/clg.png')
photo1=ImageTk.PhotoImage(clg_logo)
logo_label =Label(image=photo1).place(x=10,y=10)
#event logo
event_logo = Image.open('G:/valo/event.png')
photo2=ImageTk.PhotoImage(event_logo)
logo_label =Label(image=photo2).place(x=330,y=6)

#title
title_label = Label(root,text="Valorant Tournament",relief="solid",font="arail 22 bold")
title_label.place(x=550,y=23)
#maps
maps_label = Label(root,text="Maps:",font="arial 15 bold").place(x=500,y=80)
ascent_label = Label(root,text="1.Ascent",font="arial 12 bold").place(x=550,y=120)
bind_label = Label(root,text="2.Bind",font="arial 12 bold").place(x=550,y=150)
breeze_label = Label(root,text="3.Breeze",font="arial 12 bold").place(x=550,y=180)
heaven_label = Label(root,text="4.Heaven",font="arial 12 bold").place(x=550,y=210)
icebox_label = Label(root,text="5.Icebox",font="arial 12 bold").place(x=550,y=240)

t1 = StringVar()
t2 = StringVar()

t1_label= Label(root,text="Team 1:",font="arial 16 bold").place(x=500,y=280)
entry_t1 = Entry(root,textvar=t1,width=20,font="arial 16",bd=3).place(x= 600,y=280)


t2_label= Label(root,text="Team 2:",font="arial 16 bold").place(x=500,y=320)
entry_t2 = Entry(root,textvar=t2,width=20,font="arial 16",bd=3).place(x= 600,y=320)

def decider():
    team1 = t1.get()
    team2 = t2.get()
    attack = "Attacking"
    defend = "Defending"
    options = [attack,defend]
    t1p = random.choice(options)
    maps = ['Breeze','Bind','Heaven','Icebox','Ascent'] 
    map_selected = (random.choice(maps))
    if t1p == attack :
        t2p = defend
        output1 = [team1," is ",attack,team2," is ",defend,"Map:",map_selected]
        #print(team1," is ",attack,"\n",team2," is ",defend,"\nMAP :",map_selected)
        messagebox.showinfo("FINAL", "\n".join(output1))
    elif t1p == defend:
        t2p = attack
        output2 = [team1," is ",defend,team2," is ",attack,"Map:",map_selected]
        #print(team1," is ",defend,"\n",team2," is ",attack,"\nMAP :",map_selected)
        messagebox.showinfo("FINAL", "\n".join(output2))
    
    

#button
choose_button= Button(root,text="GENERATE",font="arial 17 bold",padx = 1,command=decider,fg='white',bg='brown').place(x=590,y=385)

root.mainloop()



