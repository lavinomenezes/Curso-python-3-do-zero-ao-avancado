tarefas = list()
aux = list()
while True:
    tar = input("nova tarefa, desfazer, refazer")

    if tar == 'nova tarefa':
        tarefas.append(input("Digite a nova terefa: "))
        aux = tarefas[:]
        print(aux)
        continue
    elif tar == 'desfazer':
        if len(tarefas) == 0:
            print("Não existe valores na lista")
            continue
        else:
            aux.pop()
            print(aux)
    elif tar == 'refazer':
        if len(tarefas) == 0:
            print("Não existe valores na lista")
            continue
        elif len(aux) == len(tarefas):
            print("Todas as modificações já foram refeitas")
            continue
        else:
            aux.append(tarefas[(len(aux))])
            print(aux)
    else:
        break

