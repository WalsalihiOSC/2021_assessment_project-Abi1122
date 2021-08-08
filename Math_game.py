from tkinter import *
from typing import Sized
from game_info import player_in
## linking student class to the main code

class Mathgame :
    ## this intial windows start he program
    def __init__(self):
        self.welcome_frame = Frame(root,width="700",height="500") ## sets the size of the frame and creating the frame
        self.welcome_frame.grid() ## using .grid to position everything in to place.

        ## creating all the label/ titles for the front page.
        Label(self.welcome_frame,text="SHEEEH").grid(column=3,row=1)
        Label(self.welcome_frame,text="Name :").grid(column=2, row=3)
        Label(self.welcome_frame,text="Year :").grid(column=2, row=4)

        ## creating all the entries and buttons to allow the user to input information.
        self.player_name= Entry(self.welcome_frame)
        self.player_name.grid(column=4, row=3)
        self.year_level = Entry(self.welcome_frame)
        self.year_level.grid(column=4, row=4)

        Button(self.welcome_frame, text="Continue", command=self.how_to).grid(column=7, row=8)

        Button(self.welcome_frame, text="Easy").grid(column=2, row=5) 
        Button(self.welcome_frame, text="Medium").grid(column=3, row=5)
        Button(self.welcome_frame, text="Hard").grid(column=4, row=5) 

        Button(self.welcome_frame, text="Add").grid(column=2, row=6) 
        Button(self.welcome_frame, text="Subtract").grid(column=3, row=6)
        Button(self.welcome_frame, text="Multiple").grid(column=4, row=6)

    def how_to(self):
        ##creating help page
        self.welcome_frame.grid_forget() ## hiding the previous frame to create the next one.
        self.howto = Frame(root,width="700",height="500") ## sets the size of the frame and creating the frame
        self.howto.grid() ## using .grid to position everything in to place.

        ## Creating all the text and titles.
        Label(self.howto, text="How To Play" ).grid(column=3 , row=1)
        Label(self.howto, text=" You will get question like “2 + 2 ”.").grid(column=3, row= 3)
        Label(self.howto, text=" Then beside it will be a box please press it").grid(column=3, row= 4)
        Label(self.howto, text=" And type your answer.").grid(column=3, row= 5)

        Label(self.howto, text="").grid(column=1, row= 2)
        
        ##creating the buttons.
        Button(self.howto, text="Continue", command=self.how_to).grid(column=7, row=8)


    

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