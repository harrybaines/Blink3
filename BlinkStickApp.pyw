##BlinkStick App

#Modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.colorchooser import *
from blinkstick import blinkstick

#Global variables
backgroundColor = "#003366"
backgroundColor1 = "#000000"

texty = "#ffffff"

class App:

       def __init__(self):
              #Window
              self.root = Tk()
              self.defaultbg = backgroundColor
              self.testbg = backgroundColor1
              self.colorText = StringVar()
              self.colorText.set("No Colour Selected")


              self.root.geometry("620x620+625+50")
              self.root.title("blink3")
              self.root.resizable(0,0)

              #Notebook widget
              self.note = ttk.Notebook(self.root, width=620, height=620,)
              self.home = Frame(self.note, bg=self.defaultbg)
              self.note.add(self.home, text='Home')
              self.colours = Frame(self.note, bg=self.defaultbg)
              self.note.add(self.colours, text='Colours')
              self.settings = Frame(self.note, bg=self.defaultbg)
              self.note.add(self.settings, text='Settings')

              self.note.pack()

              #Properties
              self.v = IntVar()
              self.colorDict = {0:"temp",1:"red",2:"blue",3:"green",4:"yellow",5:"white",6:"grey",7:"purple"}

              #Home Frames
              self.topHFrame = Frame(self.home,pady=10, bg=self.defaultbg)
              self.topHFrame.pack(side=TOP)
              self.leftHFrame = Frame(self.home,padx=20, bg=self.defaultbg)
              self.leftHFrame.pack(side=LEFT)

              #Home widgets
              self.homeLbl = Label(self.topHFrame,text='Blink3',foreground=texty, background=self.defaultbg, font=('Corbel',24)).grid(row=0,column=0)
              self.vLbl = Label(self.topHFrame,foreground=texty, background=self.defaultbg,text='a blinkstick control app',font=('Corbel',15)).grid(row=1,column=0)

              self.vLbl = Label(self.topHFrame, foreground=texty, background=self.defaultbg, text='v1.0 - developed by alt3.readn.uk',font=('Corbel',15)).grid(row=2,column=0,pady=(30,0))

              self.quitBut = Button(self.topHFrame,text='Quit',highlightbackground=self.defaultbg,command=self.__quit__).grid(row=3,column=0,pady=20)





              #--------------------------------------------------------------------------------------------
              # colour window

              self.colourTopFrame = Frame(self.colours,pady=10, bg=self.defaultbg)
              self.colourTopFrame.pack(side=TOP)

              self.colourLeftFrame = Frame(self.colours, bg=self.defaultbg)
              self.colourLeftFrame.pack(side=LEFT, pady=(0,50))


              self.colorLbl = Label(self.colourTopFrame,text='Colours',foreground=texty, bg=self.defaultbg, font=('Corbel',24)).pack()

              self.cOptsLbl = Label(self.colourTopFrame,foreground=texty, bg=self.defaultbg,text='Choose a default colour or a custom colour:',font=('Sitka',16)).pack()

              self.redLbl = Label(self.colourLeftFrame,foreground=texty, bg=self.defaultbg,text='Red',font=('Sitka',14)).grid(row=3,column=0,pady=2,padx=(70,60))
              self.blueLbl = Label(self.colourLeftFrame,foreground=texty, bg=self.defaultbg,text='Blue',font=('Sitka',14)).grid(row=4,column=0,pady=2,padx=(70,60))
              self.greenLbl = Label(self.colourLeftFrame,foreground=texty, bg=self.defaultbg,text='Green',font=('Sitka',14)).grid(row=5,column=0,pady=2,padx=(70,60))
              self.yellowLbl = Label(self.colourLeftFrame,foreground=texty, bg=self.defaultbg,text='Yellow',font=('Sitka',14)).grid(row=6,column=0,pady=2,padx=(70,60))
              self.whiteLbl = Label(self.colourLeftFrame,foreground=texty, bg=self.defaultbg,text='White',font=('Sitka',14)).grid(row=7,column=0,pady=2,padx=(70,60))
              self.greyLbl = Label(self.colourLeftFrame,foreground=texty, bg=self.defaultbg,text='Grey',font=('Sitka',14)).grid(row=8,column=0,pady=2,padx=(70,60))
              self.purpleLbl = Label(self.colourLeftFrame,foreground=texty, bg=self.defaultbg,text='Purple',font=('Sitka',14)).grid(row=9,column=0,pady=2,padx=(70,60))

              
              self.redRad = Radiobutton(self.colourLeftFrame,bg=self.defaultbg,command=self.setDefColor, highlightthickness=0,variable=self.v,value=1).grid(row=3,column=0,padx=(0,100))
              self.blueRad = Radiobutton(self.colourLeftFrame,bg=self.defaultbg,command=self.setDefColor, variable=self.v,value=2).grid(row=4,column=0,padx=(0,100))
              self.greenRad = Radiobutton(self.colourLeftFrame,bg=self.defaultbg,command=self.setDefColor, variable=self.v,value=3).grid(row=5,column=0,padx=(0,100))
              self.yellowRad = Radiobutton(self.colourLeftFrame,bg=self.defaultbg,command=self.setDefColor, variable=self.v,value=4).grid(row=6,column=0,padx=(0,100))
              self.whiteRad = Radiobutton(self.colourLeftFrame,bg=self.defaultbg,command=self.setDefColor, variable=self.v,value=5).grid(row=7,column=0,padx=(0,100))
              self.greyRad = Radiobutton(self.colourLeftFrame,bg=self.defaultbg,command=self.setDefColor, variable=self.v,value=6).grid(row=8,column=0,padx=(0,100))
              self.purpleRad = Radiobutton(self.colourLeftFrame,bg=self.defaultbg,command=self.setDefColor, variable=self.v,value=7).grid(row=9,column=0,padx=(0,100))

              self.chooseLbl = Label(self.colourLeftFrame,foreground=texty, bg=self.defaultbg,text='Pick a color:',font=('Corbel',15)).grid(row=4,column=2, pady=(10,0), padx=(5,400))
              self.defaultLbl = Label(self.colourLeftFrame,foreground=texty, bg=self.defaultbg,text='by default, it is random',font=('Corbel',10)).grid(row=5,column=2, padx=(5,400))
              self.colourbutton = Button(self.colourLeftFrame, highlightbackground=self.defaultbg, text='Set Color', command=self.setOwnColor).grid(row=6,column=2,pady=(10,0), padx=(5,400))



              self.colorSelectedLabel = Label(self.colourLeftFrame,foreground=texty, bg=self.defaultbg,textvariable=self.colorText, font=('Sitka',14)).grid(row=10,column=0,pady=20,padx=(200,0))
              self.blinkTypeBox = Listbox(self.colourLeftFrame, width=13, height=7)
              self.blinkTypeBox.grid(row=11,column=0,pady=20)
              self.fillListbox()
              

              
              





              #--------------------------------------------------------------------------------------------
              # settings window

              self.settingTopFrame = Frame(self.settings,pady=10, bg=self.defaultbg)
              self.settingTopFrame.pack(side=TOP)

              self.settingsLbl = Label(self.settingTopFrame,text='Settings',foreground=texty, bg=self.defaultbg, font=('Corbel',24)).grid(row=0,column=0)
              #On/Off buttons
              self.powerLbl = Label(self.settingTopFrame,foreground=texty, bg=self.defaultbg,text='Power your blinkstick',font=('Corbel',15)).grid(row=1,column=0)

              self.onlabel = Label(self.settingTopFrame,foreground=texty, bg=self.defaultbg,text='ON',font=('Sitka',16)).grid(row=2,column=0,padx=(0,70),pady=10)
              self.offlabel = Label(self.settingTopFrame,foreground=texty, bg=self.defaultbg,text='OFF',font=('Sitka',16)).grid(row=3,column=0,padx=(0,70))

              self.onrad = Radiobutton(self.settingTopFrame,foreground=texty, bg=self.defaultbg, command=self.blinkon,variable=self.v,value=1).grid(row=2,column=0,padx=(40,0))
              self.offrad = Radiobutton(self.settingTopFrame,foreground=texty, bg=self.defaultbg, command=self.blinkoff, variable=self.v,value=0).grid(row=3,column=0,padx=(40,0))





              #--------------------------------------------------------------------------------------------

              self.root.mainloop()




# Methods
       def fillListbox(self):
          self.blinkTypeArray = ['Static','Blink','Pulse','Morph']
          for i in self.blinkTypeArray:
             self.blinkTypeBox.insert(END,i)




       def setOwnColor(self):
           bstick = blinkstick.find_first()
           self.bcolor = askcolor()[1]

           if bstick is not None:
              bstick.set_color(hex=self.bcolor)
           else:
              self.warn()

       def setDefColor(self):
          self.colorText.set(self.colorDict[self.v.get()])

       # def __blink__(self):
       #        bstick = blinkstick.find_first()

       #        self.color = self.colorDict[self.v.get()]

       #        if bstick is not None:
       #           bstick.pulse(name=self.color, repeats=5,
       #                            duration=20)
       #        else:
       #           self.warn()

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
       Blink3 = App()








