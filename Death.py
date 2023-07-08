from tkinter import *


def returntomain():
    from TheWorld import endoftheworld
    global dsE
    dsE.destroy()
    endoftheworld()


def PLayerDied():
    global dsE
    dsE=Toplevel()
    dsE.geometry("1500x875")
    bgD=PhotoImage(file="images/Defeat Screen.png")
    bg=Label(dsE,image=bgD)
    bg.place(x=0,y=0)

    Dmm=PhotoImage(file="images/mian menu Defeat.png")

    mainmenuD=Button(dsE,image=Dmm,command=returntomain)
    mainmenuD.place(relx=0.44,y=590)
    dsE.mainloop()