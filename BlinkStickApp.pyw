##BlinkStick App

#test
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from blinkstick import blinkstick


class App:

       def __init__(self):
              #Window
              self.root = Tk()
              self.root.geometry("500x500+100+50")
              self.root.title("blink3")

              #Notebook widget
              self.note = ttk.Notebook(self.root, width=500, height=500)
              self.home = Frame(self.note)
              self.note.add(self.home, text='Home')

              self.note.pack()

              #Frames
              self.topHFrame = Frame(self.home,pady=10)
              self.topHFrame.pack(side=TOP)
              self.leftHFrame = Frame(self.home,padx=20)
              self.leftHFrame.pack(side=LEFT)

              #Window widgets

              self.homeLbl = Label(self.topHFrame,text='BlinkStick Client',relief=RAISED,font=('Sitka',24)).grid(row=0,column=0)
              self.vLbl = Label(self.topHFrame,text='v1.0',relief=RAISED,font=('Courier',15)).grid(row=1,column=0)

              self.cOptsLbl = Label(self.topHFrame,text='Colour Options:',font=('Sitka',16)).grid(row=2,column=0,pady=(10,0),padx=(0,220))
              self.redLbl = Label(self.topHFrame,text='Red',font=('Sitka',14)).grid(row=3,column=0,pady=5,padx=(0,220))
              self.blueLbl = Label(self.topHFrame,text='Blue',font=('Sitka',14)).grid(row=4,column=0,pady=5,padx=(0,220))
              self.greenLbl = Label(self.topHFrame,text='Green',font=('Sitka',14)).grid(row=5,column=0,pady=5,padx=(0,220))
              self.yellowLbl = Label(self.topHFrame,text='Yellow',font=('Sitka',14)).grid(row=6,column=0,pady=5,padx=(0,220))
              self.whiteLbl = Label(self.topHFrame,text='White',font=('Sitka',14)).grid(row=7,column=0,pady=5,padx=(0,220))
              self.greyLbl = Label(self.topHFrame,text='Grey',font=('Sitka',14)).grid(row=8,column=0,pady=5,padx=(0,220))
              self.purpleLbl = Label(self.topHFrame,text='Purple',font=('Sitka',14)).grid(row=9,column=0,pady=5,padx=(0,220))

              self.v = IntVar()

              self.colorDict = {0:"temp",1:"red",2:"blue",3:"green",4:"yellow",5:"white",6:"grey",7:"purple"}

              self.redRad = Radiobutton(self.topHFrame,variable=self.v,value=1).grid(row=3,column=0,padx=(0,100))
              self.blueRad = Radiobutton(self.topHFrame,variable=self.v,value=2).grid(row=4,column=0,padx=(0,100))
              self.greenRad = Radiobutton(self.topHFrame,variable=self.v,value=3).grid(row=5,column=0,padx=(0,100))
              self.yellowRad = Radiobutton(self.topHFrame,variable=self.v,value=4).grid(row=6,column=0,padx=(0,100))
              self.whiteRad = Radiobutton(self.topHFrame,variable=self.v,value=5).grid(row=7,column=0,padx=(0,100))
              self.greyRad = Radiobutton(self.topHFrame,variable=self.v,value=6).grid(row=8,column=0,padx=(0,100))
              self.purpleRad = Radiobutton(self.topHFrame,variable=self.v,value=7).grid(row=9,column=0,padx=(0,100))

              self.applyColours = Button(self.topHFrame,text='Apply',command=self.__blink__).grid(row=10,column=0,pady=5,padx=(0,100))
              self.quitBut = Button(self.topHFrame,text='Quit',command=self.__quit__).grid(row=10,column=0,pady=5,padx=(0,220))

              self.root.mainloop()


       def __blink__(self):
              bstick = blinkstick.find_first()

              self.color = self.colorDict[self.v.get()]

              if bstick is not None:
                     bstick.pulse(name=self.color, repeats=5,
                                  duration=20)
              else:
                     warn()




       def __quit__(self):
           result = messagebox.askquestion("Blink3 - Quit?", "Are you sure you want to quit Blink3?",)
           if result == 'yes':
              self.root.quit()
           else:
               print()
               


def warn():
       messagebox.showinfo("Blink3 Error", "No Blinksticks could be found! Please check your USB ports", icon='warning')



if __name__ == "__main__":
       client = App()
















