import random


def Shifumi(round):
    print("Let's play Rock, Paper Scissors !")
    choice:list = ["rock","paper","scissors"]
    Wins:list = [0,0]
    for i in range(round):
        Bot:int = random.randint(0,2)
        print("Choose : Rock (1), Paper (2) or Scissors (3) .")
        player:int = ask_int_1_3() - 1
        Winner = Win(Bot,player,Wins)
        print(choice[Bot],"vs",choice[player],Winner)
    Results:str = Win(Bot,player,Wins,True)
    print(Results,Wins[0],"/",Wins[1],"!")
    print("Do you want to retry ?")
    retry:str = ask_str(['Y','N'])
    try_again(retry)



def Win(A,B,Points,end):
    if end == True:
        if Points[0] == Points[1]:
            return "It's a Tie "
        elif Points[0]>Points[1]:
            return "You Win "
        else :
            return "You Loose "
        
    else:
        if A == B :
            return "It' s a Tie"
        elif (A == 0 and B == 1) or (A == 1 and B == 2) or (A == 2 and B == 0):
            Points[0]+=1
            return "You Win !"
        elif (B == 0 and A == 1) or (B == 1 and A == 2) or (B == 2 and A == 0):
            Points[1]+=1
            return "You Loose !"


def ask_int_1_3():
    while True :
        given_int = input("Choose a number : ")
        if given_int.isdigit():
            given_int = int(given_int)
            if given_int > 0 and given_int < 4: 
                return given_int
             
def ask_int():
    while True :
        given_int = input("Choose a number : ")
        if given_int.isdigit():
                given_int = int(given_int)
                return given_int

def ask_str(sPosibilities: list):
    while True:
        print("Please enter ",sPosibilities,")")
        given_input:str = input(": ")   
        for element in sPosibilities:
            if element == given_input:
                return given_input


def try_again(T):
    if T =='N' or T == 'n':
        Start(False)
    else:
        Start(True)

def Start(restart): 
    start = True
    while start == True:
        if restart ==False:
            break
        print("How many rounds do you want to do ?")
        R = ask_int()
        Shifumi(R)
    print("Game Over")

Start(True)