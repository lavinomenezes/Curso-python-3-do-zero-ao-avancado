try:
    a=1/0
except NameError as erro:
    print("erro:", erro)
except (IndexError,KeyError) as erro:
    print("erro  de indice:")

except Exception as erro:
    print("ocorreu um erro inexperado")
else:
    pass
    print("Sucesso")
    print(a)
finally:
    print("finalmente")
print("bora continuar")