import sys

print("Bienvenue dans mon jeu du morpion")
print(" \n The player X begin!")

grille = [0 for i in range(9)]
player_sign = 'X'
win = False

x = ('X','X','X')
o = ('O','O','O')

def afficher_grille():
    print('\n',grille[0],"|", grille[1], ("|"), grille[2], '\n',
          grille[3],"|", grille[4], ("|"), grille[5], '\n',
    grille[6],"|", grille[7], ("|"), grille[8])
    player()


def pos_ok(choose):
    global grille, player_sign
    if grille[choose - 1] == 0:
        grille[choose - 1] = player_sign
        if player_sign == 'X':
            player_sign = 'O'
        else :
            player_sign = 'X'
        afficher_grille()
    else:
        print("\nYou made a mistake, this position is already taken, pls try again\n")
        player()
        if player_sign == 'X':
            player_sign = 'O'


def check_win():
    global player_sign
    if win == True:
        if player_sign == 'X':
            player_sign = 'O'
        else:
            player_sign = 'X'
        print(f"\n The player {player_sign} had won")
    rejouer = input("Do you want to play again? (Yes - No) ")
    restart(rejouer)


def restart(rejouer):
    global grille, player_sign
    if rejouer == "Yes":
        grille = [0 for i in range(9)]
        player_sign = 'X'
        print("\nNew Game : The player X start")
        afficher_grille()
    else:
        sys.exit()

def check_colonnes(colonnes):
    global win
    if (colonnes[0] == (x) or colonnes[0] == (o)) or (colonnes[1] == (x) or colonnes[1] == (o)) or (colonnes[2] == (x)
            or colonnes[2] == (o)):
        win = True
        check_win()
    else:
        lignes = (
        (grille[0], grille[1], grille[2]), (grille[3], grille[4], grille[5]), (grille[6], grille[7], grille[8]))
        check_lignes(lignes)


def check_lignes(lignes):
    global win
    if (lignes[0] == (x) or lignes[1] == (o)) or (lignes[1] == (x) or lignes[1] == (o)) or (lignes[2] == (x)
            or lignes[2] == (o)):
        win = True
        check_win()
    else:
        diago = ((grille[0], grille[4], grille[8]), (grille[2], grille[4], grille[6]))
        check_diago(diago)

def check_diago(diago):
    global win
    if (diago[0] == (x) or diago[0] == (o)) or (diago[1] == (x) or diago[1] == (o)):
        win = True
        check_win()
    else:
        pass

def player():
    colonnes = ((grille[0], grille[3], grille[6]),(grille[1], grille[4], grille[7]),(grille[2], grille[5], grille[8]))
    check_colonnes(colonnes)
    if grille.count(0) == 0 and win == False:
        print("Its a Tie game")
        sys.exit()
    choose = int(input("Choose a position between 1 and 9 : "))
    pos_ok(choose)


afficher_grille()