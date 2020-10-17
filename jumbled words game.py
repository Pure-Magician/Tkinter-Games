#Finally the task has been completed
#so using comments now
#task of making a Gui based Jumbbled Game

import tkinter
from tkinter import *
import random
from tkinter import messagebox


#anwers of the jumbbled questions
answers = [
"python",
"java",
"swift",
"kotlin",
"india",
"russia",
"mumbai",
"delhi",
"sirohi",
"tokyo",
"cairo",
"italy",
]

#Jumbbled words
words = [
"nptohy",
"ajva",
"wfsit",
"ktloni",
"dniai",
"ssuari",
"mubiam",
"dlhei" ,
"rosiih",
"yotok",
"rocia",
"taliy"
]

#In-Built function for forwarding the jumbbled words
num =random.randrange(0,12,1)

#various functions used for buttons
def reset():
    global words, answers, num
    num = random.randrange(0, 12, 1)
    word.config(text=words [num])
    e1.delete(0, END)

def  default():
    global words , answers ,num
    word.config(text = words[num])

def checkans():
    global words, answers, num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Success","you are currect")
        reset()
    else:
        messagebox.showerror("Error" ,"This is not correct")
        e1.delete(0 ,END)





# basic outline
root = tkinter.Tk()

root.geometry("350x400+400+300")
root.title("Jumbbled Game")
root.configure(background="#000000")

word =Label(
    root,
    text= "you are here",
    font=("TImes New Roman",20),
    fg="white",
    bg="black"
)
word.pack(pady=15)

ans1 = StringVar()

#layout for entry
e1 = Entry(
    root,
    font =("Times New Roman",18),
    textvariable =ans1

)

e1.pack(ipady=5,ipadx=20)


#button layout
but =Button(
    root,
    text= "Check",
    fg="red",
    bg="blue",
    font=("Comic sans ms",18),
    width=10,
    relief = GROOVE,
    command = checkans
)
but.pack(pady=10)

butset= Button(
    root,
    text="Reset",
    fg="red",
    bg="blue",
    font=("Comic sans ms", 18),
    width=10,
    relief=GROOVE,
    command= reset
)
butset.pack(pady=10)
button3=Button(root,text="QUIT",fg="red",bg="blue",font=("Comic sans ms",18),command=root.quit)

button3.pack()
#function call for running the program

default()

root.mainloop()


# Creating Score Board
def creating_score_board(self):
    self.scoreboard = tkinter.Label(self, text="Score : {}".format(self.score))
    self.scoreboard.pack(anchor='n')
    return


# Updating Score Board
def update_score_board(self):
    self.score = self.score + 1
    self.scoreboard['text'] = "Score : {}".format(self.score)
