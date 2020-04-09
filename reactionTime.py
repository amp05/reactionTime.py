#reactionTime.py for phys143


import time, random, os

clear = lambda: os.system('cls') #change to 'cls' to 'clear' for linux
reset = ''

def reactionTime():
    clear()
    print("reaction time test - amp \nwhen it says stop, press enter")
    input("press enter to start")
    clear()
    interval = random.uniform(1, 10)
    a = time.time()
    time.sleep(interval)
    print("stop")
    input()
    b = time.time()
    print("Reaction time is " + str(((b-a) - interval)*1000) + " ms")

while reset != 'n':
    reactionTime()
    reset = input("Restart (y/n)? ")
