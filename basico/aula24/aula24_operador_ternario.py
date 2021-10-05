"""
Operador ternário em python
"""
log = True
sms = 'ola usuário' if log else 'vc não é bem vindo'
idade = 17
demaior = (idade>=18)
msg = 'pode acessar' if demaior else 'não pode'

print(sms)
print(msg)
