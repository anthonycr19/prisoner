from fix import inside_polygon
from fix import drawpolygon

name = []
lista_datas = []
file = open('data.txt', encoding='utf-8')

for data_file in file:
    mine = data_file.replace('\n', '')
    name.append(mine.strip())
    ope = drawpolygon(name)
    lista_datas.append(ope)
file.close()

for data in lista_datas:
    long = len(data)
    ultimo = data[long - 1]
    x = ultimo[0]
    y = ultimo[1]
    data.pop()
    state = inside_polygon(x, y, data)
    print("Is a prisioner") if state else print("Not is prisioner")
