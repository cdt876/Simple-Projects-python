import time
global gold
global apples
gold = 0
apples = 0

def start():
    print ("Hello and welcome!")
    name = input("What's your name:")
    print ("Welcome, ",name,"!")
    print ("The objective of this game is to collect apples.")
    print ("After collecting the apples you sell them.")
    choice = input("Do you want to play Y/N?")
    if choice == "Y":
        begin()
    if choice == "N":
        print ("Okay, bye...")

def begin():
    global apples
    global gold
    print ("Let's get started!")
    if gold > 99:
        print ("You have Won the game!")
        play = input("Do you want to play again Y/N?")
        if play == "Y":
            begin()
        if play == "N":
            print ("Congrats again!")
    pick = input("Do you want to pick an apple Y/N?")
    if pick == "Y":
        time.sleep(1)
        print ("You pick an apple.")
        apples = apples + 1
        print ("You currently have, ",apples," apples")
        begin()
    if pick == "N":
        sell = input("Do you want to sell your apples Y/N?")
        if sell == "Y":
            global gold
            global apples
            print ("You currently have, ",apples," apples")
            print ("You've have sold your apples.")
            gold = apples * 10
            apples = 0
            print ("Your gold is now:", gold)
            begin()
start()




