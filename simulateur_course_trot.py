#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

"""
Simulateur de course de trot
Séverine Hori Maitrehut

"""


# Longueur de la course
CONST_LENGTH = 2400
# Paramètres pour la barre de progression
CONST_SIZE_PROGRESS_BAR = 30
CONST_CHAR_FULL_PROGRESS_BAR = "#"
CONST_CHAR_EMPTY_PROGRESS_BAR = "-"

# Tuple qui donne la distance parcourue en fonction de la vitesse. Indice 0 = vitesse 0, indice 6 = vitesse 6
tuple_distance = (0, 23, 46, 69, 92, 115, 138)
array_change_speed_with_dice_roll = [[0, +1, +1, +1, +2, +2],
                                     [0, 0, +1, +1, +1, +2],
                                     [0, 0, +1, +1, +1, +2],
                                     [-1, 0, 0, +1, +1, +1],
                                     [-1, 0, 0, 0, +1, +1],
                                     [-2, -1, 0, 0, 0, +1],
                                     [-2, -1, 0, 0, 0, "DQ"]]

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
    # Si l'utilisateur a seulement tapé sur la touche entrée
    if cleaned_saisie == "":
        return True
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


def get_horse(list_horses, num_horse):
    for horse in list_horses:
        if horse["num_horse"] == num_horse:
            return horse
    return None


def get_list_horses(nb_horses):
    list_horses = []
    for i in range(1, int(nb_horses) + 1):
        horse = {'num_horse': i, 'speed': 0, 'distance_traveled': 0, 'disqualified': False, 'turn_arrival': 0}
        list_horses.append(horse)
    return list_horses


def get_progress_by_speed_and_dice_roll(speed):
    """Fonction qui renvoie la progression d'un cheval en fonction de sa vitesse et du lancer de dé
        Vitesse entre 0 et 6
    """
    # On effectue le lancer du dé pour ce cheval
    dice_roll_nb = random.randint(0, 5)

    # En fonction de la vitesse actuelle du cheval et du lancer de dés, on récupère la progression de la vitesse
    value_progress = array_change_speed_with_dice_roll[speed][dice_roll_nb]
    return value_progress


def print_horse_values(list_horses):
    """ Fonction qui affiche pour chaque cheval la vitesse et la distance parcourue, et s'il est disqualifié """
    affichage_titres = (
        f"{'Numéro':<10} | "
        f"{'Vitesse':>8} | "
        f"{'Distance parcourue':>18} | "
        f"{'Cheval disqualifié':>15} | \n"
    )
    affichage_titres += "-" * 65
    print(affichage_titres)
    affichage = ""
    for horse in list_horses:
        horse_disqualified = "Disqualifié" if horse["disqualified"] else ""
        affichage += (
            f"{str(horse["num_horse"]):<10} |"
            f"{str(horse["speed"]):>10} | "
            f"{str(horse["distance_traveled"]):>18} | "
            f"{horse_disqualified:>18} |\n"
        )
        affichage += "-" * 65
        affichage += "\n"
    print(affichage)


def print_horse_values_horizontal(list_horses):
    """ Fonction qui permet d'afficher pour chaque cheval la vitesse et la distance parcourue et s'il est disqualifié
    VERSION HORIZONTALE pour un affichage plus compact  """
    print_num = f"{'Numéro ':<20} | "
    print_speed = f"{'Vitesse ':<20} | "
    print_distance = f"{'Distance parcourue ':<20} | "
    print_disqualified = f"{'Cheval disqualifié ':<20} | "
    print_arrived = f"{'Cheval arrivé ':<20} | "

    for horse in list_horses:
        horse_disqualified = "OUI" if horse["disqualified"] else " - "
        horse_arrived = "OUI" if horse["turn_arrival"] > 0 else " - "
        print_num += f"{str(horse["num_horse"]):5} | "
        print_speed += f"{str(horse["speed"]):5} | "
        print_distance += f"{str(horse["distance_traveled"]):5} | "
        print_disqualified += f"{horse_disqualified:5} | "
        print_arrived += f"{horse_arrived:5} | "

    print(print_num+"\n")
    print(print_speed+"\n")
    print(print_distance+"\n")
    print(print_disqualified+"\n")
    print(print_arrived + "\n")


def get_visual_progression(list_horses):
    """ Fonction permettant d'afficher une progression visuelle de chaque cheval dans la course """
    size_barre = CONST_SIZE_PROGRESS_BAR
    char_full = CONST_CHAR_FULL_PROGRESS_BAR
    char_empty = CONST_CHAR_EMPTY_PROGRESS_BAR
    for horse in list_horses:
        # On calcule le nombre d'éléments pleins à afficher par rapport à la taille de la barre d'affichage
        # On arrondit - et on borne la valeur à la taille de la barre pour ne pas dépasser
        nb_full = min(round(size_barre * horse["distance_traveled"] / CONST_LENGTH), size_barre)
        nb_empty = size_barre - nb_full
        # On affiche la barre de progression
        print(f"{horse["num_horse"]:5} : [{int(nb_full) * char_full}{int(nb_empty) * char_empty}]")


