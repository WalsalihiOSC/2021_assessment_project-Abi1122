from tkinter import *
from typing import Sized

## linking student class to the main code

class Mathgame :
    ## this intial windows start he program
    def __init__(self):
        self.welcome_frame = Frame(root,width="700",height="500") ## sets the size of the frame and creating the frame
        self.welcome_frame.grid() ## using .grid to position everything in to place.

        ## creating the basic button and label of design 

        ## creating all the label/ titles for the front page.
        Label(self.welcome_frame,text="SHEEEH").grid(column=3,row=1)
        Label(self.welcome_frame,text="Name :").grid(column=2, row=3)
        Label(self.welcome_frame,text="Year :").grid(column=2, row=4)
        

    

    def backb(self, pframe, cframe):
        ## function allows to go back to the preivous frame.
        cframe.grid_remove()
        pframe.grid()

    
                    

        
## setting the root and the size of the window that is created and the name on the top.
root = Tk()
root.title("Ormiston Course Selection")
root.geometry("700x500")
Mathgame()
root.mainloop()