import random



def Shifumi():

    tab_win : list = [  [""          , "Rock" , "Paper", "Scissors"         ],
                        [" Rock "     , "Tie"  , "You win"  , "You loose"   ],
                        [" Paper "    , "You loose", "Tie"  , "You win"     ],
                        [" Scissors " , "You win"  , "You loose", "Tie"     ]]
    tab_points : list = [  [""          , "Rock" , "Paper", "Scissors"         ],
                        [" Rock "     , 2  , 0  , 1   ],
                        [" Paper "    , 1, 2  , 0     ],
                        [" Scissors " , 0  , 1, 2     ]] 
    print("Let's play Rock, Paper Scissors !")
    print("How many rounds do you want to do ?")
    round = Ask_int()
    choice:list = ["rock","paper","scissors"]
    Wins:list = [0,0,0]

    for i in range(round):

        Bot:int = random.randint(1,3)
        print("Choose : Rock (1), Paper (2) or Scissors (3) .")
        player:int = Ask_int_1_3()
        Winner = tab_win[player][Bot]
        print(tab_points[player][Bot])
        Wins[tab_points[player][Bot]] += 1
        print(choice[Bot-1],"vs",choice[player-1],Winner)

    Results:str = Win(Wins)
    print(Results,Wins[0],"/",Wins[1],"!")



def Win(Points,):
    if Points[0] == Points[1]:
        return "It's a Tie "
    elif Points[0]>Points[1]:
        return "You Win "
    else :
        return "You Loose "


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
        print("Do you want to retry ?")
        retry:str = Ask_str(['Y','N'])
        start = Try_again(retry)
    print("Game Over")



Start()