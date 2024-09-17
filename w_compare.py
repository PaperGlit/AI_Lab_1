import os
from GlobalValues import threshold


def compare(w):
    if not os.path.exists("saved.txt"):
        print("Error: no values have been saved yet!")
        return
    dev = 0
    with open("saved.txt", "r") as f:
        w_old = f.readline().split()
    for i in range(len(w)):
        if w[i] != int(w_old[i]):
            dev += 1
    if dev > len(w) * threshold:
        print("Comparison unsuccessful, the deviation is above the threshold")
    else:
        print("Comparison successful, because the deviation is below the threshold")