import random



def Shifumi():

    tab_result : list = [  
                            ["tie"      , "you win"  , "you loose" ],
                            ["you loose", "tie"      , "you win"   ],
                            ["you win"  , "you loose", "tie"       ]
                        ]
    
    tab_points : list = [
                        [ 2  , 0  , 1 ],
                        [ 1  , 2  , 0 ],
                        [ 0  , 1  , 2 ]
                        ] 
    
    print("Let's play Rock, Paper Scissors !")
    print("How many rounds do you want to do ?")
    round = Ask_int()
    choice:list = ["rock","paper","scissors"]
    Wins:list = [0,0,0]
    Who_Win : list = ["It's a Tie","You win","You loose"]
    for i in range(round):

        Bot:int = random.randint(0,2)
        print("\n Choose : Rock (1), Paper (2) or Scissors (3) .")
        player:int = Ask_int_1_3() - 1
        Winner = tab_result[Bot][player]
        Wins[tab_points[Bot][player]] += 1
        print(choice[Bot],"vs",choice[player],Winner)
    
    Results:str = Win(Wins)
    print(Who_Win[Results],Wins[0],"/",Wins[1],"!")



def Win(Points):
    x = Points[0] ; y = Points[1]
    res = x - y
    while res != 0 and res!= 1 and res!= -1 :
        y = abs(res)
        res = res // y
    return int(res)


def Ask_int_1_3():
    while True :
        given_int = input("Choose a number : ")
        if given_int.isdigit():
            given_int = int(given_int)
            if given_int > 0 and given_int < 4: 
                return given_int
             
def Ask_int():
    while True :
        given_int = input("Choose a number : ")
        if given_int.isdigit():
                given_int = int(given_int)
                return given_int

def Ask_str(sPossibilities: list):
    while True:
        print("Please enter ", sPossibilities,")")
        given_input:str = input(": ")   
        for element in sPossibilities:
            if element == given_input:
                return given_input


def Try_again(T):
    return T != 'N'

def Start():
    start: bool = True 
    while start == True:
        Shifumi()
        print("\n Do you want to retry ?")
        retry:str = Ask_str(['Y','N'])
        start = Try_again(retry)
    print("Game Over")



Start()



