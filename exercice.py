#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0 :
        return abs(number)
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    list = []
    for i in prefixes:
        list.append(i + suffixe)
    return list


def prime_integer_summation() -> int:
    nb_premier = []
    nb = 2
    somme = 0
    while len(nb_premier) < 100 :
        for i in range(2, nb) :
            if nb % i == 0 :
                nb += 1
                break
        else :
            nb_premier.append(nb)
            nb += 1
    for j in range(len(nb_premier)) :
        somme += nb_premier[j]
    return somme


def factorial(number: int) -> int:
    if number == 0 :
        return 1
    else :
        f = 1
        for i in range(2, number + 1) :
            f *= i
        return f


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5 :
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    list = []
    for i in groups :
        if len(i) > 10 or len(i) <= 3 :
            list.append(False)
            continue
        elif 25 in i :
            list.append(True)
            continue
        elif min(i) < 18 :
            list.append(False)
            continue
        elif max(i) > 70 and 50 in i :
            list.append(False)
            continue
        list.append(True)
    return list


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
