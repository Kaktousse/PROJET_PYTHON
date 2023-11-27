
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
        Win:bool = Check_Winning(grid,3,"X","O")
        if Win : 
            Winner = "X"
            break
        end = Check_grid(grid)
        if end == True : 
            Winner = "T"
            break

        draw(grid)
        p_bot = Bot(grid)
        grid[p_bot[0]][p_bot[1]] = "O"
        Win:bool = Check_Winning(grid,3,"O","X")
        if Win : 
            Winner = "O"
            break
        end = Check_grid(grid)
        if end == True : 
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


def Check_Winning(grid,max,ally,enn):
    w = 0
    play = True

    RAND = []

 
    for i in range(3): 
        w = 0 
        for j in range(3) :
            if grid[i][j] == enn:
                w = 0
            elif grid[i][j] == ally : 
                w += 1
            if grid[i][j] == " ":
                RAND.append([i,j])
        if w >= max :
    
            return play


    w = 0 
    for i in range(3):
        w = 0 
        for j in range(3):
            if grid[j][i] == enn:
                w = 0
            elif grid[j][i] == ally:
                w += 1
            if grid[j][i] == " ":
                RAND.append([j,i])
        if w >= max :
    
            return play


    w = 0
    for i in range(3):
        if grid[i][i] == ally : 
            w +=1
        elif grid[i][i] == enn :
            w = 0
        if grid[i][i] == " " : 
            RAND.append([i,i])
    if w >= max:

        return play

    j =  2
    w = 0 
    for i in range(3):
        if grid[i][j] == ally : 
            w +=1
        elif grid[i][j] == enn :
            w = 0
        if grid[i][j] == " " :
            RAND.append([i,j])
        j -=1
    if w >= max: 

        return play
    if enn == 5:
        return RAND

    return False
    
# --- Bot --- #

def Bot(grid):
    not_empty = False
    Def = Check_Winning(grid,2,"X","O")
    Att = Check_Winning(grid,2,"O","X")
    rand = Check_Winning(grid,1," ",5)
    
    if Att != False :
        b_play = Att
    elif Def != False:
        b_play = Def
    else:
        rand_inx = random.randint(0,len(rand)-1)
        b_play = rand[rand_inx]
    return b_play


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
