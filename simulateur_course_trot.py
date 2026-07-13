#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

"""
Simulateur de course de trot
Séverine Hori Maitrehut

"""


# Tuple qui donne la distance parcourue en fonction de la vitesse
# Indice 0 = vitesse 0, indice 6 = vitesse 6
tuple_distance = (0, 23, 46, 69, 92, 115, 138)
array_change_speed_with_dice_roll=[[0, +1, +1, +1, +2, +2],
                                    [0, 0, +1, +1, +1, +2],
                                    [0, 0, +1, +1, +1, +2],
                                    [-1, 0, 0, +1, +1, +1],
                                    [-1, 0, 0, 0, +1, +1],
                                    [-2, -1, 0, 0, 0, +1],
                                    [-2, -1, 0, 0, 0, "DQ"]
                                   ]

CONST_TIERCE, CONST_QUARTE, CONST_QUINTE = "Tiercé", "Quarté", "Quinté"

def is_entry_int_ok(saisie, min_int, max_int):
    """ Fonction qui vérifie la saisie d'un numérique, entre min_int et max_int    """
    cleaned_saisie = saisie.strip()
    if not cleaned_saisie.isdigit():
        return False
    if int(cleaned_saisie) < min_int or int(cleaned_saisie) > max_int:
        return False
    return True

def get_int_input(prompt, min_int, max_int):
    """Fonction qui demande au joueur de saisir un int"""
    input_int = input(prompt)
    while not is_entry_int_ok(input_int, min_int, max_int):
        input_int = input("Saisie incorrecte. Merci de recommencer : ")
    return input_int

def is_entry_user_ok(saisie):
    """ Fonction qui vérifie la saisie d'une chaine, soit D soit Q    """
    cleaned_saisie = saisie.strip()
    if not cleaned_saisie.isalpha():
        return False
    if cleaned_saisie != "D" and cleaned_saisie != "Q":
        return False
    return True

def get_str_entry_user(prompt):
    """Fonction qui demande au joueur de saisir D pour démarrer un nouveau tour, ou Q pour arrêter la course"""
    input_str = input(prompt)
    while not is_entry_user_ok(input_str):
        input_str = input("Saisie incorrecte. Merci de recommencer : ")
    return input_str

def get_distance_by_speed(speed):
    """Fonction qui renvoie la distance parcourue en un tour, par rapport à la vitesse du cheval"""
    return tuple_distance[speed]


def get_progress_by_speed_and_dice_roll(speed):
    """Fonction qui renvoie la progression d'un cheval en fonction de sa vitesse (et du lancer de dé fait dans cette fonction)
        Vitesse entre 0 et 6
    """
    # On effectue le lancer du dé pour ce cheval
    dice_roll_nb = random.randint(0, 5)

    # En fonction de la vitesse actuelle du cheval (passée en paramètre) et du lancer de dés, on récupère la progression de la vitesse
    value_progress = array_change_speed_with_dice_roll[speed][dice_roll_nb]
    if (str(value_progress) == "DQ"):
        print("Cheval disqualifié")
    else:
        print(f"Pour cette vitesse {speed} et le dé obtenu {dice_roll_nb+1} nous allons effectuer la progression suivante : {value_progress:+}")
    return value_progress



# TODO Modifier la fonction pour un bel affichage sous forme de tableau
def print_horse_values(list_horses):
    """ Fonction qui permet d'afficher pour chaque cheval la vitesse et la distance parcourue """
    for horse in list_horses:
        affichage = " "
        for key, value in horse.items():
            affichage += str(key) + " " + str(value) + " "
        print(f"Cheval : {affichage}")


def main_simulator():
    """ Fonction qui lance la simulation de la course de trot"""
    print("************************* Simulation de course de trot **************************")

    # Saisie utilisateur du nombre de chevaux entre 12 et 20
    nb_horses = get_int_input("Saisir le nombre de chevaux de la course, entre 12 et 20 : ", 12, 20)
    # Saisie utilisateur du type de course 1 Tiercé, 2 Quarté, 3 Quinté (3,4 ou 5 vainqueurs affichés)
    type_race = get_int_input("Combien de chevaux seront classés à l'arrivée (3 pour Tiercé, 4 pour Quarté, 5 pour Quinté) : ", 3, 5)

    # On initialise les chevaux de la course
    list_horses = []
    for i in range(1, int(nb_horses)+1):
        horse = {'num_horse': i, 'speed': 0, 'distance_traveled': 0, 'disqualified': False}
        list_horses.append(horse)

    nb_turn = 0
    elapsed_time_seconds = 0
    race_continue = True
    while race_continue:
        # On invite l'utilisateur à démarrer un nouveau tour en tapant D, ou Q pour quitter la course (et arrêter le programme)
        entry_user = get_str_entry_user("Pour démarrer un nouveau tour, tapez D, si vous souhaitez quitter, tapez Q : ")

        # Si l'utilisateur a demandé à arrêter la course, on quitte
        if (entry_user == "Q"):
            race_continue = False
        elif (entry_user == "D"):
            nb_turn += 1
            elapsed_time_seconds += 10
            print("L'utilisateur a demandé un nouveau tour")

            # Pour chaque cheval de la liste, on effectue un lancer de dé et on modifie la vitesse et la distance parcourue du cheval suivant le lancer de dé
            for horse in list_horses:
                # Si le cheval n'est pas disqualifié
                if not horse["disqualified"]:
                    print (f"Pour ce cheval : {horse["num_horse"]}")
                    # Récupération de la progression ou non suivant le lancer de dé et la vitesse
                    speed_progress = get_progress_by_speed_and_dice_roll(horse["speed"])
                    if (speed_progress == "DQ"):
                        # Cheval disqualifié
                        horse["disqualified"] = True
                    else:
                        # TODO On va ensuite mettre à jour la vitesse du cheval et la distance qu'il parcourt pour ce tour.
                        horse["speed"] = horse["speed"] + speed_progress
                        horse["distance_traveled"] = horse["distance_traveled"] + get_distance_by_speed(horse["speed"])

            # TODO On affiche le temps écoulé
            print(f"Temps écoulé : {elapsed_time_seconds} secondes")

            # TODO Pour chaque cheval on affiche le récapitulatif : vitesse et distance parcourue.
            print_horse_values(list_horses)

if __name__ == '__main__':
    main_simulator()

