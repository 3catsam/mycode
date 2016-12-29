

# Filename:position.py
def checkpos(INPUT, WORD):
    pos = 0
    hit = 0
    while pos < len(WORD):
        if INPUT == WORD[pos]:
            if pos + 1 == 1:
                tag = "st"
            elif pos + 1 == 2:
                tag = "nd"
            elif pos + 1 == 3:
                tag = "rd"
            else:
                tag = "th"
            print("The alphabet", INPUT, "is at",
                  str(pos + 1) + tag, "position")
            hit = hit + 1
        pos = pos + 1

    if hit == 0:
        return 1
        RESULT = input("Please guess the WROD:")
        if RESULT == WORD:
            print('\033[1;32;40m', "Congratulations,you win!!!")
            print('\033[0m')

            exit()
