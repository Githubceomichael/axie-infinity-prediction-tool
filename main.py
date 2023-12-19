#-------------------------------------------------------------------------------------------------------------#

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

#-------------------------------------------------------------------------------------------------------------#

cards = ['Blackmail', 'Spike Throw', 'Cleanse Scent', 'All-out Shot', 'Nile Strike', 'Ivory Chop', 'Anesthetic Bait', 'Acrobatic', 'Spinal Tap', 'Disarm', 'Refresh', 'Surprise Invasion', 'Critical Escape', 'Grub Surprise', 'Sticky Goo', 'Star Shuriken', 'Shelter', 'Chomp', 'Peace Treaty', 'Eggbomb', 'Piercing Sound', 'Swallow', 'Shipwreck', 'Swift Escape', 'Vegetal Bite', 'Slippery Shield', 'Wooden Stab', 'Drain Bite', 'Blood Taste', 'Allergic Reaction', 'Angry Lam', 'Spicy Surprise', 'Leek Leak', 'Seed Bullet', 'Bug Splat', 'Bug Noise', 'Cool Breeze', 'Feather Lunge', 'Nitro Leap', 'Flanking Smack', 'Water Sphere', 'Black Bubble', 'Hare Dagger', 'Balloon Pop', 'Sugar Rush', 'Aquaponics', 'Aqua Vitality', 'Dull Grip', 'Sinister Strike', 'Rampant Howl', 'Neuro Toxin', 'Soothing Song', 'Deep Sea Gore', 'Scarab Curse', 'Prickly Trap', 'Early Bird', 'Nut Throw', 'Nut Crack', 'Scale Dart', 'Tiny Catapult', 'Scaly Lunge', 'Aqua Deflect', 'Carrot Hammer', 'Vegan Diet', 'Bamboo Clan', 'October Treat', 'Terror Chomp', 'Third Glance', 'Barb Strike', 'Puffy Smack', 'Insectivore', 'Headshot', 'Air Force One', 'Ill-omened', 'Heart Break', 'Merry Legion', 'Branch Charge', 'Woodman Power', 'Revenge Arrow', 'Crimson Water', 'Heros Bane', 'Clam Slash', 'Shell Jab', 'Scale Dart (Aqua)', 'Sunder Armor', 'Tail Slap', 'Dark Swoop', 'Triple Threat', 'Night Steal', 'Self Rally', 'Single Combat', 'Why So Serious', 'Kotaro bite', 'Sneaky Raid', 'Healing Aroma', 'Shrooms Grace', 'Turnip Rocket', 'Disguise', 'Bug Signal', 'Mystic Rush', 'Smart Shot', 'Gerbil Jump', 'Chitin Jump', 'Upstream Swim', 'Fish Hook', 'Death Mark', 'Ivory Stab', 'Bulkwark', 'Patient Hunter', 'Juggling Balls', 'Overgrow Keratin', 'Aqua Stock', 'Venom Spray', 'Cockadoodledoo', 'Luna Absorb', 'Tiny Swing', 'Poo Fling', 'Chemical Warfare', 'Buzzing Wind', 'Forest Spirit', 'Risky Feather', 'Cattail Slap', 'Grub Explode', 'Heroic Reward', 'Vine Dagger', 'Mite Bite', 'Jar Barrage', 'Gas Unleash', 'Numbing Lecretion', 'Twin Needle', 'Sunder Claw', 'Sweet Party']

oneEnergyCards = ['Blackmail', 'Spike Throw', 'Nile Strike', 'Ivory Chop', 'Anesthetic Bait', 'Acrobatic', 'Spinal Tap', 'Disarm', 'Surprise Invasion', 'Critical Escape', 'Grub Surprise', 'Sticky Goo', 'Star Shuriken', 'Shelter', 'Chomp', 'Peace Treaty', 'Eggbomb', 'Piercing Sound', 'Swallow', 'Shipwreck', 'Swift Escape', 'Vegetal Bite', 'Slippery Shield', 'Wooden Stab', 'Drain Bite', 'Blood Taste', 'Allergic Reaction', 'Angry Lam', 'Spicy Surprise', 'Leek Leak', 'Seed Bullet', 'Bug Splat', 'Bug Noise', 'Cool Breeze', 'Feather Lunge', 'Nitro Leap', 'Flanking Smack', 'Water Sphere', 'Black Bubble', 'Hare Dagger', 'Sugar Rush', 'Aquaponics', 'Aqua Vitality', 'Dull Grip', 'Sinister Strike', 'Rampant Howl', 'Neuro Toxin', 'Soothing Song', 'Deep Sea Gore', 'Scarab Curse', 'Prickly Trap', 'Early Bird', 'Nut Throw', 'Nut Crack', 'Scale Dart', 'Tiny Catapult', 'Scaly Lunge', 'Aqua Deflect', 'Carrot Hammer', 'Vegan Diet', 'Bamboo Clan', 'October Treat', 'Terror Chomp', 'Third Glance', 'Barb Strike', 'Puffy Smack', 'Insectivore', 'Headshot', 'Air Force One', 'Ill-omened', 'Heart Break', 'Merry Legion', 'Branch Charge', 'Woodman Power', 'Revenge Arrow', 'Crimson Water', 'Heros Bane', 'Clam Slash', 'Shell Jab', 'Scale Dart (Aqua)', 'Sunder Armor', 'Dark Swoop', 'Night Steal', 'Single Combat', 'Why So Serious', 'Kotaro bite', 'Sneaky Raid', 'Healing Aroma', 'Shrooms Grace', 'Turnip Rocket', 'Bug Signal', 'Smart Shot', 'Gerbil Jump', 'Chitin Jump', 'Upstream Swim', 'Fish Hook', 'Death Mark', 'Ivory Stab', 'Bulkwark', 'Patient Hunter', 'Juggling Balls', 'Overgrow Keratin', 'Aqua Stock', 'Tiny Swing', 'Poo Fling', 'Chemical Warfare', 'Forest Spirit', 'Risky Feather', 'Jar Barrage', 'Gas Unleash', 'Numbing Lecretion']

noEnergyCards = ['Cleanse Scent', 'All-out Shot', 'Refresh', 'Balloon Pop', 'Tail Slap', 'Triple Threat', 'Self Rally', 'Disguise', 'Mystic Rush', 'Venom Spray', 'Cockadoodledoo', 'Luna Absorb', 'Buzzing Wind', 'Cattail Slap', 'Grub Explode', 'Heroic Reward', 'Vine Dagger', 'Mite Bite', 'Twin Needle']

twoEnergyCards = ['Sunder Claw', 'Sweet Party']

#-------------------------------------------------------------------------------------------------------------#

window = Tk()
window.title("Axie Prediction Tool")
window.geometry("600x650")

#-------------------------------------------------------------------------------------------------------------#

title = Frame(window)
title.pack(side=TOP, pady=15)

