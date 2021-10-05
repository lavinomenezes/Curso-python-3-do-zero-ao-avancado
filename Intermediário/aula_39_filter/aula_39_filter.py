from dados import pessoas, produtos, lista
def filtra(p):
    if p['preco']>=50:
        return True

n1 = list(filter(filtra,produtos))
for i in n1:
    print(i)
print("**********************************")
for i in produtos:
    print(i)