
def cleanear(listxd):
    new_list = list()
    for i in range(len(listxd)):
        if listxd[i] != ',' and len(listxd[i]) > 0:
            new_list.append(listxd[i])
    new_list[3] = int(new_list[3])
    return new_list[1:]



with open('Musica entre 10 agosto 2 sept.csv', encoding='utf8') as f:
    musica = []
    tiempo = 0
    for fila in f:
        line = fila.strip().split('"')
        resultado_clean = cleanear(line)
        tiempo += resultado_clean[2]
        musica.append(resultado_clean)


artistas = {}

for i in range(len(musica)):
    nombre_artista = musica[i][0]
    if nombre_artista in artistas.keys():
        artistas[nombre_artista] += 1
    else:
        artistas[nombre_artista] = 1
       
artistas_ordenados = sorted(artistas.items(),key=lambda k:k[1])


canciones = {}

for i in range(len(musica)):
    nombre_cancion = musica[i][1]
    if nombre_cancion in canciones.keys():
        canciones[nombre_cancion] += 1
    else:
        canciones[nombre_cancion] = 1
       
canciones_ordenados = sorted(canciones.items(),key=lambda k:k[1])


print(artistas_ordenados[-1])
print(canciones_ordenados[-1])

minutos_totales = tiempo/60000
minutos_diarios = minutos_totales/23
print(minutos_diarios)

