import w_to_binary


def calculate(w, picture, y):
    if not w:
        for i in range(len(picture)):
            w.append(w_to_binary.equate(picture[i], y))
    else:
        for i in range(len(picture)):
            w[i] = w[i] + w_to_binary.equate(picture[i], y)
    return w