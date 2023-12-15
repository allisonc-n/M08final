#Allison Nikirk
#M08 Final Project

#importing easy frame
from breezypythongui import EasyFrame

class Travel(EasyFrame):
#this displays the topic of this page
    def __init__(self):
        #sets up the window and label
        EasyFrame.__init__(self, title='Travel', width=500,height=500)
        #this adds the travel label at the top
        self.addLabel(text = "Travel", row = 0, column = 0)
        
        self.setBackground('black')
        #this button is for athens
        self.addButton(text='Athens', row=0,column=0,sticky="NSEW",command=self.NEWPAGE)
        #this button is for London
        self.addButton(text='London', row=0,column=1,sticky="NSEW",command=self.NEWPAGE)
    def NEWPAGE(self):
        self.destroy()
        THENEWPAGE().mainloop()
#starting a new class
class THENEWPAGE:
    def __init__(self):
        EasyFrame.__init__(self,tuple)
def main():
    Travel().mainloop()

if __name__ == "__main__":
    main()
