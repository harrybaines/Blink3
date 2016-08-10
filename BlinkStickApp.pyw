##BlinkStick App

#test
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.colorchooser import *
from blinkstick import blinkstick

bg = "#212121"
text = "#ffffff"
mycolor = "#ffffff"

class App:

       def __init__(self):
              #Window
              self.root = Tk()
              self.defaultbg = bg
              self.root.geometry("500x500+100+50")
              self.root.title("blink3")

              #Notebook widget
              self.note = ttk.Notebook(self.root, width=500, height=500,)
              self.home = Frame(self.note, background=bg)
              self.note.add(self.home, text='Home')
              self.colour = Frame(self.note, background=bg)
              self.note.add(self.colour, text='Colour')

              self.note.pack()

              #Home Frames
              self.topHFrame = Frame(self.home,pady=10, background=bg)
              self.topHFrame.pack(side=TOP)
              self.leftHFrame = Frame(self.home,padx=20)
              self.leftHFrame.pack(side=LEFT)

              #Home widgets

              self.homeLbl = Label(self.topHFrame,text='Blink3',foreground=text, background=bg, font=('Corbel',24)).grid(row=0,column=0)
              self.vLbl = Label(self.topHFrame,foreground=text, background=bg,text='a blinkstick control app',font=('Corbel',15)).grid(row=1,column=0)

              self.cOptsLbl = Label(self.topHFrame,foreground=text, background=bg,text='Colour Options:',font=('Sitka',16)).grid(row=2,column=0,pady=(10,0),padx=(30,60))
              self.redLbl = Label(self.topHFrame,foreground=text, background=bg,text='Red',font=('Sitka',14)).grid(row=3,column=0,pady=5,padx=(70,60))
              self.blueLbl = Label(self.topHFrame,foreground=text, background=bg,text='Blue',font=('Sitka',14)).grid(row=4,column=0,pady=5,padx=(70,60))
              self.greenLbl = Label(self.topHFrame,foreground=text, background=bg,text='Green',font=('Sitka',14)).grid(row=5,column=0,pady=5,padx=(70,60))
              self.yellowLbl = Label(self.topHFrame,foreground=text, background=bg,text='Yellow',font=('Sitka',14)).grid(row=6,column=0,pady=5,padx=(70,60))
              self.whiteLbl = Label(self.topHFrame,foreground=text, background=bg,text='White',font=('Sitka',14)).grid(row=7,column=0,pady=5,padx=(70,60))
              self.greyLbl = Label(self.topHFrame,foreground=text, background=bg,text='Grey',font=('Sitka',14)).grid(row=8,column=0,pady=5,padx=(70,60))
              self.purpleLbl = Label(self.topHFrame,foreground=text, background=bg,text='Purple',font=('Sitka',14)).grid(row=9,column=0,pady=5,padx=(70,60))

              self.v = IntVar()

              self.colorDict = {0:"temp",1:"red",2:"blue",3:"green",4:"yellow",5:"white",6:"grey",7:"purple"}

              self.redRad = Radiobutton(self.topHFrame,foreground=text, background=bg,variable=self.v,value=1).grid(row=3,column=0,padx=(0,100))
              self.blueRad = Radiobutton(self.topHFrame,foreground=text, background=bg,variable=self.v,value=2).grid(row=4,column=0,padx=(0,100))
              self.greenRad = Radiobutton(self.topHFrame,foreground=text, background=bg,variable=self.v,value=3).grid(row=5,column=0,padx=(0,100))
              self.yellowRad = Radiobutton(self.topHFrame,foreground=text, background=bg,variable=self.v,value=4).grid(row=6,column=0,padx=(0,100))
              self.whiteRad = Radiobutton(self.topHFrame,foreground=text, background=bg,variable=self.v,value=5).grid(row=7,column=0,padx=(0,100))
              self.greyRad = Radiobutton(self.topHFrame,foreground=text, background=bg,variable=self.v,value=6).grid(row=8,column=0,padx=(0,100))
              self.purpleRad = Radiobutton(self.topHFrame,foreground=text, background=bg,variable=self.v,value=7).grid(row=9,column=0,padx=(0,100))

              self.applyColours = Button(self.topHFrame,text='Apply', highlightbackground=bg, command=self.__blink__).grid(row=10,column=0,pady=5,padx=(10,100))
              self.quitBut = Button(self.topHFrame,text='Quit',highlightbackground=bg,command=self.__quit__).grid(row=10,column=0,pady=5,padx=(30,0))

              self.vLbl = Label(self.topHFrame, foreground=text, background=bg, text='v1.0 - developed by alt3.readn.uk',font=('Corbel',15)).grid(row=11,column=0,pady=(30,0))


              #--------------------------------------------------------------------------------------------
              # colour window

              self.colourtopHFrame = Frame(self.colour,pady=10, background=bg)
              self.colourtopHFrame.pack(side=TOP)
              self.colourleftHFrame = Frame(self.colour,padx=20)
              self.colourleftHFrame.pack(side=LEFT)

              self.homeLbl = Label(self.colourtopHFrame,text='Blink3',foreground=text, background=bg, font=('Corbel',24)).grid(row=0,column=0)
              #On/Off buttons
              self.vLbl = Label(self.colourtopHFrame,foreground=text, background=bg,text='Power your blinkstick',font=('Corbel',15)).grid(row=1,column=0)


              self.offlabel = Label(self.colourtopHFrame,foreground=text, background=bg,text='OFF',font=('Sitka',16)).grid(row=2,column=0,padx=(0,70))
              self.onlabel = Label(self.colourtopHFrame,foreground=text, background=bg,text='ON',font=('Sitka',16)).grid(row=2,column=2,padx=(0,400))

              self.offrad = Radiobutton(self.colourtopHFrame,foreground=text, background=bg, command=self.blinkoff, variable=self.v,value=0).grid(row=2,column=0,padx=(0,0))
              self.onrad = Radiobutton(self.colourtopHFrame,foreground=text, background=bg, command=self.blinkon,variable=self.v,value=1).grid(row=2,column=2,padx=(0,460))

          
              self.vLbl = Label(self.colourtopHFrame,foreground=text, background=bg,text='Pick a color for your Blinkstick',font=('Corbel',15)).grid(row=3,column=0, pady=(20,0))
              self.vLbl = Label(self.colourtopHFrame,foreground=text, background=bg,text='by default, it is random',font=('Corbel',10)).grid(row=4,column=0,)

              self.colourbutton = Button(self.colourtopHFrame, highlightbackground=bg, text='Set Color', command=self.setOwnColor).grid(row=5,column=0,pady=(10,0), padx=(90,100))

              self.root.mainloop()


# Definitions

       def setOwnColor(self):
           bstick = blinkstick.find_first()
           self.bcolor = askcolor()[1]

           if bstick is not None:
                     bstick.set_color(hex=self.bcolor)
           else:
                     self.warn()


       def __blink__(self):
              bstick = blinkstick.find_first()

              self.color = self.colorDict[self.v.get()]

              if bstick is not None:
                     bstick.pulse(name=self.color, repeats=5,
                                  duration=20)
              else:
                     self.warn()

       def blinkof(self):
              print()

       def blinkon(self):
              for bstick in blinkstick.find_all():
                   bstick.set_random_color()

       def blinkoff(self):
              for bstick in blinkstick.find_all():
                  bstick.turn_off()


# Alerts go below this point

       def __quit__(self):
           result = messagebox.askquestion("Blink3 - Quit?", "Are you sure you want to quit Blink3?",)
           if result == 'yes':
              self.root.quit()
           else:
               print()
               



       def warn(self):
              messagebox.showinfo("Blink3 Error", "No Blinksticks could be found! Please check your USB ports", icon='warning')


if __name__ == "__main__":
       client = App()








