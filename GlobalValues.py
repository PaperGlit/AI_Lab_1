import to_bipolar


picture1 = [1, 0, 1,
            1, 1, 1,
            0, 0, 1]
picture2 = [1, 1, 1,
            1, 0, 1,
            1, 0, 1]
is_bipolar = True
threshold = 0.15

if is_bipolar:
    to_bipolar.bipolarify(picture1)
    to_bipolar.bipolarify(picture2)
    y1 = 1
    y2 = -1
else:
    y1 = 1
    y2 = 0
