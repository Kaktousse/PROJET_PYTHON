def Tictactoe():
    tab : list = [
        [ [],"|",[],"|",[] ],
        [ [],"|",[],"|",[] ],
        [ [],"|",[],"|",[] ]
    ]
    end = False
    while end != True :
        print(tab,"\n")
        print("Joueur 1 : Selectionnez la ligne dans laquelle vous voulez jouer")
        p1_lign:int = Ask_int_1_3()-1
        print("Joueur 1 : Selectionnez la colonne dans laquelle vous voulez jouer")
        p1_column:int = Ask_int_1_3()-1
        p1_play : list = [p1_lign,p1_column]
        tab[p1_play[0],p1_play[1]].append("X")

        print("\n Joueur 2 : Selectionnez la ligne dans laquelle vous voulez jouer")
        p2_lign:int = Ask_int_1_3()-1
        print("Joueur 2 : Selectionnez la colonne dans laquelle vous voulez jouer")
        p2_column:int = Ask_int_1_3()-1
        p2_play : list = [p2_lign,p2_column]
        tab[p2_play[0],p2_play[1]] = "O"
        print(tab)


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
        
Tictactoe()