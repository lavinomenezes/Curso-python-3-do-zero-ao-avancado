senha = input("digite a senha: ")
tam_s = senha.__len__()
#if len(nome) >= 6 and 'a' in nome:
#    print(f"o nome tem {len(nome)} letras e possui a letra a")
#else:
#    print("nome pequeno")

if tam_s < 8:
    print("a senha deve possuir ao menos 8 caracteres")
elif ' ' in senha:
    print("A senha não deve conter espaços")
else:
    print("senha cadastrada com suscesso")