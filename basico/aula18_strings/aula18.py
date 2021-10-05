txt = 'o rato roeu a roupa do rei de roma'
tamanho_txt = len(txt)
print(tamanho_txt)
cont = 0
contr = 0
txt2 = ''
while cont < len(txt):
    letra = txt[cont]
    if letra == 'r':
        txt2 += letra.upper()
    else:
        txt2 += letra
    cont += 1
print(txt2)