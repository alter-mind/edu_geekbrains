def vector_len(x1=0, y1=0, z1=0, x2=0, y2=0, z2=0):
    import math
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


print(vector_len(2, 1, 1))
