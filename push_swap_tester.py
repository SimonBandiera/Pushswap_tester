 #!/usr/bin/python3

import os
import random

def nb_aleatoire():
    liste = []
    string = ""
    for i in range(0, random.randint(1, 10000)):
        nb = random.randint(-2147483647, 2147483647)
        liste.append(nb)
        string += str(nb) + " "
    with open ("test", "w") as f:
        f.write(string)

    return liste

def get_output():
    with open ("output", "r") as text_file:
        content = text_file.readline()
    return content.split()

def test(la, lb):
    output = get_output()
    l = len(output)
    for operation in output:
        if operation == "pa":
            la = [lb[0]] + la
            lb.pop(0)
        if operation == "pb":
            lb = [la[0]] + lb
            la.pop(0)
        if operation == "ra":
            la = la[1:] + [la[0]]
        if operation == "rb":
            lb = lb[1:] + [lb[0]]
    last = la[0]
    for i in range(1, len(la)):
        if last > la[i]:
            print("olala non problem")
            exit()
    print("GOOD SORT")
    return la



while True:
    liste = nb_aleatoire()
    if os.system("./push_swap $(cat test) > output") != 0:
        print("olala non problem")
        exit()
    test(liste, [])