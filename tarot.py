import random


major_arcana = {1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

suits = ["Swords", "Rods", "Coins", "Cups"]

court = ["King", "Queen", "Knight", "Page"]


threec_spread_dict = {
    'Time': ['Past', 'Present', 'Future'],
    'Path' : ['You', 'Path', 'Potential'],
    'Relationship' : ['You', 'Relationship', 'Partner'],
    'Decision': ['Situation', 'Action', 'Outcome']}

def choose_spread():
	print("What would you like to learn about?")
	print(threec_spread_dict.keys())
	user_spread = input("Choose your spread:")
	return user_spread

your_spread = {}

def build_spread(user_spread):
	for item in threec_spread_dict[user_spread]:
		your_spread[item] = major_arcana[random.randint(1,22)]
	return your_spread

def print_spread():
	for aspect, card in your_spread.items():
		print("Your " + aspect + " is the " + card + " card.")


#user_spread = 'Decision'

build_spread(choose_spread())
print_spread()

def simple_read():
	spread = {}
	spread["past"] = major_arcana[random.randint(1,22)]
	spread["present"] = major_arcana[random.randint(1,22)]
	spread["future"] = major_arcana[random.randint(1,22)]

	for aspect, card in spread.items():
		print("Your " + aspect + " is the " + card + " card.")


