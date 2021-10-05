from classes import Escritor, Caneta, MaquinaDeEscrever


esc = Escritor('lavino')
caneta = Caneta('bic')
maquina = MaquinaDeEscrever()

esc.ferramenta = maquina
esc.ferramenta.escrever()