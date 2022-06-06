import random
from tkinter import *

root = Tk()
root.title("Data Flair - Rock , Paper and Scissor")
root.resizable(0,0)
root.config(bg ='seashell3')
root.geometry("400x400")

Label(root, text = "Rock, Paper, Scissors", font = 'arial 20 bold', bg = 'seashell3').pack()

user_take = StringVar()
Label(root, text = "Select any one - 'Rock, Paper, Scissor'", font = 'arial 15 bold', bg = 'seashell2').place(x = 20, y = 70)
Entry(root, textvariable = user_take, font = 'arial 15', bg = 'antiquewhite2').place(x = 90, y = 130)

comp_pick = random.randint(1,3)
if comp_pick == '1':
    comp_pick = 'rock'
elif comp_pick == '2':
    comp_pick = 'paper' 
else:
    comp_pick = 'scissors'

Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('Its a Tie! Both Selected the Same!') 
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('You Lose! Computer Selected Paper!') 
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('You Win! Computer Selected Scissor!') 
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('You Lose,Computer Selected Scissor')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('You Win, Computer Select Rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('You Loose,  Computer Select Rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('You Win , Computer Select Paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')
    
def Reset():
    Result.set("")
    user_take.set("")

def Exit():
    root.destroy()

Entry(root, textvariable = Result, font = 'arial 10 bold', bg = 'antiquewhite2', width = 40).place(x = 25 , y = 250)

Button(root,text = "PLAY", font = 'arial 13 bold', bg = 'seashell4', padx = 5, command = play).place(x = 150 , y = 190)

Button(root, text = "RESET", font = 'arial 13 bold', bg = 'seashell4', padx = 5, command = Reset).place(x=70, y=310)

Button(root, text = "EXIT", font = 'arial 13 bold' , bg = 'seashell4' , padx = 5, command = Exit).place(x = 230, y = 310)

root.mainloop()