import w_compare
import w_save
from GlobalValues import *
import w_bipolar
import s
import w_to_binary
import w_binary
import math


w = []
s01 = -math.inf
s02 = math.inf

while True:
    if is_bipolar:
        w0 = y1 + y2
        w = w_bipolar.calculate(w, picture1, y1)
        w = w_bipolar.calculate(w, picture2, y2)
    else:
        w0 = w_to_binary.equate(1, y1) + w_to_binary.equate(1, y2)
        w = w_binary.calculate(w, picture1, y1)
        w = w_binary.calculate(w, picture2, y2)

    s1 = s.calculate(w, w0, picture1)
    s2 = s.calculate(w, w0, picture2)
    if s1 > 0 >= s2:
        print("Equation was successful! Current values: " + str(s1) + ", " + str(s2))
        prompt = input("Do you want to save the current values?: ")
        if prompt.lower() == "y":
            w_save.save(w)
        else:
            w_compare.compare(w)
        break
    else:
        if s1 - s01 > 0 >= s1 - s02:
            print("Equation was unsuccessful.  Current values: " + str(s1) + ", " + str(s2) + ". Retrying...")
            s01 = s1
            s02 = s2
        else:
            print("Equation was unsuccessful and is unsolvable.  Current values: " + str(s1) + ", " + str(s2))
            break