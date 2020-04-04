import random

# Different parts that make up a pack of tarot cards
major_arcana = {1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
suits = ["Swords", "Rods", "Coins", "Cups"]
court = ["King", "Queen", "Knight", "Page"]


# A dictionary containing different types of simple, linear, three card pulls
threec_spread_dict = {
    'Time': ['Past', 'Present', 'Future'],
    'Path' : ['You', 'Path', 'Potential'],
    'Relationship' : ['You', 'Relationship', 'Partner'],
    'Decision': ['Situation', 'Action', 'Outcome']}

# Function that lets a user choose between different spreads to learn different things
def choose_spread():
	print("What would you like to learn about?")
	print(threec_spread_dict.keys())
	user_spread = input("Choose your spread:")
	return user_spread

your_spread = {}

# Use random numbers to pull different cards
def build_spread(user_spread):
	for item in threec_spread_dict[user_spread]:
		your_spread[item] = major_arcana[random.randint(1,22)]
	return your_spread

#Format and print the spread
def print_spread():
	for aspect, card in your_spread.items():
		print("Your " + aspect + " is the " + card + " card.")


#user_spread = 'Decision'

#Run functions!
build_spread(choose_spread())
print_spread()

#The original function I wrote as part of the course
def simple_read():
	spread = {}
	spread["past"] = major_arcana[random.randint(1,22)]
	spread["present"] = major_arcana[random.randint(1,22)]
	spread["future"] = major_arcana[random.randint(1,22)]

	for aspect, card in spread.items():
		print("Your " + aspect + " is the " + card + " card.")


