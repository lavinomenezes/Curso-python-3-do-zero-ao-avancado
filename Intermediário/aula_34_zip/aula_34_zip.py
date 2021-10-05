""""
zio_unindo iteraveis
zip_logest - iterlools
"""
from itertools import zip_longest, count

cidades = ['Sousa', 'patos', 'Jaguaruana', 'recife', 'Salto do itarare']
estados = ['PB', 'PB', 'CE']
indice = count()
cidades_estados = zip(
    indice,
    cidades,
    estados,
)
for indice,cidades,estados in cidades_estados:
    print(indice,cidades,estados)
