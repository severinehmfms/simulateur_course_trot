#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simulateur de course de trot
Séverine Hori Maitrehut

"""


# Tuple qui donne la distance parcourue en fonction de la vitesse
# Indice 0 = vitesse 0, indice 6 = vitesse 6
tuple_distance = (0, 23, 46, 69, 92, 115, 138)

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

def get_distance_by_speed(speed):
    """Fonction qui renvoie la distance parcourue en un tour, par rapport à la vitesse du cheval"""
    return tuple_distance[speed]

def get_progress_by_speed_and_dice_roll(speed, dice_roll):
    """Fonction qui renvoie la progression d'un cheval en fonction de sa vitesse et du lancer de dé obtenu
        Vitesse entre 0 et 6
        Lancer de dé entre 1 et 6
    """
    




def main_simulator():
    """ Fonction qui lance la simulation de la course de trot"""
    print("************************* Simulation de course de trot **************************")

    # Saisie utilisateur du nombre de chevaux entre 12 et 20
    nb_horses = get_int_input("Saisir le nombre de chevaux de la course, entre 12 et 20 : ", 12, 20)
    # Saisie utilisateur du type de course 1 Tiercé, 2 Quarté, 3 Quinté (3,4 ou 5 vainqueurs affichés)
    type_race = get_int_input("Saisir le type de la course (1 pour Tiercé, 2 pour Quarté, 3 pour Quinté) : ", 1, 3)





if __name__ == '__main__':
    main_simulator()

