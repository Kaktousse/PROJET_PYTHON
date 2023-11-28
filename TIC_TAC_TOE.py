
import random

def Tictactoe():
    grid : list = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]

    while True:
        
        draw(grid)
        print("Joueur 1 : ")
        not_empty = False
        while not_empty == False:
            print("Selectionnez la ligne dans laquelle vous voulez jouer")
            p_lign:int = Ask_int_1_3()-1
            print("Selectionnez la colonne dans laquelle vous voulez jouer")
            p_column:int = Ask_int_1_3()-1
            not_empty = check_empty(1,[p_lign,p_column],grid)        
        grid[p_lign][p_column] = "X"
        Win:bool = CheckWinning(grid,"X",3)
        if Win : 
            Winner = "X"
            break
        if Check_grid(grid):
            Winner = "T"
            break

        draw(grid)
        p_bot = Bot(grid)
        grid[p_bot[0]][p_bot[1]] = "O"
        Win:bool = CheckWinning(grid,"O",3)
        if Win : 
            Winner = "O"
            break
        if Check_grid(grid):
            Winner = "T"
            break
         
    End(Winner,grid)


# --- The grid --- #

def draw(grid):
    print("    1   2   3")
    print("  ","-"*13)
    x = 1
    for ligne in grid:
        separator = " | "
        L = separator.join(ligne)
        print(x,"|",L,"|")
        print("  ","-"*13)
        x += 1


def check_empty(player,play,grid):
    while True:
            if grid[play[0]][play[1]] == " ":
                return True
            if player == 1:
                print("\n")
                draw(grid)
                print("Joueur ",player," :")
                print("Veuillez selectionner une case libre : ")
            return False
            
def Check_grid(grid):
    place_left = 0
    for i in grid : 
        for j in i :
            if j == " ":
                return False
    return True

# --- All Ask --- #

def Ask_int_1_3():
    while True :
        given_int = Ask_int()
        if given_int > 0 and given_int < 4: 
            return given_int
        print("Entrez un chiffre entre 1 et 3.")
             
def Ask_int():
    while True :
        given_int = input("Choississez un chiffre : ")
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


# --- --- #


def GetAvailableTiles(grid) -> list[tuple[int, int]]:
    
    Availabletiles :list  = []

    for lign in range(3) : 
        for column in range(3) : 
            if grid[lign][column] == " ":
                Availabletiles.append([lign,column])

    return Availabletiles


def CheckWinning(grid: list[list[str]], symbol: str, winning_symbol_count: int) -> bool:
    
    count = 0
    for lign in range(3):
        count = 0
        for column in range(3):
            if grid[lign][column] == symbol:
                count += 1
        if count == winning_symbol_count: 
            return True

    count = 0
    for column in range(3):
        count = 0
        for lign in range(3):
            if grid[lign][column] == symbol:
                count += 1
        if count == winning_symbol_count:
            return True
    
    count = 0
    for lign in range(3):
        column = lign
        if grid[lign][column] == symbol:
            count += 1
    if count == winning_symbol_count:
        return True
    
    count = 0
    for lign in range(3):
        column = 2-lign
        if grid[lign][column] == symbol:
            count +=1
    if count == winning_symbol_count:
        return True
    
    return False



# --- Bot --- #

def PlayBot(grid,symbol):
    Availabletiles = GetAvailableTiles(grid)
    editedgrid = grid
    for tile in Availabletiles:
        editedgrid[tile[0]][tile[1]] = symbol
        if CheckWinning(editedgrid,symbol,3):
            editedgrid[tile[0]][tile[1]] = " "
            return tile
        else:
            editedgrid[tile[0]][tile[1]] = " "
    return False



def Bot(grid):

    Availabletiles = GetAvailableTiles(grid)
    Att = PlayBot(grid,"O")
    Def = PlayBot(grid,"X")
    random_play_index: list = random.randint(0,len(Availabletiles)-1)
    
    if Att != False :
        return Att
    elif Def != False:
        return Def
    else:
        random_play = Availabletiles[random_play_index]
        return random_play


# --- Running the Game --- #

def End(Who,grid):
    if Who == "X":
        draw(grid)
        print("Player 1 Win !")
    elif Who == "O":
        draw(grid)
        print("Player 2 Win !")
    elif Who == "T":
        draw(grid)
        print("It's a Tie!")

def Try_again(T):
    return T != 'N'

def Start(start): 
    while start == True:
        start = Tictactoe()
        print("\n Do you want to retry ?")
        retry:str = Ask_str(['Y','N'])
        start = Try_again(retry)
    print("Game Over")



Start(True)
