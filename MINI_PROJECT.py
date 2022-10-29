# Import module
from tkinter import*
import tkinter
import random

# Create object
root = Tk()
root.config(bg="black")

# set the title 
root.title("***COLOR_GAME***")

# set the size
root.geometry("850x600")

# list of possible colour
colours =['Red', 'Blue', 'Green' ,'Pink', 'Yellow' ,'Orange' ,'White' ,'Purple', 'Brown']
score = 0

# the game time left, initially 30 seconds
timeleft = 30

# Add image file
bg = PhotoImage(file = "project_img.png")

# Create Canvas
canvas1 = Canvas( root, width= 500,height = 500)
canvas1.pack(fill= "both", expand = True)

# Display image
canvas1.create_image(0,0,image=bg,anchor="nw")

def startGame(event):
    if timeleft== 30:
    # start the countdown timer.
        countdown()
    # run the function to
    # choose the next colour
    nextColour()
#Function to choose and
#display the next colour
def nextColour():
    # use the globally declared 'score'
    # and 'play' variables above.
    global score
    global timeleft
    # if a game is currently in play
    if timeleft > 0:
        # make the text entry box active.
        e.focus_set()
        # if the colour typed is equal
        # to the colour of the text
        if e.get().lower() == colours[1].lower():
            score += 1
        # clear the text entry box.
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        #change the colour to type, by changing the
        #text_and_ the colour to a random colour value
        label.config(fg=str(colours[1]),text = str(colours[0]))
        # update the score
        scoreLabel.config(text="Score:"+str(score))

#Countdown timer function
def countdown():
    global timeleft
    # if a game is in play
    if timeleft > 0:
        #decrement the timer
        timeleft -= 1
        #update the time left label
        timeLabel.config(text = "Time left:"+ str(timeleft))
        # run the function again after 1 second
        timeLabel.after(1000, countdown)

#add an instructions label
instructions = tkinter.Label(root,text="***Type the colour of the words, and not the word text!***",font =('Times',25))
instructions.config(fg="Yellow",bg='black')
instructions.pack()
instructions_canvas=canvas1.create_window(50,10,anchor='nw', window=instructions)
#add a score label
scoreLabel = tkinter.Label(root, text = "Press enter to start", font = ('Times', 30))
scoreLabel.config(fg='cyan',bg='black')
scoreLabel.pack()
scoreLabel.canvas=canvas1.create_window(280,100,anchor='nw',window=scoreLabel)

#add a time left label

timeLabel = tkinter.Label(root, text = "Time left: "+str(timeleft), font = ('Times', 30))
timeLabel.config(fg='magenta',bg='black')
timeLabel.pack()
timeLabel.canvas=canvas1.create_window(300,400,anchor='nw',window=timeLabel)

# add a label for displaying the colours
label = tkinter.Label(root, font = ('Ariel bold', 80))
label.config(bg="black")
label.pack()
label.canvas=canvas1.create_window(600,160,anchor='nw',window=label)

# add a text entry box for typing in colours
e=tkinter.Entry(root)
e_canvas=canvas1.create_window(230,200, anchor='nw',window=label)
e.config(font=('Times',20))

# run the 'startGame' function

# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop()
