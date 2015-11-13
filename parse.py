#!/usr/bin/env python

"""

Parsing Cards for CS3110 - OCaml
By: Austin Liu

This bot is built to parse a json with cards into two lists,
black and white cards. In addition, it generates trainer_template.json
for actually recording data to train the bot.

"""
import json

#Lists of black and white cards
white = []
black = []

#Runs through all of the cards and splits into 2 different lists
with open('cards.json') as cards_file:
	card_list = json.load(cards_file)
	for card in card_list:
		if (card['numAnswers'] == 0 and card['expansion'] == 'Base'):
			white.append(card)
		elif (card['numAnswers']==1 and card['expansion'] == 'Base'):
			black.append(card)

#Dumps into files
with open('white.json', 'w') as white_list:
	json.dump(white, white_list, ensure_ascii=False,
	separators=(',', ': '), indent=4)

with open('black.json', 'w') as black_list:
	json.dump(black, black_list, ensure_ascii=False,
	separators=(',', ': '), indent=4)

#initialize trainer json file
trainer_json = {}
white_val = {}

for bcard in black:
	for wcard in white:
		white_val[wcard['text']] = 0
	trainer_json[bcard['text']] = white_val

with open('trainer_template.json', 'w') as trainer:
	json.dump(trainer_json, trainer, ensure_ascii=False,
	separators=(',', ': '), indent=4)	

print("success")