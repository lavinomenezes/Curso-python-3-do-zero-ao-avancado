nome = 'lavino'
print(nome, type(nome))
idade = 25
altura = 1.77
e_maior = idade > 18
data_atual = 2021
peso = 72
IMC = (peso/(altura**2))

print('Nome:', nome)
print('idade', idade)
print('altura', altura)
print('È maior: ', e_maior)
print('ano:', data_atual)
print('Peso:', peso, 'Kg')

print(nome, ' tem ', idade, ' de idade e seu IMC é ', IMC)
print(f'{nome} tem {idade} de idade e seu IMC é {IMC:.2f}')
print('{0} tem {1} anos de idade e seu imc é {2:.2f}'. format(nome,idade,IMC))
print('{n} tem {e} anos de idade e seu imc é {im}'. format(n=nome,e=idade,im=IMC))
