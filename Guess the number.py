# Author Gourish mokashi
# 29/06/2022

# Guess th number

n = 18
g = 1

while True:
    if g <= 9:
        print("Guess left-", 10 - g, "\nGuess the the: ")
        i = int(input())
        g = g + 1
        if i == n:
            g = g - 1
            print("Congrats! your guessed correct number in ", g, "guesses")
            break
        else:
            continue
    else:
        print("Sorry! your chances are done.")
        break
