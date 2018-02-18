def inside_polygon(x, y, points):
    """
    Retorna True si una coordenada (x, y) está dentro de un poligonoo definido o creado por
    una lista de vertices [(x1, y1), (x2, x2), ... , (xN, yN)].
    """
    n = len(points)
    inside = False
    p1x, p1y = points[0]
    for i in range(1, n + 1):
        p2x, p2y = points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def drawpolygon(par):
    poly = []
    for line in par:
        line = line.replace('|', ',')
        line = line.split(',')
        for coord in line:
            vals = coord.split(' ')
            lista = []
            for val in vals:
                if val == '':
                    pass
                else:
                    lista.append(val)

            res = map(int, lista)
            ctuple = tuple(res)
            poly.append(ctuple)
    return poly