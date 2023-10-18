# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:09:35 2023

@author: charl
"""

import tkinter as tk
import random

"""
User selects range
System picks int within range
dUser guesses int in minimum number of guesses

"""

#Creating window for the game

main = tk.Tk()
main.geometry("600x200")
main.title("Random Number Guesser Game")

#setting tkinter typsets
lowerRange = tk.IntVar()
upperRange = tk.IntVar()
userChoice = tk.IntVar()

#Defining global variables
USER_GUESSES = 0
TOTAL_GUESSES = 0
compChoice = 0
    
app = ''

def showGuess():
  global app
  class ResultLabel():
    def __init__(self):
      self.text = tk.StringVar()
      self.text.set("Make your guess in the box above")
      self.label = tk.Label(main, textvariable=self.text)
      self.label.grid(column=0,row=3)
      self.button = tk.Button(main, text = "Guess", command = self.pick)
      self.button.grid(column = 2, row = 2)
      self.entryG = tk.Entry(main,width=10)
      self.entryG.grid(column=0,row=2)
      self.entryG.focus()
      self.text.set("")

    def pick(self):
      global upperRange
      global lowerRange
      global compChoice
      global USER_GUESSES
      global TOTAL_GUESSES
      userChoice = int(self.entryG.get())
      USER_GUESSES+=1
      info.update()
      def win():
        self.text.set("Congratulations, you guessed the correct number!")
        #todo - add winning screen
        self.entryG['state'] = tk.DISABLED
        self.button['state'] = tk.DISABLED
      def higher():
        self.text.set("Incorrect! Your guess is too high.")
      def lower():
        self.text.set("Incorrect! Your guess is too low.")
        print(compChoice)
      def lose():
        self.text.set("You lost! Better luck next time!")
        self.entryG['state'] = tk.DISABLED
        self.button['state'] = tk.DISABLED
      if userChoice == compChoice:
        win()
      elif USER_GUESSES == TOTAL_GUESSES:
        lose()
      elif userChoice > compChoice:
        higher()
      elif userChoice < compChoice:
          lower()  
        
  if app == '':
    app=ResultLabel()
  else:
    app.text.set("")
    app=ResultLabel()
    
  
####add something in here for exceeding the guess limit
  
  

class GameInfo():
  def __init__(self):
    self.label1 = tk.Label(main, text = "Input the number range below:")
    self.label1.grid(column = 0, row = 0)

    self.entry1 = tk.Entry(main,width=10)
    self.entry1.grid(column=0,row=1)
    self.entry1.focus()

    self.entry2 = tk.Entry(main,width=10)
    self.entry2.grid(column=1,row=1)
    
    self.text = tk.StringVar()
    self.text.set(" ")
    self.box = tk.Text(main, height= 3, width = 24, bg = "grey")
    self.box.grid(column = 3, row = 1)
    
    self.button = tk.Button(main, text = "Submit", command = self.submit)
    self.button.grid(column = 2, row = 1)
    
  def changeinfo(self):
    pass
  
  def update(self):
    global USER_GUESSES
    global TOTAL_GUESSES
    global lowerRange
    global upperRange
    ranges = (
      "Number Range: {lr} to {ur} \nGuesses Allowed: {tg} \nGuesses        : {cg}"
      .format(lr=lowerRange,ur=upperRange,tg=TOTAL_GUESSES,cg = USER_GUESSES)
      )
    self.box.delete("1.0",tk.END)
    self.box.insert(tk.END,ranges)
    
  
  def submit(self):
    
    global USER_GUESSES
    USER_GUESSES = 0
    global TOTAL_GUESSES
    global compChoice
    global lowerRange
    global upperRange
    lowerRange = int(info.entry1.get())
    upperRange = int(info.entry2.get())
    if lowerRange < upperRange:
      TOTAL_GUESSES = int(((upperRange - lowerRange) / 2) + 1)
      self.update()
      showGuess()
      compChoice = random.randint(int(lowerRange),int(upperRange))
    else:
      print("That doesn't seem right, pick two whole numbers, with the smaller in the first box")
    
  
info = GameInfo()

main.mainloop()