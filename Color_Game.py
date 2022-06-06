import tkinter
import random

# List Of Colors
colors = ["Red","Purple","Orange","Green","Yellow","Blue","Brown","Black","White"]

score = 0

timeleft = 60

# Function That Will Start the Game
def startGame(event):
    if timeleft == 60:

        # Start The CountDown
        countdown()
    
    # Run the Next Function to Select The Next Color
    nextColor()

# Function to Select and Display The Next Color
def nextColor():

    # Used The Globally declared 'Score' and 'timeleft' Variables
    global score    
    global timeleft

    # if game is Currently in play
    if timeleft > 0:

        # Make the text Entry Box active
        e.focus_set()

        # if Colored Type is Equal to Color text
        if e.get().lower() == colors[1].lower():
            score += 1
        
        # Clear the Entry of Text Box
        e.delete(0,tkinter.END)

        # shuffle the Colors
        random.shuffle(colors)

        # change the colour to type, by changing the
        #  text _and_ the colour to a random colour value
        label.config(fg = str(colors[1]),text = str(colors[0]))

        # Updating The Score
        scoreLabel.config(text = "SCORE: " + str(score))

def countdown():
    global timeleft

    if timeleft > 0:

        # decrement The Timer
        timeleft -= 1

        # Updatind the timeleft label
        timeLabel.config(text = "Time left: "
                               + str(timeleft))

        # Runnuning The Function after every 1 second
        timeLabel.after(1000,countdown)

root = tkinter.Tk()
  
# set the title
root.title("PIKACHU'S COLORGAME")
  
# set the size
root.geometry("375x200")
  
# add an instructions label
instructions = tkinter.Label(root, text = "Type in the colour"
                        " of the words, and not the word text!",
                                      font = ('Helvetica', 12))
instructions.pack() 
  
# add a score label
scoreLabel = tkinter.Label(root, text = "Press enter to start",
                                      font = ('Helvetica', 12))
scoreLabel.pack()
  
# add a time left label
timeLabel = tkinter.Label(root, text = "Time left: " +
              str(timeleft), font = ('Helvetica', 12))
                
timeLabel.pack()
  
# add a label for displaying the colours
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()
  
# add a text entry box for
# typing in colours
e = tkinter.Entry(root)
  
# run the 'startGame' function 
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()
  
# set focus on the entry box
e.focus_set()
  
# start the GUI
root.mainloop()

