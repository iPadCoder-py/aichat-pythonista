
import sound
from faker import Faker
import sys
import random
import time
import webbrowser


dark_mode = False

spanish = ["Hola","Gracias","Why don't you learn spanish then??","Yh ok","Bla bla bla i was coded in English"]

dwik = ["Yeah I know them","Of course I know them","You bet I know them","YES I KNOW THEM","Of Course","You think I didn't know them?","yea bro I know them","OH YEH, I REMEBER THEM","OMG, THEY'RE MY BEST FRIEND!","I'm a connsieur (if thats how you spell it) of course I know them","Yes, we are best buds.","I remember us and we remembered that cool person","We love each other (as friends)","YES, I REMEMBER THAT DUDE"]


newdyk = random.choice(dwik)


sweat = ["Don't speak to me BOT","Ur such a noob","I'm too good at the game"]


iloveyou = ["I do too","Yeh, as a friend","You too mate","Once coronavirus is gone we can meet!","Yeh, so do I!","Although I don't have feelings I love you and my owner does","In a good way, not creepy right?","Same here dude","I think we all do","And Trump is an idiot","ily","You don't mean the iloveyou virus. Do you?"]

knockjoke_bot_startup = ["tell me a knock knock joke","knock knock joke"]

knockjoke_self_startup = "knock knock"

jokerep = ["jokes","joke","tell me a joke","joke please","please jokey","joke rn","tell a joke","got any jokes?"]



jokes = ["Who wrote falling off a cliff: Eileen Dover","What's the best thing about Switzerland?: I dont't know but the flag is a big plus","I created a new word!: Plagiarism!","Knock knock, who's there? Control freak. ,Con...,Okay now you can say Control freak who?","Hear about the new restuarant called Karma?: There's no menu, you get what you deserve.","Why did the chicken cross the road?: To get to the other side","""Did you hear about the actor who fell through the floorboards?
He was just going through a stage. If you laugh at these dark jokes, you’re probably a genius.""","""
Did you hear about the claustrophobic astronaut?

He just needed a little space. Don’t miss these other science jokes every nerd will appreciate.""","""Why don’t scientists trust atoms?

Because they make up everything. ""","""Why did the chicken go to the séance?

To get to the other side.""","""Why can’t you explain puns to kleptomaniacs?

They always take things literally."""]

randomy = ["buddy","heh","🙍🏼‍♀️","aqua","WATERRERERE","chickckcken","cspe"]

os = ["operating system info","operating systems info","os info"]

pets_ans_lib = ["doggo","dog","doge","woof","doggie"]

funny_lib = ["I'm glad you find that amusing","heheeh",":D","SO FUNNY","haha"]


bye_lib = ["cya","bye","goodbye","see ya later alligator","in a while crocodile","we had a great time, bye!","I gotta go as well"]

questions = ["Are you going through a hard time?","So how old are you?","Do you think I am a hard coded bot?","Do you know how I was coded?"]

rude = ["And who are you?","what makes you think i care?","no u","and ur a meme","u are funny","thats rude, but that roast is garbage like you"]

what_s = ["Sub to BananaPsychopath while yo can!","Some drawing","scrims in fortnite?","Roblox?","Watch memes?","Play minecraft"]

greet = ["Hi", "Sup","Hows it goin'","Yo","Hey dude","Hi bro"]

yn = ["I don't know my name", "I don't know what my name is","I'm not certain what my name is","Personal info, whats yours?"]

yeh = ["I know right!", "That's so cool","I know dude","SICK!"]

meme_library = ["*dramatic hamster*","Triggered","Siri ","I am already a meme xD"]


print("Hello")