logo = Canvas(title, width=80, height=100)
logo.grid(row=0, column=0)
img = Image.open()
resized_image= img.resize((90,90), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
logo.create_image(0, 0, anchor=NW, image=new_image)


titleLabel = Frame(title)
titleLabel.grid(row=0, column=1)

mainTitle = Label(titleLabel, text="Axie")
mainTitle.pack(side=TOP)

subTitle = Label(titleLabel, text="Axie Prediction Tool")
subTitle.pack(side=TOP)

footerTitle = Label(titleLabel, text="© 2021 volantebjb")
footerTitle.pack(side=TOP)

round = Frame(window)
round.pack()

roundCountTitle = Frame(round)
roundCountTitle.pack(side=TOP)

roundCountLabel = Label(roundCountTitle, text="Round")
roundCountLabel.pack(side=TOP)

roundCountButtons = Frame(round)
roundCountButtons.pack(side=BOTTOM, pady=3)

roundCount = 1

def subtractRound():
    global roundCount
    roundCount = roundCount - 1
    roundCounter.delete(0, END)
    roundCounter.insert(END, roundCount)

    subtractOpponentEnergy()
    subtractOpponentEnergy()

    subtractOpponentOnHand()
    subtractOpponentOnHand()
    subtractOpponentOnHand()

    if roundCount == 2:
        addOpponentOnDeck()
        addOpponentOnDeck()
        addOpponentOnDeck()
        addOpponentOnDeck()
        addOpponentOnDeck()
        addOpponentOnDeck()

    else: 
        addOpponentOnDeck()
        addOpponentOnDeck()
        addOpponentOnDeck()

def addRound():
    global roundCount
    roundCount = roundCount + 1
    roundCounter.delete(0, END)
    roundCounter.insert(END, roundCount)

    addOpponentEnergy()
    addOpponentEnergy()
    addOpponentOnHand()
    addOpponentOnHand()
    addOpponentOnHand()

    if roundCount == 2:

        subtractOpponentOnDeck()
        subtractOpponentOnDeck()
        subtractOpponentOnDeck()
        subtractOpponentOnDeck()
        subtractOpponentOnDeck()
        subtractOpponentOnDeck()

    else: 
        subtractOpponentOnDeck()
        subtractOpponentOnDeck()
        subtractOpponentOnDeck()

subtractRoundButton = Button(roundCountButtons, text="-", command=subtractRound, width=2)
subtractRoundButton.grid(row=0, column=0)

roundCounter = Entry(roundCountButtons, width=5, justify = CENTER)
roundCounter.insert(END, roundCount)
roundCounter.grid(row=0, column=1, padx=10)

addRoundButton = Button(roundCountButtons, text="+", command=addRound, width=2)
addRoundButton.grid(row=0, column=2)

#-------------------------------------------------------------------------------------------------------------#
'''
player = Frame(window)
player.pack(pady=5)

playerTitle = Frame(player)
playerTitle.pack()

playerLabel = Label(playerTitle, text="Player")
playerLabel.grid(row=0, column=0, padx=30)

#----------------------------------#

playerButtons = Frame(player)
playerButtons.pack(pady=5)

#----------------------------------#

newPlayerDeckButton = Button(playerButtons, text="New Deck")
newPlayerDeckButton.grid(row=0, column=0, padx=3)

resetPlayerDeckButton = Button(playerButtons, text="Reset Deck")
resetPlayerDeckButton.grid(row=0, column=1, padx=3)

deletePlayerACardsButton = Button(playerButtons, text="Disable Plant")
deletePlayerACardsButton.grid(row=0, column=2, padx=3)

deletePlayerBCardsButton = Button(playerButtons, text="Disable Beast")
deletePlayerBCardsButton.grid(row=0, column=3, padx=3)

deletePlayerCCardsButton = Button(playerButtons, text="Disable Aqua")
deletePlayerCCardsButton.grid(row=0, column=4, padx=3)

#----------------------------------#

playerA1 = Frame(player)
playerA1.pack(pady=5)

playerA1Title = Frame(playerA1)
playerA1Title.grid(row=0, column=0, padx=30)

playerA1Label = Label(playerA1Title, text="Plant")
playerA1Label.grid(row=0, column=0, padx=30)

playerA1Cards = Frame(playerA1)
playerA1Cards.grid(row=1, column=0, padx=30)

#----------------------------------#

playerA11 = Frame(playerA1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
playerA11.grid(row=1, column=0, padx=5, pady=5)

playerA11Title = Frame(playerA11, width=70, height=40)
playerA11Title.grid(row=0, column=0)

playerA11Label = Label(playerA11Title, text="Vegetal Bite")
playerA11Label.grid(row=0, column=0)

playerA11Buttons = Frame(playerA11, width=70, height=40)
playerA11Buttons.grid(row=1, column=0, padx=5, pady=5)

playerA11B1V = IntVar()
playerA11B1 = Checkbutton(playerA11Buttons, variable=playerA11B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA11B1.grid(row=1, column=0)
  
playerA11B2V = IntVar()
playerA11B2 = Checkbutton(playerA11Buttons, variable=playerA11B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA11B2.grid(row=1, column=1) 

playerA11B3V = IntVar()
playerA11B3 = Checkbutton(playerA11Buttons, variable=playerA11B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA11B3.grid(row=1, column=2) 

playerA11B4V = IntVar()
playerA11B4 = Checkbutton(playerA11Buttons, variable=playerA11B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA11B4.grid(row=1, column=3) 

#----------------------------------#
 
playerA12 = Frame(playerA1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
playerA12.grid(row=1, column=1, padx=5, pady=5)

playerA12Title = Frame(playerA12, width=70, height=40)
playerA12Title.grid(row=0, column=0)

playerA12Label = Label(playerA12Title, text="Prickly Trap")
playerA12Label.grid(row=0, column=0)

playerA12Buttons = Frame(playerA12, width=70, height=40)
playerA12Buttons.grid(row =1, column=0, padx=5, pady=5)

playerA12B1V = IntVar()
playerA12B1 = Checkbutton(playerA12Buttons, variable=playerA12B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA12B1.grid(row=0, column=0)

playerA12B2V = IntVar()
playerA12B2 = Checkbutton(playerA12Buttons, variable=playerA12B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA12B2.grid(row=0, column=1) 

playerA12B3V = IntVar()
playerA12B3 = Checkbutton(playerA12Buttons, variable=playerA12B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA12B3.grid(row=0, column=2) 

playerA12B4V = IntVar()
playerA12B4 = Checkbutton(playerA12Buttons, variable=playerA12B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA12B4.grid(row=0, column=3) 

playerA13 = Frame(playerA1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
playerA13.grid(row=1, column=2, padx=5, pady=5)

#----------------------------------#

playerA13Title = Frame(playerA13, width=70, height=40)
playerA13Title.grid(row=0, column=0)

playerA13Label = Label(playerA13Title, text="October Treat")
playerA13Label.grid(row=0, column=0)

playerA13Buttons = Frame(playerA13, width=70, height=40)
playerA13Buttons.grid(row =1, column=0, padx=5, pady=5)

playerA13B1V = IntVar()
playerA13B1 = Checkbutton(playerA13Buttons, variable=playerA13B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA13B1.grid(row=0, column=0)

playerA13B2V = IntVar()
playerA13B2 = Checkbutton(playerA13Buttons, variable=playerA13B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA13B2.grid(row=0, column=1) 

playerA13B3V = IntVar()
playerA13B3 = Checkbutton(playerA13Buttons, variable=playerA13B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA13B3.grid(row=0, column=2) 

playerA13B4V = IntVar()
playerA13B4 = Checkbutton(playerA13Buttons, variable=playerA13B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA13B4.grid(row=0, column=3) 

#----------------------------------#

playerA14 = Frame(playerA1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
playerA14.grid(row=1, column=3, padx=5, pady=5)

playerA14Title = Frame(playerA14, width=70, height=40)
playerA14Title.grid(row=0, column=0)

playerA14Label = Label(playerA14Title, text="Carrot Hammer")
playerA14Label.grid(row=0, column=0)

playerA14Buttons = Frame(playerA14, width=70, height=40)
playerA14Buttons.grid(row =1, column=0, padx=5, pady=5)

playerA14B1V = IntVar()
playerA14B1 = Checkbutton(playerA14Buttons, variable=playerA14B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA14B1.grid(row=0, column=0)

playerA14B2V = IntVar()
playerA14B2 = Checkbutton(playerA14Buttons, variable=playerA14B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA14B2.grid(row=0, column=1) 

playerA14B3V = IntVar()
playerA14B3 = Checkbutton(playerA14Buttons, variable=playerA14B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA14B3.grid(row=0, column=2) 

playerA14B4V = IntVar()
playerA14B4 = Checkbutton(playerA14Buttons, variable=playerA14B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerA14B4.grid(row=0, column=3) 

#----------------------------------------------------------------#

playerB1 = Frame(player)
playerB1.pack(pady=5)

playerB1Title = Frame(playerB1)
playerB1Title.grid(row=0, column=0, padx=30)

playerB1Label = Label(playerB1Title, text="Beast")
playerB1Label.grid(row=0, column=0, padx=30)

playerB1Cards = Frame(playerB1)
playerB1Cards.grid(row=1, column=0, padx=30)

playerB11 = Frame(playerB1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
playerB11.grid(row=1, column=0, padx=5, pady=5)

playerB11Title = Frame(playerB11, width=70, height=40)
playerB11Title.grid(row=0, column=0)

playerB11Label = Label(playerB11Title, text="Piercing Sound")
playerB11Label.grid(row=0, column=0)

playerB11Buttons = Frame(playerB11, width=70, height=40)
playerB11Buttons.grid(row =1, column=0, padx=5, pady=5)

playerB11B1V = IntVar()
playerB11B1 = Checkbutton(playerB11Buttons, variable=playerB11B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB11B1.grid(row=0, column=0)

playerB11B2V = IntVar()
playerB11B2 = Checkbutton(playerB11Buttons, variable=playerB11B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB11B2.grid(row=0, column=1) 

playerB11B3V = IntVar()
playerB11B3 = Checkbutton(playerB11Buttons, variable=playerB11B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB11B3.grid(row=0, column=2) 

playerB11B4V = IntVar()
playerB11B4 = Checkbutton(playerB11Buttons, variable=playerB11B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB11B4.grid(row=0, column=3) 

#----------------------------------#
 
playerB12 = Frame(playerB1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
playerB12.grid(row=1, column=1, padx=5, pady=5)

playerB12Title = Frame(playerB12, width=70, height=40)
playerB12Title.grid(row=0, column=0)

playerB12Label = Label(playerB12Title, text="Ivory Stab")
playerB12Label.grid(row=0, column=0)

playerB12Buttons = Frame(playerB12, width=70, height=40)
playerB12Buttons.grid(row =1, column=0, padx=5, pady=5)

playerB12B1V = IntVar()
playerB12B1 = Checkbutton(playerB12Buttons, variable=playerB12B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB12B1.grid(row=0, column=0)

playerB12B2V = IntVar()
playerB12B2 = Checkbutton(playerB12Buttons, variable=playerB12B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB12B2.grid(row=0, column=1) 

playerB12B3V = IntVar()
playerB12B3 = Checkbutton(playerB12Buttons, variable=playerB12B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB12B3.grid(row=0, column=2) 

playerB12B4V = IntVar()
playerB12B4 = Checkbutton(playerB12Buttons, variable=playerB12B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB12B4.grid(row=0, column=3) 

#----------------------------------#

playerB13 = Frame(playerB1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
playerB13.grid(row=1, column=2, padx=5, pady=5)

playerB13Title = Frame(playerB13, width=70, height=40)
playerB13Title.grid(row=0, column=0)

playerB13Label = Label(playerB13Title, text="SIngle Combat")
playerB13Label.grid(row=0, column=0)

playerB13Buttons = Frame(playerB13, width=70, height=40)
playerB13Buttons.grid(row =1, column=0, padx=5, pady=5)

playerB13B1V = IntVar()
playerB13B1 = Checkbutton(playerB13Buttons, variable=playerB13B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB13B1.grid(row=0, column=0)

playerB13B2V = IntVar()
playerB13B2 = Checkbutton(playerB13Buttons, variable=playerB13B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB13B2.grid(row=0, column=1) 

playerB13B3V = IntVar()
playerB13B3 = Checkbutton(playerB13Buttons, variable=playerB13B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB13B3.grid(row=0, column=2) 

playerB13B4V = IntVar()
playerB13B4 = Checkbutton(playerB13Buttons, variable=playerB13B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB13B4.grid(row=0, column=3) 

#----------------------------------#

playerB14 = Frame(playerB1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
playerB14.grid(row=1, column=3, padx=5, pady=5)

playerB14Title = Frame(playerB14, width=70, height=40)
playerB14Title.grid(row=0, column=0)

playerB14Label = Label(playerB14Title, text="Luna Absorb")
playerB14Label.grid(row=0, column=0)

playerB14Buttons = Frame(playerB14, width=70, height=40)
playerB14Buttons.grid(row =1, column=0, padx=5, pady=5)

playerB14B1V = IntVar()
playerB14B1 = Checkbutton(playerB14Buttons, variable=playerB14B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB14B1.grid(row=0, column=0)

playerB14B2V = IntVar()
playerB14B2 = Checkbutton(playerB14Buttons, variable=playerB14B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB14B2.grid(row=0, column=1) 

playerB14B3V = IntVar()
playerB14B3 = Checkbutton(playerB14Buttons, variable=playerB14B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB14B3.grid(row=0, column=2) 

playerB14B4V = IntVar()
playerB14B4 = Checkbutton(playerB14Buttons, variable=playerB14B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerB14B4.grid(row=0, column=3) 


#-------------------------------------------------------------------------------------------------------------#

playerC1 = Frame(player)
playerC1.pack(pady=5)

playerC1Title = Frame(playerC1)
playerC1Title.grid(row=0, column=0, padx=30)

playerC1Label = Label(playerC1Title, text="Aquatic")
playerC1Label.grid(row=0, column=0, padx=30)

playerC1Cards = Frame(playerC1)
playerC1Cards.grid(row=1, column=0, padx=30)

#----------------------------------#

playerC11 = Frame(playerC1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
playerC11.grid(row=1, column=0, padx=5, pady=5)

playerC11Title = Frame(playerC11, width=70, height=40)
playerC11Title.grid(row=0, column=0)

playerC11Label = Label(playerC11Title, text="Risky Fish")
playerC11Label.grid(row=0, column=0)

playerC11Buttons = Frame(playerC11, width=70, height=40)
playerC11Buttons.grid(row =1, column=0, padx=5, pady=5)

playerC11B1V = IntVar()
playerC11B1 = Checkbutton(playerC11Buttons, variable=playerC11B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC11B1.grid(row=0, column=0)

playerC11B2V = IntVar()
playerC11B2 = Checkbutton(playerC11Buttons, variable=playerC11B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC11B2.grid(row=0, column=1) 

playerC11B3V = IntVar()
playerC11B3 = Checkbutton(playerC11Buttons, variable=playerC11B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC11B3.grid(row=0, column=2) 

playerC11B4V = IntVar()
playerC11B4 = Checkbutton(playerC11Buttons, variable=playerC11B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC11B4.grid(row=0, column=3) 

#----------------------------------#
 
playerC12 = Frame(playerC1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
playerC12.grid(row=1, column=1, padx=5, pady=5)

playerC12Title = Frame(playerC12, width=70, height=40)
playerC12Title.grid(row=0, column=0)

playerC12Label = Label(playerC12Title, text="Star Shuriken")
playerC12Label.grid(row=0, column=0)

playerC12Buttons = Frame(playerC12, width=70, height=40)
playerC12Buttons.grid(row =1, column=0, padx=5, pady=5)

playerC12B1V = IntVar()
playerC12B1 = Checkbutton(playerC12Buttons, variable=playerC12B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC12B1.grid(row=0, column=0)

playerC12B2V = IntVar()
playerC12B2 = Checkbutton(playerC12Buttons, variable=playerC12B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC12B2.grid(row=0, column=1) 

playerC12B3V = IntVar()
playerC12B3 = Checkbutton(playerC12Buttons, variable=playerC12B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC12B3.grid(row=0, column=2) 

playerC12B4V = IntVar()
playerC12B4 = Checkbutton(playerC12Buttons, variable=playerC12B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC12B4.grid(row=0, column=3) 

#----------------------------------#

playerC13 = Frame(playerC1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
playerC13.grid(row=1, column=2, padx=5, pady=5)

playerC13Title = Frame(playerC13, width=70, height=40)
playerC13Title.grid(row=0, column=0)

playerC13Label = Label(playerC13Title, text="Swift Escape")
playerC13Label.grid(row=0, column=0)

playerC13Buttons = Frame(playerC13, width=70, height=40)
playerC13Buttons.grid(row =1, column=0, padx=5, pady=5)

playerC13B1V = IntVar()
playerC13B1 = Checkbutton(playerC13Buttons, variable=playerC13B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC13B1.grid(row=0, column=0)

playerC13B2V = IntVar()
playerC13B2 = Checkbutton(playerC13Buttons, variable=playerC13B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC13B2.grid(row=0, column=1) 

playerC13B3V = IntVar()
playerC13B3 = Checkbutton(playerC13Buttons, variable=playerC13B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC13B3.grid(row=0, column=2) 

playerC13B4V = IntVar()
playerC13B4 = Checkbutton(playerC13Buttons, variable=playerC13B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC13B4.grid(row=0, column=3) 

#----------------------------------#

playerC14 = Frame(playerC1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
playerC14.grid(row=1, column=3, padx=5, pady=5)

playerC14Title = Frame(playerC14, width=70, height=40)
playerC14Title.grid(row=0, column=0)

playerC14Label = Label(playerC14Title, text="Tail Slap")
playerC14Label.grid(row=0, column=0)

playerC14Buttons = Frame(playerC14, width=70, height=40)
playerC14Buttons.grid(row =1, column=0, padx=5, pady=5)

playerC14B1V = IntVar()
playerC14B1 = Checkbutton(playerC14Buttons, variable=playerC14B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC14B1.grid(row=0, column=0)

playerC14B2V = IntVar()
playerC14B2 = Checkbutton(playerC14Buttons, variable=playerC14B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC14B2.grid(row=0, column=1) 

playerC14B3V = IntVar()
playerC14B3 = Checkbutton(playerC14Buttons, variable=playerC14B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC14B3.grid(row=0, column=2) 

playerC14B4V = IntVar()
playerC14B4 = Checkbutton(playerC14Buttons, variable=playerC14B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0)
playerC14B4.grid(row=0, column=3) 
'''

#-------------------------------------------------------------------------------------------------------------#

opponent = Frame(window)
opponent.pack(pady=15)

#----------------------------------------------------------------#

opponentCardsTitle = Frame(opponent)
opponentCardsTitle.pack()

opponentCardsLabel = Label(opponentCardsTitle, text="Opponent")
opponentCardsLabel.grid(row=0, column=0, padx=30)

#----------------------------------------------------------------#

opponentCardButtons = Frame(opponent)
opponentCardButtons.pack(pady=5)

#----------------------------------------------------------------#

opponentEnergy = Frame(opponentCardButtons)
opponentEnergy.grid(row=0, column=0, padx=10)

opponentEnergyTitle = Frame(opponentEnergy)
opponentEnergyTitle.pack(side=TOP)

opponentEnergyLabel = Label(opponentEnergyTitle, text="Opponent Energy")
opponentEnergyLabel.pack(side=TOP)

opponentEnergyButtons = Frame(opponentEnergy)
opponentEnergyButtons.pack(side=BOTTOM, pady=3)

opponentEnergyCount = 3

def subtractOpponentEnergy():
    global opponentEnergyCount
    opponentEnergyCount -= 1
    opponentEnergyCounter.delete(0, END)
    opponentEnergyCounter.insert(END, opponentEnergyCount)

def addOpponentEnergy():
    global opponentEnergyCount
    opponentEnergyCount += 1
    opponentEnergyCounter.delete(0, END)
    opponentEnergyCounter.insert(END, opponentEnergyCount)

subtractOpponentEnergyButton = Button(opponentEnergyButtons, text="-", command=subtractOpponentEnergy, width=2)
subtractOpponentEnergyButton.grid(row=0, column=0)

opponentEnergyCounter = Entry(opponentEnergyButtons, width=5, justify=CENTER)
opponentEnergyCounter.insert(END, opponentEnergyCount)
opponentEnergyCounter.grid(row=0, column=1, padx=10)

addOpponentEnergyButton = Button(opponentEnergyButtons, text="+", command=addOpponentEnergy, width=2)
addOpponentEnergyButton.grid(row=0, column=2)

#--------------#

opponentOnDeck = Frame(opponentCardButtons)
opponentOnDeck.grid(row=0, column=1, padx=10)

opponentOnDeckTitle = Frame(opponentOnDeck)
opponentOnDeckTitle.pack(side=TOP)

opponentOnDeckLabel = Label(opponentOnDeckTitle, text="On Deck")
opponentOnDeckLabel.pack(side=TOP)

opponentOnDeckButtons = Frame(opponentOnDeck)
opponentOnDeckButtons.pack(side=BOTTOM, pady=3)

opponentOnDeckCount = 24

def subtractOpponentOnDeck():
    global opponentOnDeckCount
    opponentOnDeckCount -= 1
    opponentOnDeckCounter.delete(0, END)
    opponentOnDeckCounter.insert(END, opponentOnDeckCount)

def addOpponentOnDeck():
    global opponentOnDeckCount
    opponentOnDeckCount += 1
    opponentOnDeckCounter.delete(0, END)
    opponentOnDeckCounter.insert(END, opponentOnDeckCount)

subtractOpponentOnDeckButton = Button(opponentOnDeckButtons, text="-", command=subtractOpponentOnDeck, width=2)
subtractOpponentOnDeckButton.grid(row=0, column=0)

opponentOnDeckCounter = Entry(opponentOnDeckButtons, width=5, justify=CENTER)
opponentOnDeckCounter.insert(END, opponentOnDeckCount)
opponentOnDeckCounter.grid(row=0, column=1, padx=10)

addOpponentOnDeckButton = Button(opponentOnDeckButtons, text="+", command=addOpponentOnDeck, width=2)
addOpponentOnDeckButton.grid(row=0, column=2)

#----------------------------------------------------------------#

opponentOnHand = Frame(opponentCardButtons)
opponentOnHand.grid(row=0, column=2, padx=10)

opponentOnHandTitle = Frame(opponentOnHand)
opponentOnHandTitle.pack(side=TOP)

opponentOnHandLabel = Label(opponentOnHandTitle, text="On Hand")
opponentOnHandLabel.pack(side=TOP)

opponentOnHandButtons = Frame(opponentOnHand)
opponentOnHandButtons.pack(side=BOTTOM, pady=3)

opponentOnHandCount = 6

def subtractOpponentOnHand():
    global opponentOnHandCount
    opponentOnHandCount -= 1
    opponentOnHandCounter.delete(0, END)
    opponentOnHandCounter.insert(END, opponentOnHandCount)
    

def addOpponentOnHand():
    global opponentOnHandCount
    opponentOnHandCount += 1
    opponentOnHandCounter.delete(0, END)
    opponentOnHandCounter.insert(END, opponentOnHandCount)


subtractOpponentOnHand2Button = Button(opponentOnHandButtons, text="-", command=subtractOpponentOnHand, width=2)
subtractOpponentOnHand2Button.grid(row=0, column=0, padx=3)

opponentOnHandCounter = Entry(opponentOnHandButtons, width=5, justify=CENTER)
opponentOnHandCounter.insert(END, opponentOnHandCount)
opponentOnHandCounter.grid(row=0, column=1, padx=10)

addOpponentOnHandButton = Button(opponentOnHandButtons, text="+", command=addOpponentOnHand, width=2)
addOpponentOnHandButton.grid(row=0, column=2)

opponentButtons = Frame(opponent)
opponentButtons.pack(pady=5)

#-------------------------------------------------------------------------------------------------------------#

newOpponentDeckButton = Button(opponentButtons, text="New Deck")
newOpponentDeckButton.grid(row=0, column=0, padx=3)

resetOpponentDeckButton = Button(opponentButtons, text="Reset Deck")
resetOpponentDeckButton.grid(row=0, column=1, padx=3)

deleteOpponentACardsButton = Button(opponentButtons, text="Disable Front")
deleteOpponentACardsButton.grid(row=0, column=2, padx=3)

deleteOpponentBCardsButton = Button(opponentButtons, text="Disable Mid")
deleteOpponentBCardsButton.grid(row=0, column=3, padx=3)

deleteOpponentCCardsButton = Button(opponentButtons, text="Disable Back")
deleteOpponentCCardsButton.grid(row=0, column=4, padx=3)

#-------------------------------------------------------------------------------------------------------------#

opponentA1 = Frame(opponent)
opponentA1.pack(pady=5)

opponentA1Title = Frame(opponentA1)
opponentA1Title.grid(row=0, column=0, padx=30)

opponentA1Label = Label(opponentA1Title, text="Front")
opponentA1Label.grid(row=0, column=0, padx=30)

opponentA1Cards = Frame(opponentA1)
opponentA1Cards.grid(row=1, column=0, padx=30)

#----------------------------------------------------------------#



opponentA11 = Frame(opponentA1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
opponentA11.grid(row=1, column=0, padx=5, pady=5)


opponentA11Title = Frame(opponentA11, width=70, height=40)
opponentA11Title.grid(row=0, column=0)

def check_input(event):
    value = event.widget.get()

    if value == '':
        opponentA11Combobox['values'] = cards
    else:
        data = [] 
        for item in cards:
            if value.lower() in item.lower():
                data.append(item)

        opponentA11Combobox['values'] = data

opponentA11Combobox = ttk.Combobox(opponentA11Title, width=15)
opponentA11Combobox['values'] = cards
opponentA11Combobox.bind('<KeyRelease>', check_input)
opponentA11Combobox.grid(row=0, column=0)

opponentA11Buttons = Frame(opponentA11, width=70, height=40)
opponentA11Buttons.grid(row=1, column=0, padx=5, pady=5)

def opponentA11B1V_onClick():
    if opponentA11Combobox.get() in oneEnergyCards:
        if opponentA11B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA11B1V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA11Combobox.get() in noEnergyCards:
        if opponentA11B1V.get() == 1:
            subtractOpponentOnHand()
        if opponentA11B1V.get() == 0:
            addOpponentOnHand()
    elif opponentA11Combobox.get() in twoEnergyCards:
        if opponentA11B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA11B1V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()


opponentA11B1V = IntVar()
opponentA11B1 = Checkbutton(opponentA11Buttons, variable=opponentA11B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA11B1V_onClick)
opponentA11B1.grid(row=0, column=0)

def opponentA11B2V_onClick():
    if opponentA11Combobox.get() in oneEnergyCards:
        if opponentA11B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA11B2V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA11Combobox.get() in noEnergyCards:
        if opponentA11B2V.get() == 1:
            subtractOpponentOnHand()
        if opponentA11B2V.get() == 0:
            addOpponentOnHand()
    elif opponentA11Combobox.get() in twoEnergyCards:
        if opponentA11B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA11B2V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA11B2V = IntVar()
opponentA11B2 = Checkbutton(opponentA11Buttons, variable=opponentA11B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA11B2V_onClick)
opponentA11B2.grid(row=0, column=1) 

def opponentA11B3V_onClick():
    if opponentA11Combobox.get() in oneEnergyCards:
        if opponentA11B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA11B3V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA11Combobox.get() in noEnergyCards:
        if opponentA11B3V.get() == 1:
            subtractOpponentOnHand()
        if opponentA11B3V.get() == 0:
            addOpponentOnHand()
    elif opponentA11Combobox.get() in twoEnergyCards:
        if opponentA11B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA11B3V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA11B3V = IntVar()
opponentA11B3 = Checkbutton(opponentA11Buttons, variable=opponentA11B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA11B3V_onClick)
opponentA11B3.grid(row=0, column=2) 

def opponentA11B4V_onClick():
    if opponentA11Combobox.get() in oneEnergyCards:
        if opponentA11B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA11B4V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA11Combobox.get() in noEnergyCards:
        if opponentA11B4V.get() == 1:
            subtractOpponentOnHand()
        if opponentA11B4V.get() == 0:
            addOpponentOnHand()
    elif opponentA11Combobox.get() in twoEnergyCards:
        if opponentA11B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA11B4V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA11B4V = IntVar()
opponentA11B4 = Checkbutton(opponentA11Buttons, variable=opponentA11B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA11B4V_onClick)
opponentA11B4.grid(row=0, column=3) 

#-------------------------------------------------------------------------------------------------------------#


opponentA12 = Frame(opponentA1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
opponentA12.grid(row=1, column=1, padx=5, pady=5)

opponentA12Title = Frame(opponentA12, width=70, height=40)
opponentA12Title.grid(row=0, column=0)

def check_input(event):
    value = event.widget.get()

    if value == '':
        opponentA12Combobox['values'] = cards
    else:
        data = [] 
        for item in cards:
            if value.lower() in item.lower():
                data.append(item)

        opponentA12Combobox['values'] = data

opponentA12Combobox = ttk.Combobox(opponentA12Title, width=15)
opponentA12Combobox['values'] = cards
opponentA12Combobox.bind('<KeyRelease>', check_input)
opponentA12Combobox.grid(row=0, column=0)

opponentA12Buttons = Frame(opponentA12, width=70, height=40)
opponentA12Buttons.grid(row=1, column=0, padx=5, pady=5)

def opponentA12B1V_onClick():
    if opponentA12Combobox.get() in oneEnergyCards:
        if opponentA12B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA12B1V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA12Combobox.get() in noEnergyCards:
        if opponentA12B1V.get() == 1:
            subtractOpponentOnHand()
        if opponentA12B1V.get() == 0:
            addOpponentOnHand()
    elif opponentA12Combobox.get() in twoEnergyCards:
        if opponentA12B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA12B1V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA12B1V = IntVar()
opponentA12B1 = Checkbutton(opponentA12Buttons, variable=opponentA12B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA12B1V_onClick)
opponentA12B1.grid(row=0, column=0)

def opponentA12B2V_onClick():
    if opponentA12Combobox.get() in oneEnergyCards:
        if opponentA12B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA12B2V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA12Combobox.get() in noEnergyCards:
        if opponentA12B2V.get() == 1:
            subtractOpponentOnHand()
        if opponentA12B2V.get() == 0:
            addOpponentOnHand()
    elif opponentA12Combobox.get() in twoEnergyCards:
        if opponentA12B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA12B2V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA12B2V = IntVar()
opponentA12B2 = Checkbutton(opponentA12Buttons, variable=opponentA12B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA12B2V_onClick)
opponentA12B2.grid(row=0, column=1) 

def opponentA12B3V_onClick():
    if opponentA12Combobox.get() in oneEnergyCards:
        if opponentA12B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA12B3V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA12Combobox.get() in noEnergyCards:
        if opponentA12B3V.get() == 1:
            subtractOpponentOnHand()
        if opponentA12B3V.get() == 0:
            addOpponentOnHand()
    elif opponentA12Combobox.get() in twoEnergyCards:
        if opponentA12B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA12B3V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA12B3V = IntVar()
opponentA12B3 = Checkbutton(opponentA12Buttons, variable=opponentA12B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA12B3V_onClick)
opponentA12B3.grid(row=0, column=2) 

def opponentA12B4V_onClick():
    if opponentA12Combobox.get() in oneEnergyCards:
        if opponentA12B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA12B4V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA12Combobox.get() in noEnergyCards:
        if opponentA12B4V.get() == 1:
            subtractOpponentOnHand()
        if opponentA12B4V.get() == 0:
            addOpponentOnHand()
    elif opponentA12Combobox.get() in twoEnergyCards:
        if opponentA12B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA12B4V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA12B4V = IntVar()
opponentA12B4 = Checkbutton(opponentA12Buttons, variable=opponentA12B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA12B4V_onClick)
opponentA12B4.grid(row=0, column=3) 

#-------------------------------------------------------------------------------------------------------------#

opponentA13 = Frame(opponentA1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
opponentA13.grid(row=1, column=2, padx=5, pady=5)

opponentA13Title = Frame(opponentA13, width=70, height=40)
opponentA13Title.grid(row=0, column=0)

def check_input(event):
    value = event.widget.get()

    if value == '':
        opponentA13Combobox['values'] = cards
    else:
        data = [] 
        for item in cards:
            if value.lower() in item.lower():
                data.append(item)

        opponentA13Combobox['values'] = data

opponentA13Combobox = ttk.Combobox(opponentA13Title, width=15)
opponentA13Combobox['values'] = cards
opponentA13Combobox.bind('<KeyRelease>', check_input)
opponentA13Combobox.grid(row=0, column=0)

opponentA13Buttons = Frame(opponentA13, width=70, height=40)
opponentA13Buttons.grid(row=1, column=0, padx=5, pady=5)

def opponentA13B1V_onClick():
    if opponentA13Combobox.get() in oneEnergyCards:
        if opponentA13B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA13B1V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA13Combobox.get() in noEnergyCards:
        if opponentA13B1V.get() == 1:
            subtractOpponentOnHand()
        if opponentA13B1V.get() == 0:
            addOpponentOnHand()
    elif opponentA13Combobox.get() in twoEnergyCards:
        if opponentA13B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA13B1V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA13B1V = IntVar()
opponentA13B1 = Checkbutton(opponentA13Buttons, variable=opponentA13B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA13B1V_onClick)
opponentA13B1.grid(row=0, column=0)

def opponentA13B2V_onClick():
    if opponentA13Combobox.get() in oneEnergyCards:
        if opponentA13B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA13B2V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA13Combobox.get() in noEnergyCards:
        if opponentA13B2V.get() == 1:
            subtractOpponentOnHand()
        if opponentA13B2V.get() == 0:
            addOpponentOnHand()
    elif opponentA13Combobox.get() in twoEnergyCards:
        if opponentA13B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA13B2V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA13B2V = IntVar()
opponentA13B2 = Checkbutton(opponentA13Buttons, variable=opponentA13B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA13B2V_onClick)
opponentA13B2.grid(row=0, column=1) 

def opponentA13B3V_onClick():
    if opponentA13Combobox.get() in oneEnergyCards:
        if opponentA13B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA13B3V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA13Combobox.get() in noEnergyCards:
        if opponentA13B3V.get() == 1:
            subtractOpponentOnHand()
        if opponentA13B3V.get() == 0:
            addOpponentOnHand()
    elif opponentA13Combobox.get() in twoEnergyCards:
        if opponentA13B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA13B3V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA13B3V = IntVar()
opponentA13B3 = Checkbutton(opponentA13Buttons, variable=opponentA13B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA13B3V_onClick)
opponentA13B3.grid(row=0, column=2) 

def opponentA13B4V_onClick():
    if opponentA13Combobox.get() in oneEnergyCards:
        if opponentA13B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA13B4V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA13Combobox.get() in noEnergyCards:
        if opponentA13B4V.get() == 1:
            subtractOpponentOnHand()
        if opponentA13B4V.get() == 0:
            addOpponentOnHand()
    elif opponentA13Combobox.get() in twoEnergyCards:
        if opponentA13B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA13B4V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA13B4V = IntVar()
opponentA13B4 = Checkbutton(opponentA13Buttons, variable=opponentA13B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA13B4V_onClick)
opponentA13B4.grid(row=0, column=3) 

#-------------------------------------------------------------------------------------------------------------#

opponentA14 = Frame(opponentA1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
opponentA14.grid(row=1, column=3, padx=5, pady=5)

opponentA14Title = Frame(opponentA14, width=70, height=40)
opponentA14Title.grid(row=0, column=0)

def check_input(event):
    value = event.widget.get()

    if value == '':
        opponentA14Combobox['values'] = cards
    else:
        data = [] 
        for item in cards:
            if value.lower() in item.lower():
                data.append(item)

        opponentA14Combobox['values'] = data

opponentA14Combobox = ttk.Combobox(opponentA14Title, width=15)
opponentA14Combobox['values'] = cards
opponentA14Combobox.bind('<KeyRelease>', check_input)
opponentA14Combobox.grid(row=0, column=0)

opponentA14Buttons = Frame(opponentA14, width=70, height=40)
opponentA14Buttons.grid(row=1, column=0, padx=5, pady=5)

def opponentA14B1V_onClick():
    if opponentA14Combobox.get() in oneEnergyCards:
        if opponentA14B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA14B1V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA14Combobox.get() in noEnergyCards:
        if opponentA14B1V.get() == 1:
            subtractOpponentOnHand()
        if opponentA14B1V.get() == 0:
            addOpponentOnHand()
    elif opponentA14Combobox.get() in twoEnergyCards:
        if opponentA14B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA14B1V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA14B1V = IntVar()
opponentA14B1 = Checkbutton(opponentA14Buttons, variable=opponentA14B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA14B1V_onClick)
opponentA14B1.grid(row=0, column=0)

def opponentA14B2V_onClick():
    if opponentA14Combobox.get() in oneEnergyCards:
        if opponentA14B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA14B2V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA14Combobox.get() in noEnergyCards:
        if opponentA14B2V.get() == 1:
            subtractOpponentOnHand()
        if opponentA14B2V.get() == 0:
            addOpponentOnHand()
    elif opponentA14Combobox.get() in twoEnergyCards:
        if opponentA14B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA14B2V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA14B2V = IntVar()
opponentA14B2 = Checkbutton(opponentA14Buttons, variable=opponentA14B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA14B2V_onClick)
opponentA14B2.grid(row=0, column=1) 

def opponentA14B3V_onClick():
    if opponentA14Combobox.get() in oneEnergyCards:
        if opponentA14B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA14B3V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA14Combobox.get() in noEnergyCards:
        if opponentA14B3V.get() == 1:
            subtractOpponentOnHand()
        if opponentA14B3V.get() == 0:
            addOpponentOnHand()
    elif opponentA14Combobox.get() in twoEnergyCards:
        if opponentA14B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA14B3V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA14B3V = IntVar()
opponentA14B3 = Checkbutton(opponentA14Buttons, variable=opponentA14B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA14B3V_onClick)
opponentA14B3.grid(row=0, column=2) 

def opponentA14B4V_onClick():
    if opponentA14Combobox.get() in oneEnergyCards:
        if opponentA14B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA14B4V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentA14Combobox.get() in noEnergyCards:
        if opponentA14B4V.get() == 1:
            subtractOpponentOnHand()
        if opponentA14B4V.get() == 0:
            addOpponentOnHand()
    elif opponentA14Combobox.get() in twoEnergyCards:
        if opponentA14B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentA14B4V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentA14B4V = IntVar()
opponentA14B4 = Checkbutton(opponentA14Buttons, variable=opponentA14B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentA14B4V_onClick)
opponentA14B4.grid(row=0, column=3) 


#-------------------------------------------------------------------------------------------------------------#

opponentB1 = Frame(opponent)
opponentB1.pack(pady=5)

opponentB1Title = Frame(opponentB1)
opponentB1Title.grid(row=0, column=0, padx=30)

opponentB1Label = Label(opponentB1Title, text="Mid")
opponentB1Label.grid(row=0, column=0, padx=30)

opponentB1Cards = Frame(opponentB1)
opponentB1Cards.grid(row=1, column=0, padx=30)

#----------------------------------------------------------------#


opponentB11 = Frame(opponentB1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
opponentB11.grid(row=1, column=0, padx=5, pady=5)

opponentB11Title = Frame(opponentB11, width=70, height=40)
opponentB11Title.grid(row=0, column=0)

def check_input(event):
    value = event.widget.get()

    if value == '':
        opponentB11Combobox['values'] = cards
    else:
        data = [] 
        for item in cards:
            if value.lower() in item.lower():
                data.append(item)

        opponentB11Combobox['values'] = data

opponentB11Combobox = ttk.Combobox(opponentB11Title, width=15)
opponentB11Combobox['values'] = cards
opponentB11Combobox.bind('<KeyRelease>', check_input)
opponentB11Combobox.grid(row=0, column=0)

opponentB11Buttons = Frame(opponentB11, width=70, height=40)
opponentB11Buttons.grid(row=1, column=0, padx=5, pady=5)

def opponentB11B1V_onClick():
    if opponentB11Combobox.get() in oneEnergyCards:
        if opponentB11B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB11B1V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB11Combobox.get() in noEnergyCards:
        if opponentB11B1V.get() == 1:
            subtractOpponentOnHand()
        if opponentB11B1V.get() == 0:
            addOpponentOnHand()
    elif opponentB11Combobox.get() in twoEnergyCards:
        if opponentB11B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB11B1V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB11B1V = IntVar()
opponentB11B1 = Checkbutton(opponentB11Buttons, variable=opponentB11B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB11B1V_onClick)
opponentB11B1.grid(row=0, column=0)

def opponentB11B2V_onClick():
    if opponentB11Combobox.get() in oneEnergyCards:
        if opponentB11B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB11B2V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB11Combobox.get() in noEnergyCards:
        if opponentB11B2V.get() == 1:
            subtractOpponentOnHand()
        if opponentB11B2V.get() == 0:
            addOpponentOnHand()
    elif opponentB11Combobox.get() in twoEnergyCards:
        if opponentB11B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB11B2V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB11B2V = IntVar()
opponentB11B2 = Checkbutton(opponentB11Buttons, variable=opponentB11B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB11B2V_onClick)
opponentB11B2.grid(row=0, column=1) 

def opponentB11B3V_onClick():
    if opponentB11Combobox.get() in oneEnergyCards:
        if opponentB11B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB11B3V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB11Combobox.get() in noEnergyCards:
        if opponentB11B3V.get() == 1:
            subtractOpponentOnHand()
        if opponentB11B3V.get() == 0:
            addOpponentOnHand()
    elif opponentB11Combobox.get() in twoEnergyCards:
        if opponentB11B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB11B3V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB11B3V = IntVar()
opponentB11B3 = Checkbutton(opponentB11Buttons, variable=opponentB11B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB11B3V_onClick)
opponentB11B3.grid(row=0, column=2) 

def opponentB11B4V_onClick():
    if opponentB11Combobox.get() in oneEnergyCards:
        if opponentB11B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB11B4V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB11Combobox.get() in noEnergyCards:
        if opponentB11B4V.get() == 1:
            subtractOpponentOnHand()
        if opponentB11B4V.get() == 0:
            addOpponentOnHand()
    elif opponentB11Combobox.get() in twoEnergyCards:
        if opponentB11B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB11B4V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB11B4V = IntVar()
opponentB11B4 = Checkbutton(opponentB11Buttons, variable=opponentB11B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB11B4V_onClick)
opponentB11B4.grid(row=0, column=3) 

#-------------------------------------------------------------------------------------------------------------#

opponentB12 = Frame(opponentB1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
opponentB12.grid(row=1, column=1, padx=5, pady=5)

opponentB12Title = Frame(opponentB12, width=70, height=40)
opponentB12Title.grid(row=0, column=0)

def check_input(event):
    value = event.widget.get()

    if value == '':
        opponentB12Combobox['values'] = cards
    else:
        data = [] 
        for item in cards:
            if value.lower() in item.lower():
                data.append(item)

        opponentB12Combobox['values'] = data

opponentB12Combobox = ttk.Combobox(opponentB12Title, width=15)
opponentB12Combobox['values'] = cards
opponentB12Combobox.bind('<KeyRelease>', check_input)
opponentB12Combobox.grid(row=0, column=0)

opponentB12Buttons = Frame(opponentB12, width=70, height=40)
opponentB12Buttons.grid(row=1, column=0, padx=5, pady=5)

def opponentB12B1V_onClick():
    if opponentB12Combobox.get() in oneEnergyCards:
        if opponentB12B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB12B1V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB12Combobox.get() in noEnergyCards:
        if opponentB12B1V.get() == 1:
            subtractOpponentOnHand()
        if opponentB12B1V.get() == 0:
            addOpponentOnHand()
    elif opponentB12Combobox.get() in twoEnergyCards:
        if opponentB12B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB12B1V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB12B1V = IntVar()
opponentB12B1 = Checkbutton(opponentB12Buttons, variable=opponentB12B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB12B1V_onClick)
opponentB12B1.grid(row=0, column=0)

def opponentB12B2V_onClick():
    if opponentB12Combobox.get() in oneEnergyCards:
        if opponentB12B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB12B2V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB12Combobox.get() in noEnergyCards:
        if opponentB12B2V.get() == 1:
            subtractOpponentOnHand()
        if opponentB12B2V.get() == 0:
            addOpponentOnHand()
    elif opponentB12Combobox.get() in twoEnergyCards:
        if opponentB12B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB12B2V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB12B2V = IntVar()
opponentB12B2 = Checkbutton(opponentB12Buttons, variable=opponentB12B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB12B2V_onClick)
opponentB12B2.grid(row=0, column=1) 

def opponentB12B3V_onClick():
    if opponentB12Combobox.get() in oneEnergyCards:
        if opponentB12B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB12B3V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB12Combobox.get() in noEnergyCards:
        if opponentB12B3V.get() == 1:
            subtractOpponentOnHand()
        if opponentB12B3V.get() == 0:
            addOpponentOnHand()
    elif opponentB12Combobox.get() in twoEnergyCards:
        if opponentB12B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB12B3V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB12B3V = IntVar()
opponentB12B3 = Checkbutton(opponentB12Buttons, variable=opponentB12B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB12B3V_onClick)
opponentB12B3.grid(row=0, column=2) 

def opponentB12B4V_onClick():
    if opponentB12Combobox.get() in oneEnergyCards:
        if opponentB12B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB12B4V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB12Combobox.get() in noEnergyCards:
        if opponentB12B4V.get() == 1:
            subtractOpponentOnHand()
        if opponentB12B4V.get() == 0:
            addOpponentOnHand()
    elif opponentB12Combobox.get() in twoEnergyCards:
        if opponentB12B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB12B4V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB12B4V = IntVar()
opponentB12B4 = Checkbutton(opponentB12Buttons, variable=opponentB12B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB12B4V_onClick)
opponentB12B4.grid(row=0, column=3) 

#-------------------------------------------------------------------------------------------------------------#

opponentB13 = Frame(opponentB1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
opponentB13.grid(row=1, column=2, padx=5, pady=5)

opponentB13Title = Frame(opponentB13, width=70, height=40)
opponentB13Title.grid(row=0, column=0)

def check_input(event):
    value = event.widget.get()

    if value == '':
        opponentB13Combobox['values'] = cards
    else:
        data = [] 
        for item in cards:
            if value.lower() in item.lower():
                data.append(item)

        opponentB13Combobox['values'] = data

opponentB13Combobox = ttk.Combobox(opponentB13Title, width=15)
opponentB13Combobox['values'] = cards
opponentB13Combobox.bind('<KeyRelease>', check_input)
opponentB13Combobox.grid(row=0, column=0)

opponentB13Buttons = Frame(opponentB13, width=70, height=40)
opponentB13Buttons.grid(row=1, column=0, padx=5, pady=5)

def opponentB13B1V_onClick():
    if opponentB13Combobox.get() in oneEnergyCards:
        if opponentB13B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB13B1V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB13Combobox.get() in noEnergyCards:
        if opponentB13B1V.get() == 1:
            subtractOpponentOnHand()
        if opponentB13B1V.get() == 0:
            addOpponentOnHand()
    elif opponentB13Combobox.get() in twoEnergyCards:
        if opponentB13B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB13B1V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB13B1V = IntVar()
opponentB13B1 = Checkbutton(opponentB13Buttons, variable=opponentB13B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB13B1V_onClick)
opponentB13B1.grid(row=0, column=0)

def opponentB13B2V_onClick():
    if opponentB13Combobox.get() in oneEnergyCards:
        if opponentB13B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB13B2V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB13Combobox.get() in noEnergyCards:
        if opponentB13B2V.get() == 1:
            subtractOpponentOnHand()
        if opponentB13B2V.get() == 0:
            addOpponentOnHand()
    elif opponentB13Combobox.get() in twoEnergyCards:
        if opponentB13B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB13B2V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB13B2V = IntVar()
opponentB13B2 = Checkbutton(opponentB13Buttons, variable=opponentB13B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB13B2V_onClick)
opponentB13B2.grid(row=0, column=1) 

def opponentB13B3V_onClick():
    if opponentB13Combobox.get() in oneEnergyCards:
        if opponentB13B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB13B3V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB13Combobox.get() in noEnergyCards:
        if opponentB13B3V.get() == 1:
            subtractOpponentOnHand()
        if opponentB13B3V.get() == 0:
            addOpponentOnHand()
    elif opponentB13Combobox.get() in twoEnergyCards:
        if opponentB13B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB13B3V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB13B3V = IntVar()
opponentB13B3 = Checkbutton(opponentB13Buttons, variable=opponentB13B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB13B3V_onClick)
opponentB13B3.grid(row=0, column=2) 

def opponentB13B4V_onClick():
    if opponentB13Combobox.get() in oneEnergyCards:
        if opponentB13B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB13B4V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB13Combobox.get() in noEnergyCards:
        if opponentB13B4V.get() == 1:
            subtractOpponentOnHand()
        if opponentB13B4V.get() == 0:
            addOpponentOnHand()
    elif opponentB13Combobox.get() in twoEnergyCards:
        if opponentB13B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB13B4V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB13B4V = IntVar()
opponentB13B4 = Checkbutton(opponentB13Buttons, variable=opponentB13B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB13B4V_onClick)
opponentB13B4.grid(row=0, column=3) 

#-------------------------------------------------------------------------------------------------------------#

opponentB14 = Frame(opponentB1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
opponentB14.grid(row=1, column=3, padx=5, pady=5)

opponentB14Title = Frame(opponentB14, width=70, height=40)
opponentB14Title.grid(row=0, column=0)

def check_input(event):
    value = event.widget.get()

    if value == '':
        opponentB14Combobox['values'] = cards
    else:
        data = [] 
        for item in cards:
            if value.lower() in item.lower():
                data.append(item)

        opponentB14Combobox['values'] = data

opponentB14Combobox = ttk.Combobox(opponentB14Title, width=15)
opponentB14Combobox['values'] = cards
opponentB14Combobox.bind('<KeyRelease>', check_input)
opponentB14Combobox.grid(row=0, column=0)

opponentB14Buttons = Frame(opponentB14, width=70, height=40)
opponentB14Buttons.grid(row=1, column=0, padx=5, pady=5)

def opponentB14B1V_onClick():
    if opponentB14Combobox.get() in oneEnergyCards:
        if opponentB14B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB14B1V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB14Combobox.get() in noEnergyCards:
        if opponentB14B1V.get() == 1:
            subtractOpponentOnHand()
        if opponentB14B1V.get() == 0:
            addOpponentOnHand()
    elif opponentB14Combobox.get() in twoEnergyCards:
        if opponentB14B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB14B1V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB14B1V = IntVar()
opponentB14B1 = Checkbutton(opponentB14Buttons, variable=opponentB14B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB14B1V_onClick)
opponentB14B1.grid(row=0, column=0)

def opponentB14B2V_onClick():
    if opponentB14Combobox.get() in oneEnergyCards:
        if opponentB14B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB14B2V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB14Combobox.get() in noEnergyCards:
        if opponentB14B2V.get() == 1:
            subtractOpponentOnHand()
        if opponentB14B2V.get() == 0:
            addOpponentOnHand()
    elif opponentB14Combobox.get() in twoEnergyCards:
        if opponentB14B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB14B2V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB14B2V = IntVar()
opponentB14B2 = Checkbutton(opponentB14Buttons, variable=opponentB14B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB14B2V_onClick)
opponentB14B2.grid(row=0, column=1) 

def opponentB14B3V_onClick():
    if opponentB14Combobox.get() in oneEnergyCards:
        if opponentB14B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB14B3V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB14Combobox.get() in noEnergyCards:
        if opponentB14B3V.get() == 1:
            subtractOpponentOnHand()
        if opponentB14B3V.get() == 0:
            addOpponentOnHand()
    elif opponentB14Combobox.get() in twoEnergyCards:
        if opponentB14B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB14B3V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB14B3V = IntVar()
opponentB14B3 = Checkbutton(opponentB14Buttons, variable=opponentB14B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB14B3V_onClick)
opponentB14B3.grid(row=0, column=2) 

def opponentB14B4V_onClick():
    if opponentB14Combobox.get() in oneEnergyCards:
        if opponentB14B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB14B4V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentB14Combobox.get() in noEnergyCards:
        if opponentB14B4V.get() == 1:
            subtractOpponentOnHand()
        if opponentB14B4V.get() == 0:
            addOpponentOnHand()
    elif opponentB14Combobox.get() in twoEnergyCards:
        if opponentB14B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentB14B4V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentB14B4V = IntVar()
opponentB14B4 = Checkbutton(opponentB14Buttons, variable=opponentB14B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentB14B4V_onClick)
opponentB14B4.grid(row=0, column=3) 


#-------------------------------------------------------------------------------------------------------------#

opponentC1 = Frame(opponent)
opponentC1.pack(pady=5)

opponentC1Title = Frame(opponentC1)
opponentC1Title.grid(row=0, column=0, padx=30)

opponentC1Label = Label(opponentC1Title, text="Back")
opponentC1Label.grid(row=0, column=0, padx=30)

opponentC1Cards = Frame(opponentC1)
opponentC1Cards.grid(row=1, column=0, padx=30)

#----------------------------------------------------------------#


opponentC11 = Frame(opponentC1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
opponentC11.grid(row=1, column=0, padx=5, pady=5)

opponentC11Title = Frame(opponentC11, width=70, height=40)
opponentC11Title.grid(row=0, column=0)

def check_input(event):
    value = event.widget.get()

    if value == '':
        opponentC11Combobox['values'] = cards
    else:
        data = [] 
        for item in cards:
            if value.lower() in item.lower():
                data.append(item)

        opponentC11Combobox['values'] = data

opponentC11Combobox = ttk.Combobox(opponentC11Title, width=15)
opponentC11Combobox['values'] = cards
opponentC11Combobox.bind('<KeyRelease>', check_input)
opponentC11Combobox.grid(row=0, column=0)

opponentC11Buttons = Frame(opponentC11, width=70, height=40)
opponentC11Buttons.grid(row=1, column=0, padx=5, pady=5)

def opponentC11B1V_onClick():
    if opponentC11Combobox.get() in oneEnergyCards:
        if opponentC11B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC11B1V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC11Combobox.get() in noEnergyCards:
        if opponentC11B1V.get() == 1:
            subtractOpponentOnHand()
        if opponentC11B1V.get() == 0:
            addOpponentOnHand()
    elif opponentC11Combobox.get() in twoEnergyCards:
        if opponentC11B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC11B1V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC11B1V = IntVar()
opponentC11B1 = Checkbutton(opponentC11Buttons, variable=opponentC11B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC11B1V_onClick)
opponentC11B1.grid(row=0, column=0)

def opponentC11B2V_onClick():
    if opponentC11Combobox.get() in oneEnergyCards:
        if opponentC11B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC11B2V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC11Combobox.get() in noEnergyCards:
        if opponentC11B2V.get() == 1:
            subtractOpponentOnHand()
        if opponentC11B2V.get() == 0:
            addOpponentOnHand()
    elif opponentC11Combobox.get() in twoEnergyCards:
        if opponentC11B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC11B2V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC11B2V = IntVar()
opponentC11B2 = Checkbutton(opponentC11Buttons, variable=opponentC11B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC11B2V_onClick)
opponentC11B2.grid(row=0, column=1) 

def opponentC11B3V_onClick():
    if opponentC11Combobox.get() in oneEnergyCards:
        if opponentC11B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC11B3V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC11Combobox.get() in noEnergyCards:
        if opponentC11B3V.get() == 1:
            subtractOpponentOnHand()
        if opponentC11B3V.get() == 0:
            addOpponentOnHand()
    elif opponentC11Combobox.get() in twoEnergyCards:
        if opponentC11B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC11B3V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC11B3V = IntVar()
opponentC11B3 = Checkbutton(opponentC11Buttons, variable=opponentC11B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC11B3V_onClick)
opponentC11B3.grid(row=0, column=2) 

def opponentC11B4V_onClick():
    if opponentC11Combobox.get() in oneEnergyCards:
        if opponentC11B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC11B4V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC11Combobox.get() in noEnergyCards:
        if opponentC11B4V.get() == 1:
            subtractOpponentOnHand()
        if opponentC11B4V.get() == 0:
            addOpponentOnHand()
    elif opponentC11Combobox.get() in twoEnergyCards:
        if opponentC11B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC11B4V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC11B4V = IntVar()
opponentC11B4 = Checkbutton(opponentC11Buttons, variable=opponentC11B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC11B4V_onClick)
opponentC11B4.grid(row=0, column=3) 

#-------------------------------------------------------------------------------------------------------------#

opponentC12 = Frame(opponentC1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
opponentC12.grid(row=1, column=1, padx=5, pady=5)

opponentC12Title = Frame(opponentC12, width=70, height=40)
opponentC12Title.grid(row=0, column=0)

def check_input(event):
    value = event.widget.get()

    if value == '':
        opponentC12Combobox['values'] = cards
    else:
        data = [] 
        for item in cards:
            if value.lower() in item.lower():
                data.append(item)

        opponentC12Combobox['values'] = data

opponentC12Combobox = ttk.Combobox(opponentC12Title, width=15)
opponentC12Combobox['values'] = cards
opponentC12Combobox.bind('<KeyRelease>', check_input)
opponentC12Combobox.grid(row=0, column=0)

opponentC12Buttons = Frame(opponentC12, width=70, height=40)
opponentC12Buttons.grid(row=1, column=0, padx=5, pady=5)

def opponentC12B1V_onClick():
    if opponentC12Combobox.get() in oneEnergyCards:
        if opponentC12B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC12B1V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC12Combobox.get() in noEnergyCards:
        if opponentC12B1V.get() == 1:
            subtractOpponentOnHand()
        if opponentC12B1V.get() == 0:
            addOpponentOnHand()
    elif opponentC12Combobox.get() in twoEnergyCards:
        if opponentC12B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC12B1V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC12B1V = IntVar()
opponentC12B1 = Checkbutton(opponentC12Buttons, variable=opponentC12B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC12B1V_onClick)
opponentC12B1.grid(row=0, column=0)

def opponentC12B2V_onClick():
    if opponentC12Combobox.get() in oneEnergyCards:
        if opponentC12B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC12B2V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC12Combobox.get() in noEnergyCards:
        if opponentC12B2V.get() == 1:
            subtractOpponentOnHand()
        if opponentC12B2V.get() == 0:
            addOpponentOnHand()
    elif opponentC12Combobox.get() in twoEnergyCards:
        if opponentC12B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC12B2V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC12B2V = IntVar()
opponentC12B2 = Checkbutton(opponentC12Buttons, variable=opponentC12B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC12B2V_onClick)
opponentC12B2.grid(row=0, column=1) 

def opponentC12B3V_onClick():
    if opponentC12Combobox.get() in oneEnergyCards:
        if opponentC12B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC12B3V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC12Combobox.get() in noEnergyCards:
        if opponentC12B3V.get() == 1:
            subtractOpponentOnHand()
        if opponentC12B3V.get() == 0:
            addOpponentOnHand()
    elif opponentC12Combobox.get() in twoEnergyCards:
        if opponentC12B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC12B3V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC12B3V = IntVar()
opponentC12B3 = Checkbutton(opponentC12Buttons, variable=opponentC12B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC12B3V_onClick)
opponentC12B3.grid(row=0, column=2) 

def opponentC12B4V_onClick():
    if opponentC12Combobox.get() in oneEnergyCards:
        if opponentC12B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC12B4V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC12Combobox.get() in noEnergyCards:
        if opponentC12B4V.get() == 1:
            subtractOpponentOnHand()
        if opponentC12B4V.get() == 0:
            addOpponentOnHand()
    elif opponentC12Combobox.get() in twoEnergyCards:
        if opponentC12B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC12B4V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC12B4V = IntVar()
opponentC12B4 = Checkbutton(opponentC12Buttons, variable=opponentC12B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC12B4V_onClick)
opponentC12B4.grid(row=0, column=3) 

#-------------------------------------------------------------------------------------------------------------#

opponentC13 = Frame(opponentC1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
opponentC13.grid(row=1, column=2, padx=5, pady=5)

opponentC13Title = Frame(opponentC13, width=70, height=40)
opponentC13Title.grid(row=0, column=0)

def check_input(event):
    value = event.widget.get()

    if value == '':
        opponentC13Combobox['values'] = cards
    else:
        data = [] 
        for item in cards:
            if value.lower() in item.lower():
                data.append(item)

        opponentC13Combobox['values'] = data

opponentC13Combobox = ttk.Combobox(opponentC13Title, width=15)
opponentC13Combobox['values'] = cards
opponentC13Combobox.bind('<KeyRelease>', check_input)
opponentC13Combobox.grid(row=0, column=0)

opponentC13Buttons = Frame(opponentC13, width=70, height=40)
opponentC13Buttons.grid(row=1, column=0, padx=5, pady=5)

def opponentC13B1V_onClick():
    if opponentC13Combobox.get() in oneEnergyCards:
        if opponentC13B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC13B1V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC13Combobox.get() in noEnergyCards:
        if opponentC13B1V.get() == 1:
            subtractOpponentOnHand()
        if opponentC13B1V.get() == 0:
            addOpponentOnHand()
    elif opponentC13Combobox.get() in twoEnergyCards:
        if opponentC13B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC13B1V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC13B1V = IntVar()
opponentC13B1 = Checkbutton(opponentC13Buttons, variable=opponentC13B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC13B1V_onClick)
opponentC13B1.grid(row=0, column=0)

def opponentC13B2V_onClick():
    if opponentC13Combobox.get() in oneEnergyCards:
        if opponentC13B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC13B2V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC13Combobox.get() in noEnergyCards:
        if opponentC13B2V.get() == 1:
            subtractOpponentOnHand()
        if opponentC13B2V.get() == 0:
            addOpponentOnHand()
    elif opponentC13Combobox.get() in twoEnergyCards:
        if opponentC13B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC13B2V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC13B2V = IntVar()
opponentC13B2 = Checkbutton(opponentC13Buttons, variable=opponentC13B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC13B2V_onClick)
opponentC13B2.grid(row=0, column=1) 

def opponentC13B3V_onClick():
    if opponentC13Combobox.get() in oneEnergyCards:
        if opponentC13B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC13B3V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC13Combobox.get() in noEnergyCards:
        if opponentC13B3V.get() == 1:
            subtractOpponentOnHand()
        if opponentC13B3V.get() == 0:
            addOpponentOnHand()
    elif opponentC13Combobox.get() in twoEnergyCards:
        if opponentC13B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC13B3V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC13B3V = IntVar()
opponentC13B3 = Checkbutton(opponentC13Buttons, variable=opponentC13B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC13B3V_onClick)
opponentC13B3.grid(row=0, column=2) 

def opponentC13B4V_onClick():
    if opponentC13Combobox.get() in oneEnergyCards:
        if opponentC13B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC13B4V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC13Combobox.get() in noEnergyCards:
        if opponentC13B4V.get() == 1:
            subtractOpponentOnHand()
        if opponentC13B4V.get() == 0:
            addOpponentOnHand()
    elif opponentC13Combobox.get() in twoEnergyCards:
        if opponentC13B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC13B4V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC13B4V = IntVar()
opponentC13B4 = Checkbutton(opponentC13Buttons, variable=opponentC13B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC13B4V_onClick)
opponentC13B4.grid(row=0, column=3) 

#-------------------------------------------------------------------------------------------------------------#

opponentC14 = Frame(opponentC1Cards, width=70, height=40, highlightbackground="black", highlightthickness=1)
opponentC14.grid(row=1, column=3, padx=5, pady=5)

opponentC14Title = Frame(opponentC14, width=70, height=40)
opponentC14Title.grid(row=0, column=0)

def check_input(event):
    value = event.widget.get()

    if value == '':
        opponentC14Combobox['values'] = cards
    else:
        data = [] 
        for item in cards:
            if value.lower() in item.lower():
                data.append(item)

        opponentC14Combobox['values'] = data

opponentC14Combobox = ttk.Combobox(opponentC14Title, width=15)
opponentC14Combobox['values'] = cards
opponentC14Combobox.bind('<KeyRelease>', check_input)
opponentC14Combobox.grid(row=0, column=0)

opponentC14Buttons = Frame(opponentC14, width=70, height=40)
opponentC14Buttons.grid(row=1, column=0, padx=5, pady=5)

def opponentC14B1V_onClick():
    if opponentC14Combobox.get() in oneEnergyCards:
        if opponentC14B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC14B1V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC14Combobox.get() in noEnergyCards:
        if opponentC14B1V.get() == 1:
            subtractOpponentOnHand()
        if opponentC14B1V.get() == 0:
            addOpponentOnHand()
    elif opponentC14Combobox.get() in twoEnergyCards:
        if opponentC14B1V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC14B1V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC14B1V = IntVar()
opponentC14B1 = Checkbutton(opponentC14Buttons, variable=opponentC14B1V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC14B1V_onClick)
opponentC14B1.grid(row=0, column=0)

def opponentC14B2V_onClick():
    if opponentC14Combobox.get() in oneEnergyCards:
        if opponentC14B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC14B2V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC14Combobox.get() in noEnergyCards:
        if opponentC14B2V.get() == 1:
            subtractOpponentOnHand()
        if opponentC14B2V.get() == 0:
            addOpponentOnHand()
    elif opponentC14Combobox.get() in twoEnergyCards:
        if opponentC14B2V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC14B2V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC14B2V = IntVar()
opponentC14B2 = Checkbutton(opponentC14Buttons, variable=opponentC14B2V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC14B2V_onClick)
opponentC14B2.grid(row=0, column=1) 

def opponentC14B3V_onClick():
    if opponentC14Combobox.get() in oneEnergyCards:
        if opponentC14B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC14B3V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC14Combobox.get() in noEnergyCards:
        if opponentC14B3V.get() == 1:
            subtractOpponentOnHand()
        if opponentC14B3V.get() == 0:
            addOpponentOnHand()
    elif opponentC14Combobox.get() in twoEnergyCards:
        if opponentC14B3V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC14B3V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC14B3V = IntVar()
opponentC14B3 = Checkbutton(opponentC14Buttons, variable=opponentC14B3V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC14B3V_onClick)
opponentC14B3.grid(row=0, column=2) 

def opponentC14B4V_onClick():
    if opponentC14Combobox.get() in oneEnergyCards:
        if opponentC14B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC14B4V.get() == 0:
            addOpponentEnergy()
            addOpponentOnHand()
    elif opponentC14Combobox.get() in noEnergyCards:
        if opponentC14B4V.get() == 1:
            subtractOpponentOnHand()
        if opponentC14B4V.get() == 0:
            addOpponentOnHand()
    elif opponentC14Combobox.get() in twoEnergyCards:
        if opponentC14B4V.get() == 1:
            subtractOpponentEnergy()
            subtractOpponentEnergy()
            subtractOpponentOnHand()
        if opponentC14B4V.get() == 0:
            addOpponentEnergy()
            addOpponentEnergy()
            addOpponentOnHand()

opponentC14B4V = IntVar()
opponentC14B4 = Checkbutton(opponentC14Buttons, variable=opponentC14B4V, onvalue=1, offvalue=0, borderwidth=0, padx=0, command=opponentC14B4V_onClick)
opponentC14B4.grid(row=0, column=3) 

#-------------------------------------------------------------------------------------------------------------#

window.mainloop()

#-------------------------------------------------------------------------------------------------------------#