import random
def mainscreen():
    name=input("enter your Name:")
    print("WELCOME, {}! TO A SIMPLE WORD SEARCH GAME".format(name))
    print("GAME RULES:")
    print("In this game, your challenge is to find a word related to the given topic. Stay attentive, be patient, and aim to discover the word within 6 attempts.")
    print("Let's dive into the game. Best of luck, {}!".format(name))
    print("****************************************************************************************************")
    print("Try to guess the word in 6 tries or fewer.")
    wsearch()
    print()
def wsearch():
    word=random.choice(["darling","mirchi","pournami","bahubali","chatrapathi","varsham","chakram","bujjigaadu","eshwar","saaho","adaviramudu","mrperfect","munna","yogi","ekniranjan","billa","rebel"])
    validletters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    turns=10
    guessed=""
    while(len(word)>0):
        msg=""
        missed=0
        for letter in word:
            if(letter in guessed):
                msg=msg+letter
            else:
                msg=msg+"_"+" "
                missed=missed+1
        if(msg==word):
            print(msg)
            print("You are correct ,the word was:",word)
            print("well done my boy i am impressed")
            print("plz rate this game")
            print("* * * * *")
            input()
            print("thanks for your response!! :) :) :)")
            break
        print("guess the word:",msg)
        guess=input()
        if(guess in validletters):
            guessed+=guess
        else:
            print("enter a valid letter:")
            guess=input()
        if(guess not in word):
            turns=turns-1
            if(turns==9):
                print("soryy worng one!! you have 5 turns")
            if(turns==8):
                print("soryy worng one!! you have 4 turns")
            if(turns==7):
                print("soryy worng one!! you have 3 turns")
            if(turns==6):
                print("soryy worng one!! you have 2 turns")
            if(turns==5):
                print("soryy worng one!! you have 1 turn remaining")
            if(turns==4):
                print("sorry no more turns remaining")
                print("you have to fail to guess the word:",word)
                print("plz rate this game")
                print("* * * * *")
                input()
                print("thanks for your response!! :) :) :)")
                break
            # if(turns==3):
            #     print("soryy worng one!! you have 5 turns")
            # if(turns==2):
            #     print("soryy worng one!! you have 5 turns")
            # if(turns==1):
            #     print("you have to fail to guess the word:",word)
            #     break

if __name__=="__main__":
    mainscreen()
