
import random



def Tictactoe():
    tab : list = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]

    while True:
        
        draw(tab)
        print("Joueur 1 : ")
        not_empty = False
        while not_empty == False:
            print("Selectionnez la ligne dans laquelle vous voulez jouer")
            p_lign:int = Ask_int_1_3()-1
            print("Selectionnez la colonne dans laquelle vous voulez jouer")
            p_column:int = Ask_int_1_3()-1
            not_empty = check_empty(1,[p_lign,p_column],tab)        
        tab[p_lign][p_column] = "X"
        Win:str = verif(tab)
        if Win != " ":
            break
        end = Check_Tab(tab)
        if end == True : 
            Win = "T"
            break

        draw(tab)
        p_bot = Bot(tab)
        tab[p_bot[0]][p_bot[1]] = "O"
        Win:str = verif(tab)
        if Win != " ":
            break
        end = Check_Tab(tab)
        if end == True : 
            Win = "T"
            break
         
    End(Win,tab)

def End(Who,tab):
    if Who == "X":
        draw(tab)
        return print("Player 1 Win !")
    elif Who == "O":
        draw(tab)
        return print("Player 2 Win !")
    elif Who == "T":
        draw(tab)
        return print("It's a Tie!")


def Check_Tab(tab):
    place_left = 0
    for i in tab : 
        for j in i :
            if j == " ":
                place_left += 1
    if place_left == 0:
        return True

def verif(tab:list):
    Win:str = " "
    for i in range(3):
        if tab[0][i] == tab[1][i] == tab[2][i] and tab[0][i] != " ":
            Win = tab[0][i]
        if tab[i][0] == tab[i][1] == tab[i][2] and tab[i][0] != " ":
            Win = tab[i][0]
    if tab[0][0] == tab[1][1] == tab[2][2] and tab[0][0] != " ":
        Win = tab[0][0]
    if tab[0][2] == tab[1][1] == tab[2][0] and tab[0][2] != " ":
        Win = tab[0][2]
    return Win


def draw(tab):
    print("    1   2   3")
    print("  ","-"*13)
    x = 1
    for ligne in tab:
        separator = " | "
        L = separator.join(ligne)
        print(x,"|",L,"|")
        print("  ","-"*13)
        x += 1



def check_empty(player,play,tab):
    while True:
            if tab[play[0]][play[1]] == " ":
                return True
            if player == 1:
                print("\n")
                draw(tab)
                print("Joueur ",player," :")
                print("Veuillez selectionner une case libre : ")
            return False
            
        

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

def Try_again(T):
    return T != 'N'


def Start(start): 
    while start == True:
        start = Tictactoe()
        print("\n Do you want to retry ?")
        retry:str = Ask_str(['Y','N'])
        start = Try_again(retry)
    print("Game Over")


def Check_Winning(tab,max,enn,ally):
    w = 0 
    for i in tab: 
        w = 0 
        for j in i :
            if j == ally:
                w = 0
            if j == enn : 
                w += 1
        if w == max :
            return ["l", tab.index(i)]
    w = 0 
    for i in range(3):
        w = 0 
        for j in range(3):
            if tab[j][i] == ally:
                w = 0
            if tab[j][i] == enn:
                w += 1
        if w == max :
            return ["c",i]
    w = 0 
    for i in range(3):
        if tab[i][i] == enn : 
            w +=1
        elif tab[i][i] == ally :
            w = 0
    if w == max:
        print("BOUH") 
        return ["d",1]
    
    j =  2
    w = 0 
    for i in range(3):
        if tab[i][j] == enn : 
            w +=1
        elif tab[i][j] == ally :
            w = 0
        j -=1
    if w == max:
        print("BOUH")  
        return ["d",2]
        
    return [" ",0]
    

def Bot(tab):
    not_empty = False
    Def = Check_Winning(tab,2,"X","O")
    Att = Check_Winning(tab,2,"O","X")
    
    if Att[0] != " " :
        while not_empty == False:
            if Att[0] == "l":
                l = Att[1]
                c = random.randint(0,2)
            elif Att [0] == "c":
                l = random.randint(0,2)
                c = Att[1]
            elif  Att[0] == "d":
                if Att[1] == 1:
                    l = random.randint(0,2)
                    c = l
                elif Att[1] == 2:
                    l = random.randint(0,2)
                    c = 2 - l
            b_play = [l,c]
            not_empty = check_empty(2,b_play,tab)

    elif Def[0] != " ":
        while not_empty == False:
            if Def[0] == "l":
                l = Def[1]
                c = random.randint(0,2)
            elif Def [0] == "c":
                l = random.randint(0,2)
                c = Def[1]
            elif  Def[0] == "d":
                if Def[1] == 1:
                    l = random.randint(0,2)
                    c = l
                elif Def[1] == 2:
                    l = random.randint(0,2)
                    c = 2 - l
            b_play = [l,c]
            not_empty = check_empty(2,b_play,tab)
    else:
        while not_empty == False :
            l:int = random.randint(0,2)
            c:int = random.randint(0,2)
            b_play = [l,c]
            not_empty = check_empty(2,b_play,tab)
    return [l,c]


Start(True)
