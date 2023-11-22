
import random

def Higher_Lower():

    print("Set a maximum for the random number (min. 10) : ")
    W = False
    given_range = ask_int_10()
    result:int = random.randint(1,given_range)
    attempt:int = 10
    att = 0

    while attempt > 0 and W != True:
        print( attempt,"attempt left! ")
        a = ask_int()
        W = Compare(a,result,attempt,W)
        attempt -= 1
        att += 1
    return Ending(W,attempt,result)


def Compare(a,result,attempts,W):
    if a == result:
        W = True
        return W
    elif a > result:
        return print("Lower")
    elif a < result:
        return print("Higher")



def Ending(Win,attempts,result):
    if Win == True:
        print("Well done you did it in ", attempts , " attempts.")
        print("Do you want to retry ?")
        retry:str = ask_str(['Y','N','y','n'])
        return try_again(retry)
    else:
        print("You loose the number was",result,".")
        print("Do you want to retry ?")
        retry:str = ask_str(['Y','N','y','n'])
        return try_again(retry)



def ask_int_10() -> int:
    while True :
        given_int = ask_int()
        if given_int >= 10:
            return given_int
        print("Please Choose a number greater than or equal to 10")

def ask_int() -> int:
    while True :
        given_int = input("Choose a number : ")
        if given_int.isdigit():
            given_int = int(given_int)
            return given_int

def ask_str(sPosibilities: list) -> str:
    while True:
        print("Please enter (",sPosibilities,")")
        given_input:str = input(": ")   
        for element in sPosibilities:
            if element == given_input:
                return given_input

def try_again(T):
    if T =='N' or T == 'n':
        return False
    else:
       return True

def Start(start): 
    while start == True:
        start = Higher_Lower()
    print("Game Over")
        

Start(True)


