#!/usr/bin/env python

"""

Merging JSON for CS3110 - OCaml
By: Austin Liu

"""
import json

trainer_json_final = {}

with open('trainer_template.json') as file1:
	json1 = json.load(file1)
	with open('trainer_template_2.json') as file2:
		json2 = json.load(file2)
		for key in json1.keys():
			white = json1[key]
			white2 = json2[key]
			white_ans = {}
			for key2 in white.keys():
				white_ans[key2] = white[key2] + white2[key2]
			trainer_json_final[key] = white_ans			

with open('trainer_template_merged.json', 'w') as trainer:
	json.dump(trainer_json_final, trainer, ensure_ascii=False,
	separators=(',', ': '), indent=4)	

print("success")