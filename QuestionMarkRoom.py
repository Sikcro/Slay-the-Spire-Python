from tkinter import *
import random
from openpyxl import workbook, load_workbook

def Wcurse():
    global psL
    global pbL
    global qsr
    global NQlabel
    from TheWorld import THEboard
    NQlabel.place_forget()
    spinscreenwheel = PhotoImage(file="images/the wheel curse.png")
    Qlabel = Label(qsr, image=spinscreenwheel, anchor="center")
    Qlabel.place(relx=0, y=0)
    psL['B4'].value = "True"
    pbL.save('Excel files/Player Data.xlsx')
    qsr.after(140,THEboard)
    qsr.after(500,qsr.destroy)
    qsr.mainloop()


def Wchest():
    global psL
    global pbL
    global qsr
    global NQlabel
    from Chest_Battle import chestbattlestart
    NQlabel.place_forget()
    spinscreenwheel = PhotoImage(file="images/the wheel treasure.png")
    Qlabel = Label(qsr, image=spinscreenwheel, anchor="center")
    Qlabel.place(relx=0, y=0)
    qsr.after(450,chestbattlestart)
    qsr.after(500,qsr.destroy)
    qsr.mainloop()


def Wmoney():
    global psL
    global pbL
    global qsr
    global NQlabel
    from TheWorld import coinslvl3clear
    from TheWorld import THEboard
    NQlabel.place_forget()
    spinscreenwheel = PhotoImage(file="images/Slay-the-Spire-Wheel-Spin.png")
    Qlabel = Label(qsr, image=spinscreenwheel, anchor="center")
    Qlabel.place(relx=0, y=0)
    currentmoney = psL['B2'].value
    newval = currentmoney + 100
    psL['B2'].value = newval
    pbL.save('Excel files/Player Data.xlsx')
    qsr.after(100,coinslvl3clear)
    qsr.after(140,THEboard)
    qsr.after(800,qsr.destroy)
    qsr.mainloop()

def wheelspinnerRUN():
    wheelchoice = random.randint(2,2)

    if wheelchoice ==1:
        print("money")
        Wmoney()
    if wheelchoice ==2:
        print("chest")
        Wchest()
    if wheelchoice ==3:
        print("delete card")
        Wcurse()
    if wheelchoice ==4:
        print("death")
    if wheelchoice ==5:
        print("curse card")
    if wheelchoice ==6:
        print("regen")

def spinwheelstart():
    global Qlabel
    global qsr
    global NQlabel

    Qlabel.place_forget()
    spinscreenwheel = PhotoImage(file="images/Slay-the-Spire-Wheel-Spin.png")
    NQlabel = Label(qsr, image=spinscreenwheel, anchor="center")
    NQlabel.place(relx=0, y=0)
    wheelspinner = PhotoImage(file="images/Wheel spinner.png")
    THEspin=Button(qsr,image=wheelspinner,command=wheelspinnerRUN)
    THEspin.place(relx=0.16,y=598)
    qsr.mainloop()

def startQroom():
    global Qlabel
    global qsr
    global psL
    global pbL
    qsr = Toplevel()
    qsr.geometry("1500x805")
    theroomchoice = random.randint(1,1)
    pbL = load_workbook("Excel files/Player Data.xlsx")
    psL = pbL.active
    if theroomchoice ==1:
        spinscreenguy=PhotoImage(file="images/wheel start.png")
        Qlabel=Label(qsr,image=spinscreenguy,anchor="center")
        Qlabel.place(relx=0,y=0)

        pagebutton1=PhotoImage(file="images/spinguypage button.png")
        pagebutton1B=Button(qsr,image=pagebutton1,command=spinwheelstart)
        pagebutton1B.place(relx=0.43,y=612)


    qsr.mainloop()

