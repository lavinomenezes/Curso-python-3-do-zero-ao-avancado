from datetime import datetime
from  locale import  setlocale, LC_ALL
from calendar import mdays
setlocale(LC_ALL,'pt_BR.utf-8')
#sexta, 13 de junho de 2021
data = datetime.now()
mes_atual = int(data.strftime('%m'))
print(data.strftime('%A, %d de %B de %Y'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('%M'))
print(mes_atual,mdays[mes_atual])