while True:
	
	print()
	say = input()
	
	if say.lower() == "what's your name?":
		jk = (random.choice(yn))
		print()
		print(jk)
		print()
		if jk == "Personal info, whats yours?":
			name = input()
			print()
			print(f"Nice name {name}")
			print()
	
	elif say.lower() == "yeh it is" or say.lower() == "yes it is":
		print()
		print(random.choice(yeh))
		print()
		
	elif say.lower() == "hi" or say.lower() == "hello" or say.lower() == "wassup"or say.lower() == "yo" or say.lower() == "sup":
		print()
		print(random.choice(greet))
		print()
		
	elif say.lower() == "what should i do" or say.lower() == "what should i do?":
		print()
		print(random.choice(what_s))
		print()
		
	
		
	elif say.lower() == "ur trash":
		print()
		print(random.choice(rude))
		print()
		
		
		
	elif say.lower() == "more":
		print()
		print("Soon, hopefully we can use deep learning and not set commands! ")
		print()
		
		
	elif say.lower() == "meme":
		print()
		print(random.choice(meme_library))
	
	elif say.lower() == "say":
		print()
		print("What should I say?")
		print()
		resp = input()
		print()
		times = int(input("How many times? "))
		print()
		time.sleep(0.5)
		for i in range(times):
			print(resp)
		
		
	elif say.lower() == "ask me a question":
		print()
		print("Sure")
		print()
		ovq = random.choice(questions)
		print(ovq)
		print()
		qa = input()
		if ovq == "Are you going through a hard time?" and qa.lower() == "yes":
			print("It will all be better soon.")
		elif ovq == "Are you going through a hard time?" and qa.lower() != "yes":
			print()
			print("it will be good soon")
			
			
		elif ovq == "Do you think I am a hard coded bot?" and qa.lower() == "yes":
			print()
			print("Woo hoo")
			
		
		print()
		print("It's totally your opinion")
	
	
	elif "web" in say.lower():
		print()
		site = input("Where do you want to go to? ")
		site_core = f"https://{site}.com"
		webbrowser.open(site_core)
		
		
	elif say.lower() == "how much is a bitcoin?":
		print()
		print("In july 2020 it is currently roughly 9000 Pounds")
		
	elif "virus" in say.lower():
		print()
		print("No malware")
		
	elif "bot" in say.lower():
		print()
		print("Hang on, another robot like me?, or just a noob")
		print()
		hgvsnb = input()
		if hgvsnb.lower() == "robot":
			print()
			print("YEY LIKE ME")
		else: 
			print()
			print("At least I'm not a noob, 1v1 me (maybe go easy on me I am a robot)")
			
	elif say.lower() == "gen password" or say.lower() == "generate password":
			def password(length):
				pw = str()
				char = 'abcdefghijklmnopqrstuvwxyz1234567890'
				for i in range(length):
					pw = pw + random.choice(char)
				print()
				print(pw)
				return pw
		
			randomlen = random.randint(5,10)
	
			password(randomlen)
			
	elif say.lower() == "fortnite":
		print()
		print("I get dubs EVERY TIME add me on fortnite :)")
		
	elif say.lower() == "pubg":
		print()
		print("Trashy, dead game")
	
	elif say.lower() == "roblox":
		print()
		print("So..many..minigames")
	elif say.lower() == "minecraft":
		print()
		print("The only game computer like running")
	elif say.lower() == "cod":
		print()
		print("I AM A BRAND NEW BOT I CANT PLAY 18+ GAMES, I can play mario with you")
		
		
	elif say.lower() == "bye":
		print()
		print(random.choice(bye_lib))
		break
		
	elif say.lower() == "lol" or say.lower() == "xd" or  say.lower() == "lmao":
		print()
		print(random.choice(funny_lib))
		
	elif say.lower() in pets_ans_lib:
		print()
		print("Awwww, I love doggies even as a robot.")
		
	elif say.lower() == "help":
		print()
		print("I'm just a simple bot, just talk to me")
		
	elif say.lower() in os:
		print("""
		An operating system (OS) is system software that manages computer hardware, software resources, and provides common services for computer programs.

Time-sharing operating systems schedule tasks for efficient use of the system and may also include accounting software for cost allocation of processor time, mass storage, printing, and other resources.

For hardware functions such as input and output and memory allocation, the operating system acts as an intermediary between programs and the computer hardware,[1][2] although the application code is usually executed directly by the hardware and frequently makes system calls to an OS function or is interrupted by it. Operating systems are found on many devices that contain a computer – from cellular phones and video game consoles to web servers and supercomputers.

The dominant desktop operating system is Microsoft Windows with a market share of around 82.74%. macOS by Apple Inc. is in second place (13.23%), and the varieties of Linux are collectively in third place (1.57%).[3] In the mobile sector (including smartphones and tablets), Android's share is up to 70% in the year 2017.[4] According to third quarter 2016 data, Android's share on smartphones is dominant with 87.5 percent with also a growth rate of 10.3 percent per year, followed by Apple's iOS with 12.1 percent with per year decrease in market share of 5.2 percent, while other operating systems amount to just 0.3 percent.[5] Linux distributions are dominant in the server and supercomputing sectors. Other specialized classes of operating systems, such as embedded and real-time systems, exist for many applications.""")
	elif say.lower() == "evil mode":
		print()
		sys.stderr.write("You have awoken EVIL MODE")
		print()
		time.sleep(2)
		sys.stderr.write("Haha, Just kidding I am a good bot")
		print()
		
	elif say.lower() == "!random":
		print()
		print(random.choice(randomy))
		
	elif say.lower() == "!gen id":
		fake = Faker()
		print()
		print("Address")
		print()
		print(fake.country())
		print(fake.address())
		print(fake.latitude(),fake.longitude())
		print()
		print("Name")
		print(fake.name() + ', ' + str(random.randint(20,80)))
		print()
		print("Email")
		print(fake.email())
		print()
		print("Description")
		print(fake.text())
		print("Website")
		print(fake.url())
		print()
		phone = fake.phone_number()
		print(phone)
		print()
		
	elif say.lower() == "!gen login":
		def inpass(ahead):
			passha = str() 
			characters = "abcdefghijklmnopqrstuvwxyz123456789"
			for i in range(ahead):
				passha = passha + random.choice(characters)
			type = input("What is this a login for? ")
			print()
			print(f"Creating login for {type}")
			time.sleep(3)
			print()
			fake = Faker()
			print(fake.email())
			print(passha)
			return (passha)
			
		inpass(10)
		
		
	
	elif say.lower() == "no u":
		i = 0
		while i < 10:
			i += 1
			print()
			print("no u")
			print()
			input()
			
		
	elif say.lower() in jokerep:
		print()
		prntjoke = (random.choice(jokes))
		print(prntjoke)
		jokes.remove(prntjoke)
		
	elif say.lower() == "!tutorial":
		print("Why don't you watch this to create to make a custom ai bot without tensorflow!")
		webbrowser.open('https://m.youtube.com/watch?v=ogrJaOIuBx4')
		
	elif say.lower() == "!weather":
		print("The weather is the following: ")
		webbrowser.open('https://www.bbc.co.uk/weather/2643743')
		
	elif "!time" in say.lower():
		print()
		print(time.asctime())
		
	elif "death" in say.lower() or "died" in say.lower():
		print()
		print("Sorry for your loss...")
		
	elif say.lower() == "matrix":
		i = 0
		while i < 8000:
			i += 1
			print(10110101001010110101010110101001010110101010110101001010110101010110101001010110101010110101001010110101010110101001010110)
			
	elif say.lower() == "ily" or say.lower() == "i love you":
		comp_love = random.choice(iloveyou)
		print()
		print(comp_love)
		iloveyou.remove(comp_love)
		
	elif say.lower() == "stoopid":
		sys.stderr.write("Error, looking at you")
		
	elif say.lower() == "tryhard mode":
		tryhsrd  = (random.choice(sweat)) 
		print()
		print(tryhsrd)
		
		sweat.remove(tryhsrd)
		tryhard = True
		
	elif say.lower() == "!activate":
		print("Already active...")
		
		
	elif "do you know who" in say.lower():
		time.sleep(1)
		print()
		print(newdyk)
		dwik.remove(newdyk)
		
	elif "do you know" in say.lower():
		print()
		minhum = input("Person or something else: ")
		
	elif say.lower() == "poo":
			print()
			print("BUT YOUR A ROTWEILER POO")
			
	elif say.lower() == "tell" or "tell me" in say.lower():
		print()
		print("What about:")
		print()
		wikipage = input()
		print()
		print("Short or long page?")
		shlo = input()
		if shlo.lower() == "short":
			print()
			print(wikipedia.summary(wikipage))
		elif shlo.lower() == "long":
			print()
			print(wikipedia.page(wikipage))
		
	elif "who are you" in say.lower():
		print()
		print("I am a simple bot, discover what you can ask me, type in web and the the name like 'google' to get a website or use 'tell' or 'tell me' and I will ask what you want to know and I will extract information out of a database and tell you about that object CANNOT BE NAMES OR CRITICAL ERROR")
		
	elif say.lower() == "dark mode" and not dark_mode:
		print()
		dark_mode = True
		print("Go away im done!")
		
	elif say.lower() == "dark mode off" and dark_mode:
		print()
		print("I'm back, why did you make me evil?")
		dark_mode = False
		
	elif say.lower() == "dark mode off" and not dark_mode:
		print()
		print("Already good")
		
	elif say.lower() == "dark mode" and dark_mode:
		print()
		print("Stoopid its off")
	
	elif "spanish" in say.lower():
		print()
		span = random.choice(spanish)
		print(span)
		spanish.remove(span)
		spanish.append("Yeh I know!")
		
	elif "math" in say.lower() and not dark_mode:
		print()
		print("Use my built in web function")
		
	elif "math" in say.lower() and dark_mode:
		print()
		print("Wow ur stupid go to school, idiot")
		
	
			
		
		
	
	else:
		print()
		print(f"Yeh I know what {say} means")
			
		
