def save(w):
    with open("saved.txt", "w") as f:
        for i in w:
            f.write(str(i) + " ")