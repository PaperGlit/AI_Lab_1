def calculate(w, w0, picture):
    s = w0
    for i in range(len(w)):
        s += picture[i] * w[i]
    return s