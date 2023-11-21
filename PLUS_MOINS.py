
import random

def Higher_Lower():

    print("Set a maximum for the random number (min. 10) : ")

    given_range = ask_int_10()
    result:int = random.randint(1,given_range)
    attempt:int = 10
    att = 0

    while attempt > 0:
        print( attempt,"attempt left! ")
        a = ask_int()
        Compare(a,result,attempt)
        attempt -= 1
        att += 1
    Ending(False,attempt,result)


def Compare(a,result,attempts):
    if a == result:
        return Ending(True,attempts,result)
    elif a > result:
        return "Lower"
    elif a < result:
        return "Higher"



def Ending(Win,attempts,result):
    if Win == True:
        print("Well done you did it in ", attempts , " attempts.")
        print("Do you want to retry ?")
        retry:str = ask_str(['Y','N','y','n'])
        try_again(retry)
    else:
        print("You loose the number was",result,".")
        print("Do you want to retry ?")
        retry:str = ask_str(['Y','N','y','n'])
        try_again(retry)



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
        Start(False)
    else:
        Start(True)

def Start(restart): 
    start = True
    while start == True:
        if restart == False:
            break
        start = Higher_Lower()
    print("Game Over")
        

Start(True)


