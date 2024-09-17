from GlobalValues import *
import w_bipolar
import s
import w_to_binary
import w_binary
import math


w = []
s01 = -math.inf
s02 = math.inf

if is_bipolar:
    w0 = y1 + y2
    w = w_bipolar.calculate(w, picture1, y1)
    w = w_bipolar.calculate(w, picture2, y2)
else:
    w0 = w_to_binary.equate(1, y1) + w_to_binary.equate(1, y2)
    w = w_binary.calculate(w, picture1, y1)
    w = w_binary.calculate(w, picture2, y2)

while True:
    s1 = s.calculate(w, w0, picture1)
    s2 = s.calculate(w, w0, picture2)
    if s1 > 0 >= s2:
        print("Equation was successful! Current values: " + str(s1) + ", " + str(s2))
        prompt = input("Do you want to save the current values?: ")
        if prompt.lower() == "y":
            with open("saved.txt", "w") as f:
                for i in w:
                    f.write(str(i) + " ")
        else:
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
        break
    else:
        if s1 - s01 > 0 >= s1 - s02:
            print("Equation was unsuccessful.  Current values: " + str(s1) + ", " + str(s2) + ". Retrying...")
            s01 = s1
            s02 = s2
        else:
            print("Equation was unsuccessful and is unsolvable.  Current values: " + str(s1) + ", " + str(s2))
            break