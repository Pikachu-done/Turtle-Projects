from tkinter import *
from playsound import playsound
from gtts import gTTS

root = Tk()
root.geometry("350x300") 
root.configure(bg='ghost white')
root.title("TANISH'S - TEXT TO SPEECH")

Label(root,text = 'TEXT_TO_SPEECH',font = 'arial 20 bold',bg = 'white smoke').pack()

Msg = StringVar()

Label(root,text = 'Enter Text',font = 'arial 15 bold',bg = 'white smoke').place(x = 20,y = 60)

entry_field = Entry(root,textvariable = Msg, width = 50).place(x = 20, y = 100)

def Text_To_Speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Tanish.mp3')
    playsound('Tanish.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

Button(root,text = "PLAY",font = 'arial 15 bold',command = Text_To_Speech,width = '4').place(x = 25,y = 140)
Button(root,text = 'EXIT',font = 'arial 15 bold',bg = 'OrangeRed1',width = '4',command = Exit).palce(x=100,y=140)
Button(root,text = 'RESET',font = 'arial 15 bold',command = Reset,width = '6').place(x=175,y=140)

root.mainloop()