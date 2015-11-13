#!/usr/bin/env python

"""

Bot Trainer for CS3110 - OCaml
By: Austin Liu

sdfsdfdsf

"""
from tkinter import *
import json
import random

root = Tk()
root.title("CS3110 Bot Trainer")

with open('trainer_template.json') as trainer_list:
	t_list = json.load(trainer_list)

with open('black.json') as black_list:
	b_list = json.load(black_list)

with open('white.json') as white_list:
	w_list = json.load(white_list)

def updateScores():
	t_list[black_card.get(1.0,END)][button1["text"]] = t_list[black_card.get(1.0,END)][button1["text"]] + 1

def Button1():
	updateCards()
	listbox.insert(END, "button1 pressed")

def Button2():
	updateCards()
	listbox.insert(END, "button2 pressed")

def Button3():
	updateCards()
	listbox.insert(END, "button3 pressed")

def Button4():
	updateCards()
	listbox.insert(END, "button4 pressed")

def Button5():
	updateCards()
	listbox.insert(END, "button5 pressed")

def drawRandBlack(b_list):
	# For random black
	return random.choice(b_list)

def drawRandWhite(w_list, num_to_select):
	# For random whites
	return random.sample(w_list, num_to_select)

def updateCards():
	newList = drawRandWhite(w_list, 5)
	button1["text"] = newList[0]["text"]
	button2["text"] = newList[1]["text"]
	button3["text"] = newList[2]["text"]
	button4["text"] = newList[3]["text"]
	button5["text"] = newList[4]["text"]
	black_card.delete(1.0, END)
	black_card.insert(END, drawRandBlack(b_list)['text'])

random_b = drawRandBlack(b_list)
list_of_random_items = drawRandWhite(w_list, 5)

black_card = Text(root, height = 2, width=30)

button1 = Button(root, text=list_of_random_items[0]["text"], command = Button1)
button2 = Button(root, text=list_of_random_items[1]["text"], command = Button2)
button3 = Button(root, text=list_of_random_items[2]["text"], command = Button3)
button4 = Button(root, text=list_of_random_items[3]["text"], command = Button4)
button5 = Button(root, text=list_of_random_items[4]["text"], command = Button5)

scrollbar = Scrollbar(root, orient=VERTICAL)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

black_card.insert(END, random_b['text'])

black_card.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
listbox.pack()
scrollbar.pack()

root.mainloop()