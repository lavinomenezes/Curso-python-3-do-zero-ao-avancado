""""
combinations, permutations, product - itertool
combinação - Ordem não importa
Permutação - Ordem importa
ambos não repetem valores únicos
Produtos - Ordem importa e repete valores únicos
"""""
pessoas = ['Lavino', 'Wanessa', 'Barbara', 'roberta', 'guilherme']
from itertools import combinations, permutations, product

for group in combinations(pessoas, 4):
    print(group)
print("#" * 50)
for i, c in enumerate(permutations(pessoas, 2)):
    print(i, c)
print("#" * 50)
for group in product(pessoas, repeat=2):
    print(group)
