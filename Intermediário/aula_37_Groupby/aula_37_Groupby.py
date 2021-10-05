from itertools import groupby, tee
alunos = [
    {'Nome': 'luiz', 'nota':'A'},
    {'Nome': 'lavino', 'nota':'B'},
    {'Nome': 'wanessa', 'nota':'C'},
    {'Nome': 'helena', 'nota':'D'},
    {'Nome': 'elaine', 'nota':'C'},
    {'Nome': 'guilheme', 'nota':'B'},
    {'Nome': 'roberta', 'nota':'A'},
]

alunos.sort(key=lambda item: item['nota'])
alunos_agrupados = groupby(alunos,lambda item: item['nota'])
for grupo, valores_agrupados in alunos_agrupados:
    v1, v2 = tee(valores_agrupados)
    print("Grupo:", grupo)
    for i in v1:
        print(i)
    quant = len(list(v2))
    print(quant,"Aluno(s) tiraram nota", grupo)