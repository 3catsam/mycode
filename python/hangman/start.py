# Filename:start.py
#!/usr/bin/python3
import os

import position

print("Welcome to Hang Man!!!")
ORIGIN = input("Please write down your WROD:")
os.system('clear')
print("The word has", len(ORIGIN), "alphabets.")
TIMES = 1
ERROR = 0


while TIMES <= 6:
    if TIMES == 1:
        TAG = "st"
    elif TIMES == 2:
        TAG = "nd"
    elif TIMES == 3:
        TAG = "rd"
    else:
        TAG = "th"
    print("Now please do your", str(TIMES) + TAG, "try:")
    print("(Make sure there is only one alphabet)")
    GUESS = input()

    while len(GUESS) != 1:
        print("Please try again:")
        print("(Make sure there is only one alphabet)")
        GUESS = input()

    if position.checkpos(GUESS, ORIGIN) == 1:
        RESULT = input("Please guess the WROD:")
        if RESULT == ORIGIN:
            print('\033[1;32;40m', "Congratulations,you win!!!")
            print('\033[0m')
            exit()
        print("Sorry,you lost one chance.")
        TIMES = TIMES + 1


print('\033[1;31;40m', "Sorry,you are killed!")
print('\033[1;31;40m', "GAME OVER")
print('\033[0m')
exit()
