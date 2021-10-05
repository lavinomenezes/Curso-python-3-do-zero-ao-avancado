from pessoa import Pessoa

p1 = Pessoa('lavino',29)
p2 = Pessoa('elaine',25)
print(p1.ano_atual)
print(p1.ano_de_nascimento())
print(p2.ano_de_nascimento())

p1.comer('maça')
p1.comer('maça')
p1.para_de_comer('maça')
p1.para_de_comer('maça')
p1.comer('maça')
p1.para_de_comer('maça')

p1.falar('POO')
p1.falar('POO')
p1.parar_falar()
p1.parar_falar()
p2.falar('moster high')
