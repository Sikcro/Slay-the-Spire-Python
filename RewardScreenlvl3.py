from tkinter import *
import random
from openpyxl import workbook, load_workbook



def skipbutton():
    global rscreen
    from TheWorld import THEboard
    rscreen.destroy()
    THEboard()
def cardselection1():
    global wb2
    global ws2
    global rscreen

    if ws2['B10'] =="True":
        print("col 1 working")
        thercard = ws2['A11']
        thercard.value = "multi"
        ws2['B11'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)

    elif ws2['B11'] == "True":
        print("col 1 working")
        thercard = ws2['A12']
        thercard.value = "multi"
        ws2['B12'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)

    elif ws2['B12'] == "True":
        print("col 1 working")
        thercard = ws2['A13']
        thercard.value = "multi"
        ws2['B13'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)





def cardselection2():
    global wb2
    global ws2

    if ws2['B10'] =="True":
        print("col 2 working")
        thercard = ws2['A11']
        thercard.value = "repair"
        ws2['B11'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)

    elif ws2['B11'] =="True":
        print("col 2 working")
        thercard = ws2['A12']
        thercard.value = "repair"
        ws2['B12'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)

    elif ws2['B12'] == "True":
        print("col 2 working")
        thercard = ws2['A13']
        thercard.value = "repair"
        ws2['B13'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)



def cardselection3():
    global wb2
    global ws2

    if ws2['B10'] =="True":
        print("col 3 working")
        thercard = ws2['A11']
        thercard.value = "heavy"
        ws2['B11'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)

    elif ws2['B11'] =="True":
        print("col 3 working")
        thercard = ws2['A12']
        thercard.value = "heavy"
        ws2['B12'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)

    elif ws2['B12'] == "True":
        print("col 3 working")
        thercard = ws2['A13']
        thercard.value = "heavy"
        ws2['B13'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)



def cardselection5():
    global wb2
    global ws2

    if ws2['B10'] =="True":
        print("col 5 working")
        thercard = ws2['A11']
        thercard.value = "30block"
        ws2['B11'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)

    else:
        print("col 5 working")
        thercard = ws2['A10']
        thercard.value = "30block"
        ws2['B10'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)




def cardselection6():
    global wb2
    global ws2

    if ws2['B10'] =="True":
        print("col 6 working")
        thercard = ws2['A11']
        thercard.value = "moreE"
        ws2['B11'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)

    else:
        print("col 6 working")
        thercard = ws2['A10']
        thercard.value = "moreE"
        ws2['B10'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)



def cardselection4():
    global wb2
    global ws2

    if ws2['B10'] =="True":
        print("col 4 working")
        thercard = ws2['A11']
        thercard.value = "Double"
        ws2['B11'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)

    else:
        print("col 4 working")
        thercard = ws2['A10']
        thercard.value = "Double"
        ws2['B10'].value = "True"
        wb2.save('Excel files/Active Deck.xlsx')
        rscreen.after(200, skipbutton)





def cardoptions():
    global rscreen

    leftcardchoice=random.randint(1,6)
    midcardchoice=random.randint(1,6)
    rightcardchoice=random.randint(1,6)

    bigblock=PhotoImage(file="images/30 block card.png")
    repair=PhotoImage(file="images/Self repair card.png")
    heavyhit=PhotoImage(file="images/Heavy hit card reskin.png")
    multihit=PhotoImage(file="images/multi slash card.png")
    doublestr=PhotoImage(file="images/Double Strength card.png")
    more_energy=PhotoImage(file="images/Double Energy.png")

    if leftcardchoice==1:
        leftcard=Button(rscreen,image=multihit,command=cardselection1)
        leftcard.place(relx=0.3,y=300)

    if leftcardchoice==2:
        leftcard=Button(rscreen,image=repair,command=cardselection2)
        leftcard.place(relx=0.3,y=300)



    if leftcardchoice == 3:
        leftcard = Button(rscreen, image=heavyhit,command=cardselection3)
        leftcard.place(relx=0.3, y=300)


    if leftcardchoice == 4:
        leftcard = Button(rscreen, image=doublestr,command=cardselection4)
        leftcard.place(relx=0.3, y=300)

    if leftcardchoice == 5:
        leftcard = Button(rscreen, image=bigblock,command=cardselection5)
        leftcard.place(relx=0.3, y=300)


    if leftcardchoice == 6:
        leftcard = Button(rscreen, image=more_energy,command=cardselection6)
        leftcard.place(relx=0.3, y=300)


    if midcardchoice == 1:
        midcard = Button(rscreen, image=multihit,command=cardselection1)
        midcard.place(relx=0.45, y=300)


    if midcardchoice == 2:
        midcard = Button(rscreen, image=repair,command=cardselection2)
        midcard.place(relx=0.45, y=300)


    if midcardchoice == 3:
        midcard = Button(rscreen, image=heavyhit,command=cardselection3)
        midcard.place(relx=0.45, y=300)


    if midcardchoice == 4:
        midcard = Button(rscreen, image=doublestr,command=cardselection4)
        midcard.place(relx=0.45, y=300)


    if midcardchoice == 5:
        midcard = Button(rscreen, image=bigblock,command=cardselection5)
        midcard.place(relx=0.45, y=300)


    if midcardchoice == 6:
        midcard = Button(rscreen, image=more_energy,command=cardselection6)
        midcard.place(relx=0.45, y=300)


    if rightcardchoice == 1:
        rightcard = Button(rscreen, image=multihit,command=cardselection1)
        rightcard.place(relx=0.6, y=300)


    if rightcardchoice == 2:
        rightcard = Button(rscreen, image=repair,command=cardselection2)
        rightcard.place(relx=0.6, y=300)


    if rightcardchoice == 3:
        rightcard = Button(rscreen, image=heavyhit,command=cardselection3)
        rightcard.place(relx=0.6, y=300)

    if rightcardchoice == 4:
        rightcard = Button(rscreen, image=doublestr,command=cardselection4)
        rightcard.place(relx=0.6, y=300)


    if rightcardchoice == 5:
        rightcard = Button(rscreen, image=bigblock,command=cardselection5)
        rightcard.place(relx=0.6, y=300)


    if rightcardchoice == 6:
        rightcard = Button(rscreen, image=more_energy,command=cardselection6)
        rightcard.place(relx=0.6, y=300)



    rscreen.mainloop()


def Rewardstartlvl3():
    global rscreen
    global wb2
    global ws2

    wb2 = load_workbook("Excel files/Active Deck.xlsx")
    ws2 = wb2.active
    rscreen=Toplevel()
    rscreen.geometry("1500x875")
    bgI=PhotoImage(file="images/win screen.png")
    bg=Label(rscreen,image=bgI)
    bg.place(x=0,y=0)
    ski=PhotoImage(file="images/Skip button.png")
    skipbuttonB=Button(rscreen,image=ski,command=skipbutton)
    skipbuttonB.place(relx=0.44,y=590)
    cardoptions()

    rscreen.mainloop()

