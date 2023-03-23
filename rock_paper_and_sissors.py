import random



def play ():     
    bot = 0 
    you = 0
    i = 0

    while i >= 0:
        print(f"shift: {i} \npoints: \nplayer: {you} \ncomputer: {bot}\n")
        i += 1
        
        if score():
            print()
            you += 1
            
        else:
            bot += 1
            
        if bot > you and bot == 2: 
            
            print(f"¡¡¡COMPUTER WIN!!! \nshift: {i}  \npoints: \nplayer: {you} \ncomputer: {bot}\n ")
            reset = input("do you want to play again: ")
            if reset == "yes":
                i = 0
                you = 0
                bot = 0
            if reset == "no":     
                print("ok... see you later 🥺 ")

        if bot < you and you == 2: 
            print(f"¡¡¡PLAYER WIN!!!: \nshift{i} \npoints: \nplayer: {you} \ncomputer: {bot}\n")
            reset = input("Do you want to play again: ")
            reset.lower()
            if reset == "yes":
                i = 0
                you = 0
                bot = 0
            if reset == "no":           
                print("Ok... see you later 🥺")
                break
                

def score  (): 
        player = input("`r` for rock, `p` for paper, `s` for sissors: ")
        player.lower()
        
        opponent = random.choice(["r","s","p"])
        if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
            return True

print(play())