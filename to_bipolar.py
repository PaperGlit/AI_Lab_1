def bipolarify(picture):
    for i in range(len(picture)):
        if picture[i] == 0:
            picture[i] = -1