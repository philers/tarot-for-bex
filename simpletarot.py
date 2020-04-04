import random


tarot = {
	1:	"The Magician", 
	2:	"The High Priestess", 
	3:	"The Empress", 
	4:	"The Emperor", 
	5:	"The Hierophant", 
	6:	"The Lovers", 
	7:	"The Chariot", 
	8:	"Strength", 
	9:	"The Hermit", 
	10:	"Wheel of Fortune", 
	11:	"Justice", 
	12:	"The Hanged Man", 
	13:	"Death", 
	14:	"Temperance", 
	15:	"The Devil", 
	16:	"The Tower", 
	17:	"The Star", 
	18:	"The Moon", 
	19:	"The Sun", 
	20:	"Judgement", 
	21:	"The World", 
	22: "The Fool"}

spread = {}

spread["past"] = tarot[random.randint(1,22)]

spread["present"] = tarot[random.randint(1,22)]

spread["future"] = tarot[random.randint(1,22)]

for time, card in spread.items():
  print("Your " + time + " is the " + card + " card.")



threec_spread_dict = {
    'Timeline': ['Past', 'Present', 'Future'],
    'Path' : ['You', 'Your Path', 'Your Potential'],
    'Relationship' : ['You', 'Relationship', 'Partner'],
    'Decision': ['Situation', 'Action', 'Outcome']}
