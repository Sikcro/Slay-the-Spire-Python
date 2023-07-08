from tkinter import *
from tkinter.tix import *
from openpyxl import workbook, load_workbook
from TheWorld import gamestart


def Ironclad():
    thecharactercell.value = "Ironclad"
    wcL.save('Excel files/Character Selection.xlsx')
    cs.destroy()
    gamestart()
    print("")

def Silent():
    thecharactercell.value = "Silent"
    wcL.save('Excel files/Character Selection.xlsx')
    cs.destroy()
    gamestart()
    print("")

def Defect():
    thecharactercell.value = "Defect"
    wcL.save('Excel files/Character Selection.xlsx')
    cs.destroy()
    gamestart()
    print("")


def selectionscreen():
    global wcL
    global thecharactercell
    global wcS
    global cs
    cs = Tk()
    cs.geometry("600x340")
    bg = PhotoImage(file="images/the character selection background.png")
    ic = PhotoImage(file="images/ironclad button.png")
    ts = PhotoImage(file="images/TheSilent button.png")
    df = PhotoImage(file="images/Defect button.png")

    bglabel = Label(cs,image=bg)
    bglabel.place(relx=0,y=0)

    ironcladbutton=Button(cs,image=ic,command=Ironclad)
    ironcladbutton.place(relx=0.13,y=280)
    tip = Balloon(cs)
    tip.bind_widget(ironcladbutton,balloonmsg="Ironclad",)

    thesilentbutton=Button(cs,image=ts,command=Silent)
    thesilentbutton.place(relx=0.45,y=280)
    tip2 = Balloon(cs)
    tip2.bind_widget(thesilentbutton,balloonmsg="The Silent")

    thedefectbutton=Button(cs,image=df,command=Defect)
    thedefectbutton.place(relx=0.8,y=276)
    tip3 = Balloon(cs)
    tip3.bind_widget(thedefectbutton,balloonmsg="The Defect")

    wcL = load_workbook("Excel files/Character Selection.xlsx")
    wcS = wcL.active
    thecharactercell = wcS['A1']
    thecharactercell.value = "normal"
    wcL.save('Excel files/Character Selection.xlsx')


    cs.mainloop()