def calculate(w, picture, y):
    if not w:
        for i in range(len(picture)):
            w.append(picture[i] * y)
    else:
        for i in range(len(picture)):
            w[i] = w[i] + picture[i] * y
    return w
