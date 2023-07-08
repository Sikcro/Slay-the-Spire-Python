import tkinter as tk
from PIL import Image, ImageTk
from itertools import count

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

root = tk.Tk()
lbl = ImageLabel(root)
lbl.pack()
lbl.load('images/The Defect.gif')
root.mainloop()


#def auto_drawhand_animslot5():
#    global str
#    global firstbscreen
#    slot5 = Button(firstbscreen, image=str)
#    slot5.place(relx=0.6, y=800, anchor="center")

#    firstbscreen.mainloop()


#def auto_drawhand_animslot4():
#    global str
#    global firstbscreen
#    slot4 = Button(firstbscreen, image=str)
#    slot4.place(relx=0.5, y=800, anchor="center")

#    firstbscreen.mainloop()


#def auto_drawhand_animslot3():
#    global str
#    global firstbscreen
#    slot3 = Button(firstbscreen, image=str)
#    slot3.place(relx=0.4, y=800, anchor="center")

#    firstbscreen.mainloop()


#def auto_drawhand_animslot2():
 #   global str
  #  global firstbscreen
   # global blo
    #global atkcardcounter
   # global blockcardcounter
    #diceslot2 = random.randint(1, 2)

    #if diceslot2 == 1:
       # slot2 = Button(firstbscreen, image=str)
      #  slot2.place(relx=0.3, y=800, anchor="center")
     #   atkcardcounter = atkcardcounter + 1

    #if diceslot2 == 2:
   #     slot2 = Button(firstbscreen, image=blo)
  #      slot2.place(relx=0.3, y=800, anchor="center")
 #       blockcardcounter = blockcardcounter + 1
#
 #   firstbscreen.mainloop()
#
#
#def auto_drawhand_animslot1():
#    global str
    #global firstbscreen
   # global blo
  #  global atkcardcounter
 #   global blockcardcounter
#    diceslot1 = random.randint(1, 2)

    #if diceslot1 == 1:
   #     slot1 = Button(firstbscreen, image=str)
  #      slot1.place(relx=0.2, y=800, anchor="center")
 #       atkcardcounter = atkcardcounter + 1
#       print("A:", atkcardcounter)
#
  #  if diceslot1 == 2:
 #       slot1 = Button(firstbscreen, image=blo)
 #       slot1.place(relx=0.2, y=800, anchor="center")
 #       blockcardcounter = blockcardcounter + 1
 #       print("B:", blockcardcounter)

 #   firstbscreen.mainloop()