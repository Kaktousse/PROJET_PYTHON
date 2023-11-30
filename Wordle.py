
import linecache
import random
Grid_length = 5

def Wordle(grid:list[list[str]], word:list[str,str,str,str,str]):
    attempt = 0
    answer = []
    for count in range(len(grid[0])):
        answer.append(" ")
    
    while attempt < len(grid):
        given_word = Ask_str()
        for count in range(len(answer)):
            answer[count] = " "
        count = 0
        for letter in given_word :
            answer[count] = letter
            count +=1
        
        colored_answer = Coloring(word,answer)
        grid[attempt] = colored_answer
        Drawgrid(grid)
        win = Checkwinning(word,answer)
        attempt +=1
        if win:
            print("You won in",attempt,"!")
            return       
    print("You Loose the word was",Drawword(word),".")
    return 



def Checkwinning(word:list[str],given_word:list[str]) -> bool:
    res = 0
    for count in range(len(given_word)):
        if given_word[count] == word[count]:
            res+=1
    if res == len(given_word):
        return True
    return False    
      


def Coloring(original_word:list[str],original_given_word:list[str]):
    word = original_word.copy()
    given_word = original_given_word.copy()    
    answer = ["","","","",""]
    letters_still = {}
    for letter in word:
        letters_still[letter] = 0
    for letter in word:
        letters_still[letter] += 1

    for count in range(len(given_word)):
        if given_word[count] == word[count]:
            answer[count] = "\033[94m" + given_word[count] + "\033[0m"
            letters_still[given_word[count]] -= 1
            given_word[count] = " "

    for count in range(len(given_word)):
        if given_word[count] in letters_still and letters_still[given_word[count]] > 0:
            answer[count] = "\033[93m" + given_word[count] + "\033[0m"
            letters_still[given_word[count]] -= 1
            given_word[count] = " "
        elif given_word[count] != " ":
            answer[count] = "\033[90m" + given_word[count] + "\033[0m"        

    return answer


def Creategrid(word_length:int,attempt:int) -> list[list[str]]:
    grid = []
    for lign in range(attempt):
        new_lign = []
        for column in range(word_length):
            new_lign.append(" ")
        grid.append(new_lign)
    return grid


def Drawgrid(grid: list[list[str]]):
    word_length =  len(grid[0])
    print("\t","-"*(4*word_length))
    count :int = 1
    for ligne in grid:
        separator = " | "
        L = separator.join(ligne)
        print("\t |",L,"|")
        print("\t", "-"*(4*word_length))


def Drawword(word:list[str,str,str,str,str]) -> bool:
    separator = ""
    result = separator.join(word)
    return result


def Createword():
    with open(r"WORD.txt", 'r') as word_line:
        lines = len(word_line.readlines())
    raw_word = linecache.getline("mot.txt", random.randint(1,lines))
    word = ["","","","",""]
    count = 0
    for letter in raw_word:
        word[count] = letter
        count+=1
        if count == 5:
            break
    return word

def Ask_str() -> str:
    while True:
        print("Choissiez un mot de 5 lettres")
        given_input:str = input(": ")
        if given_input.isalpha():
            existing = Search_str(given_input)
            if existing == True:   
                if len(given_input) == 5:
                    return given_input

def Search_str(given_input:str) -> bool:
    all_words = []
    with open(r"WORD.txt", 'r') as file:
        lines = len(word_line.readlines())
        for i in range(0,lines):
            all_words.append(file.getline(i))



def Ask_retry(sPossibilities: list[str,str]) -> bool:
    while True:
        print("Please enter ", sPossibilities,")")
        given_input:str = input(": ")   
        for element in sPossibilities:
            if element == given_input:
                return given_input  

def Try_again(T:str) -> bool:
    return T != 'N'

def Start(start:bool): 
    while start == True:
        grid = Creategrid(5,6)
        Drawgrid(grid)
        word = Createword()
        Wordle(grid,word)
        print("\n Do you want to retry ?")
        retry:str = Ask_retry(['Y','N'])
        start: bool = Try_again(retry)
    print("Game Over")

Start(True)