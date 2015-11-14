#!/usr/bin/env python

"""

Bot Trainer for CS3110 - OCaml
By: Austin Liu

Used to train our bot for Cards Against Humanity

"""
from tkinter import *
import json
import random

#To intialize the actual application
root = Tk()
root.title("CS3110 Bot Trainer")

#intialize lists
t_list = {}
b_list = {}
w_list = {}
random_b = {}
list_of_random_items = []

#load data from jsons
with open('trainer_template.json') as trainer_list:
	t_list = json.load(trainer_list)

with open('black.json') as black_list:
	b_list = json.load(black_list)

with open('white.json') as white_list:
	w_list = json.load(white_list)

def updateScores1():
	t_list[random_b['text']][button1["text"]] +=1
	t_list[random_b['text']][button2["text"]] -=0.25
	t_list[random_b['text']][button3["text"]] -=0.25
	t_list[random_b['text']][button4["text"]] -=0.25
	t_list[random_b['text']][button5["text"]] -=0.25

def updateScores2():
	t_list[random_b['text']][button2["text"]] +=1
	t_list[random_b['text']][button1["text"]] -=0.25
	t_list[random_b['text']][button3["text"]] -=0.25
	t_list[random_b['text']][button4["text"]] -=0.25
	t_list[random_b['text']][button5["text"]] -=0.25

def updateScores3():
	t_list[random_b['text']][button3["text"]] +=1
	t_list[random_b['text']][button2["text"]] -=0.25
	t_list[random_b['text']][button1["text"]] -=0.25
	t_list[random_b['text']][button4["text"]] -=0.25
	t_list[random_b['text']][button5["text"]] -=0.25

def updateScores4():
	t_list[random_b['text']][button4["text"]] +=1
	t_list[random_b['text']][button2["text"]] -=0.25
	t_list[random_b['text']][button3["text"]] -=0.25
	t_list[random_b['text']][button1["text"]] -=0.25
	t_list[random_b['text']][button5["text"]] -=0.25

def updateScores5():
	t_list[random_b['text']][button5["text"]] +=1
	t_list[random_b['text']][button2["text"]] -=0.25
	t_list[random_b['text']][button3["text"]] -=0.25
	t_list[random_b['text']][button4["text"]] -=0.25
	t_list[random_b['text']][button1["text"]] -=0.25

def ButtonAct(input):
	updateScoreAct(input)
	print(t_list[random_b['text']][button1["text"]])
	print("You selected "+ list_of_random_items[0]["text"])
	listbox.insert(END, "button1 pressed")
	updateCards()

def updateScoreAct(input_num):
	reload()
	print(button[input_num]["text"])
	t_list[random_b['text']][button[input_num]["text"]] = t_list[random_b['text']][list_of_random_items[input_num]["text"]] + 1

def Button1():
	updateScores1()
	print(random_b['text'])
	print("You selected "+ button1["text"])
	listbox.insert(END, "button1 pressed")
	updateCards()

def Button2():
	updateScores2()
	print(random_b['text'])
	print("You selected "+ button2["text"])
	listbox.insert(END, "button2 pressed")
	updateCards()

def Button3():
	updateScores3()
	print(random_b['text'])
	print("You selected "+ button3["text"])
	listbox.insert(END, "button3 pressed")
	updateCards()

def Button4():
	updateScores4()
	print(random_b['text'])
	print("You selected "+ button4["text"])
	listbox.insert(END, "button4 pressed")
	updateCards()

def Button5():
	updateScores5()
	print(random_b['text'])
	print("You selected "+ button5["text"])
	listbox.insert(END, "button5 pressed")
	updateCards()

def drawRandBlack(b_list):
	# For random black
	return random.choice(b_list)

def drawRandWhite(w_list, num_to_select):
	# For random whites
	return random.sample(w_list, num_to_select)

def updateCards():
	with open('trainer_template.json', 'w') as trainer:
		json.dump(t_list, trainer, ensure_ascii=True,
		separators=(',', ': '), indent=4)

	list_of_random_items = drawRandWhite(w_list, 5)
	button1["text"] = list_of_random_items[0]["text"]
	button2["text"] = list_of_random_items[1]["text"]
	button3["text"] = list_of_random_items[2]["text"]
	button4["text"] = list_of_random_items[3]["text"]
	button5["text"] = list_of_random_items[4]["text"]

	random_b = drawRandBlack(b_list)

	black_card.delete(1.0, END)
	black_card.insert(END, random_b['text'])

#initalize
numOfOpts = 5
random_b = drawRandBlack(b_list)
list_of_random_items = drawRandWhite(w_list, numOfOpts)

black_card = Text(root, height = 2, width=80)

# button = []

# for temp_int in range(0,4):
# 	button[temp_int] = Button(root, text=list_of_random_items[temp_int]["text"], command = ButtonAct(temp_int))

button1 = Button(root, text=list_of_random_items[0]["text"], command = Button1)
button2 = Button(root, text=list_of_random_items[1]["text"], command = Button2)
button3 = Button(root, text=list_of_random_items[2]["text"], command = Button3)
button4 = Button(root, text=list_of_random_items[3]["text"], command = Button4)
button5 = Button(root, text=list_of_random_items[4]["text"], command = Button5)

listbox = Listbox(root)

black_card.insert(END, random_b['text'])

black_card.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
listbox.pack()

root.mainloop()