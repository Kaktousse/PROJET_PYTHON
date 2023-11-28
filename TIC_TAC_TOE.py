
import random

Grid_length: int = 3
WINNING_SYMBOL_COUNT: int = 3




def Tictactoe(grid):


    while True:
        
        draw(grid)
        print("Joueur 1 : ")
        not_empty : bool = False
        while not_empty == False:
            print("Selectionnez la ligne dans laquelle vous voulez jouer")
            p_lign:int = Ask_int_1_3()-1
            print("Selectionnez la colonne dans laquelle vous voulez jouer")
            p_column:int = Ask_int_1_3()-1
            not_empty : bool = check_empty(1,[p_lign,p_column],grid)        
        grid[p_lign][p_column] = "X"
        Win: bool = CheckWinning(grid,"X",3)
        if Win : 
            Winner: str = "X"
            break
        if Check_grid(grid):
            Winner: str = "T"
            break

        draw(grid)
        p_bot: tuple[int, int] = GetBotMove(grid)
        grid[p_bot[0]][p_bot[1]] = "O"
        Win:bool = CheckWinning(grid,"O",3)
        if Win : 
            Winner: str = "O"
            break
        if Check_grid(grid):
            Winner: str = "T"
            break
         
    End(Winner,grid)


# --- The grid --- #

def creategrid(Grid_length:int) -> list[list[str]]:
    grid = []
    for lign in range(Grid_length):
        new_lign = []
        for column in range(Grid_length):
            new_lign.append(" ")
        grid.append(new_lign)
    draw(grid,Grid_length)

    return grid



def draw( grid: list[list[str]]):
    Index = []
    Grid_length =  len(grid)
    for i in range(1,Grid_length+1):
        if i < 10:
            j = " " + str(i)   
        else:
            j = str(i)
        Index.append(j)
    In ="  ".join(Index)
    print("\t ",In)
    print("\t","-"*(4*Grid_length))
    count :int = 1
    for ligne in grid:
        separator = " | "
        L = separator.join(ligne)
        print(" ",count,"\t","|",L,"|")
        print("\t", "-"*(4*Grid_length))
        count += 1


def check_empty(player: int,play: list,grid: list[list[str]]) -> bool:
    while True:
            if grid[play[0]][play[1]] == " ":
                return True
            if player == 1:
                print("\n")
                draw(grid)
                print("Joueur ",player," :")
                print("Veuillez selectionner une case libre : ")
            return False
            
def Check_grid(grid : list[list[str]]) -> bool:
    place_left : int = 0
    for lign in grid : 
        for column in lign :
            if column == " ":
                return False
    return True

# --- All Ask --- #

def Ask_int_1_3() -> int:
    while True :
        given_int:int = Ask_int()
        if given_int > 0 and given_int < 4: 
            return given_int
        print("Entrez un chiffre entre 1 et 3.")
             
def Ask_int() -> int:
    while True :
        given_int: str = input("Choississez un chiffre : ")
        if given_int.isdigit():
                given_int :int = int(given_int)
                return given_int

def Ask_str(sPossibilities: list) -> str:
    while True:
        print("Please enter ", sPossibilities,")")
        given_input:str = input(": ")   
        for element in sPossibilities:
            if element == given_input:
                return given_input


# --- --- #


def GetAvailableTiles(grid : list[list[str]]) -> list[tuple[int, int]]:
    
    Availabletiles :list  = []

    for lign in range(3) : 
        for column in range(3) : 
            if grid[lign][column] == " ":
                Availabletiles.append([lign,column])

    return Availabletiles


def CheckWinning(grid: list[list[str]], symbol: str, winning_symbol_count: int) -> bool:
    
    count:int = 0
    for lign in range(3):
        count:int = 0
        for column in range(3):
            if grid[lign][column] == symbol:
                count += 1
                if count == winning_symbol_count: 
                    return True

    count:int = 0
    for column in range(3):
        count:int = 0
        for lign in range(3):
            if grid[lign][column] == symbol:
                count += 1
                if count == winning_symbol_count:
                    return True
    
    count:int = 0
    for lign in range(3):
        column = lign
        if grid[lign][column] == symbol:
            count += 1
            if count == winning_symbol_count:
                return True
    
    count:int = 0
    for lign in range(3):
        column = 2-lign
        if grid[lign][column] == symbol:
            count +=1
            if count == winning_symbol_count:
                return True
    
    return False



# --- Bot --- #

def PlayBot(grid: list[list[str]],symbol:str) -> tuple[int, int]:
    Availabletiles: list[tuple[int,int]] = GetAvailableTiles(grid)
    for tile in Availabletiles:
        grid[tile[0]][tile[1]] = symbol
        if CheckWinning(grid,symbol,3):
            grid[tile[0]][tile[1]] = " "
            return tile
        
        grid[tile[0]][tile[1]] = " "

    return None, None



def GetBotMove(grid: list[list[str]]) -> tuple[int, int]:

    Availabletiles: list[tuple[int,int]] = GetAvailableTiles(grid)
    Att: tuple[int, int] = PlayBot(grid,"O")
    Def: tuple[int, int] = PlayBot(grid,"X")
    Random_play_index: int = random.randint(0,len(Availabletiles)-1)
    
    if Att != [None, None] :
        return Att
    
    if Def != [None, None]:
        return Def

    return Availabletiles[Random_play_index]


# --- Running the Game --- #

def End(Winner : str,grid: list[list[str]]):
    if Winner == "X":
        draw(grid)
        print("Player 1 Win !")
    elif Winner == "O":
        draw(grid)
        print("Player 2 Win !")
    elif Winner == "T":
        draw(grid)
        print("It's a Tie!")

def Try_again(T:str) -> bool:
    return T != 'N'

def Start(start:bool,Grid_length:int): 
    while start == True:
        grid = creategrid(Grid_length)
        Tictactoe(grid)
        print("\n Do you want to retry ?")
        retry:str = Ask_str(['Y','N'])
        start: bool = Try_again(retry)
    print("Game Over")


Start(True,Grid_length)