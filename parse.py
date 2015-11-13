#!/usr/bin/env python

"""

Parsing Cards for CS3110 - OCaml
By: Austin Liu

sdfsdfdsf

"""
import json

white = []
black = []

with open('cards.json') as cards_file:
	card_list = json.load(cards_file)
	for card in card_list:
		if card['numAnswers'] == 0:
			white.append(card)
		elif card['numAnswers']==1:
			black.append(card)

with open('white.json', 'w') as white_list:
	json.dump(white, white_list, ensure_ascii=True,
	separators=(',', ': '), indent=4)

with open('black.json', 'w') as black_list:
	json.dump(black, black_list, ensure_ascii=True,
	separators=(',', ': '), indent=4)

trainer_json = {}
white_val = []

for bcard in black:
	for wcard in white:
		temp_json = {}
		temp_json[wcard['text']] = 0
		white_val.append(temp_json)
	trainer_json[bcard['text']] = white_val

with open('trainer_template.json', 'w') as trainer:
	json.dump(trainer_json, trainer, ensure_ascii=True,
	separators=(',', ': '), indent=4)	

print("success")