def get_nb_horses_no_longer_in_race(list_horses):
    """ Fonction qui retourne le nombre de chevaux soit disqualifiés soit ayant franchi la ligne d'arrivée """
    nb_horses_no_longer_in_race = 0
    for horse in list_horses:
        if horse["disqualified"] or (horse["turn_arrival"] > 0):
            nb_horses_no_longer_in_race += 1
    return nb_horses_no_longer_in_race


def is_end_race(list_horses, nb_horses):
    """Fonction qui retourne True si la course est finie, False sinon"""
    nb_horses_no_longer_in_race = get_nb_horses_no_longer_in_race(list_horses)
    if nb_horses_no_longer_in_race == int(nb_horses):
        return True
    return False


def get_winners(list_horses, type_race, tab_winners):
    """Fonction qui renvoie la liste des gagnants suivant le type de course choisi (3, 4 ou 5)"""
    list_winners = []

    for num_tour in sorted(tab_winners):
        # On va récupérer les x chevaux gagnants du 1er tour enregistré
        winners_horses = tab_winners[num_tour].split("-")

        # On récupère les dictionnaires des chevaux qui ont gagné pour ce tour
        horses = []
        for num_horse in winners_horses:
            horse = get_horse(list_horses, int(num_horse))
            horses.append(horse)

        # Tri pour ce tour : distance décroissante puis vitesse décroissante (aide chat gpt pour ce tri)
        horses.sort(
            key=lambda h: (h["distance_traveled"], h["speed"]),
            reverse=True
        )

        # On ajoute les gagnants tant qu'il reste des places
        for horse in horses:
            if len(list_winners) >= int(type_race):
                break
            list_winners.append(horse)

    return list_winners


def main_simulator():
    """ Fonction qui lance la simulation de la course de trot"""
    print("************************* Simulation de course de trot **************************")

    # Saisie utilisateur du nombre de chevaux entre 12 et 20
    nb_horses = get_int_input("Saisir le nombre de chevaux de la course, entre 12 et 20 : ", 12, 20)
    # Saisie utilisateur du type de course 1 Tiercé, 2 Quarté, 3 Quinté (3,4 ou 5 vainqueurs)
    type_race = get_int_input("Nombre de gagnants classés à l'arrivée (3=>Tiercé, 4=>Quarté, 5=>Quinté) : ", 3, 5)

    # On initialise les chevaux de la course
    list_horses = get_list_horses(nb_horses)

    nb_turn = 0
    elapsed_time_seconds = 0
    race_continue = True
    tab_winners = {}
    while race_continue:
        # On invite l'utilisateur à démarrer un nouveau tour en tapant sur Entrée, ou Q pour quitter la course
        entry_user = get_str_entry_user("Pour démarrer un nouveau tour, tapez D ou touche Entrée, pour Quitter tapez Q : ")

        # Si l'utilisateur a demandé à arrêter la course, on quitte
        if entry_user == "Q":
            race_continue = False
            exit()

        nb_turn += 1
        elapsed_time_seconds += 10

        for horse in list_horses:
            # Si le cheval n'est pas disqualifié et pas non plus déjà arrivé
            if not horse["disqualified"] and horse["turn_arrival"] == 0:
                # Récupération de la progression ou non suivant le lancer de dé et la vitesse
                speed_progress = get_progress_by_speed_and_dice_roll(horse["speed"])
                if speed_progress == "DQ":
                    # Cheval disqualifié
                    horse["disqualified"] = True
                else:
                    # On va ensuite mettre à jour la vitesse du cheval et la distance qu'il parcourt pour ce tour.
                    horse["speed"] = horse["speed"] + speed_progress
                    horse["distance_traveled"] = horse["distance_traveled"] + tuple_distance[horse["speed"]]


                    # Si le cheval a franchi la ligne d'arrivée on va le mettre à jour dans la liste des chevaux.
                    if horse["distance_traveled"] > CONST_LENGTH:
                        horse["turn_arrival"] = nb_turn
                        # On ajoute le cheval dans la liste des gagnants
                        if nb_turn in tab_winners:
                            tab_winners[nb_turn] += "-" + str(horse["num_horse"])
                        else:
                            tab_winners[nb_turn] = str(horse["num_horse"])

            # Pour chaque cheval on affiche le récapitulatif : vitesse et distance parcourue.
            # print_horse_values(list_horses)
            print_horse_values_horizontal(list_horses)

            # On affiche la progression visuelle pour les chevaux
            get_visual_progression(list_horses)

            # On affiche le temps écoulé
            print(f"Temps écoulé : {elapsed_time_seconds} secondes")

            if is_end_race(list_horses, nb_horses):
                print("La course est terminée ! Il n'y a plus aucun cheval présent dans la course ! ")

                # On récupère les gagnants suivant le type de course choisi (type_race = 3,4 ou 5)
                list_winners = get_winners(list_horses, type_race, tab_winners)

                # On affiche les gagnants
                print("Liste des gagnants : ")
                for horse_win in list_winners:
                    print(f"Cheval n°{horse_win['num_horse']} arrivé au tour {horse_win['turn_arrival']} "
                          f"- (Vitesse : {horse_win['speed']} Distance parcourue : {horse_win['distance_traveled']})")

                # On arrête la course.
                race_continue = False


if __name__ == '__main__':
    main_simulator()
