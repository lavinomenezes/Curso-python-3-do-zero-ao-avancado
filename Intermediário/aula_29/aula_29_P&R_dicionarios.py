perguntas = {
    'Pergunta 1':{
        'pergunta': 'Quanto é 2+2?',
        'resposta': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa' : 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2?',
        'resposta': {
            'a': '12',
            'b': '4',
            'c': '6',
        },
        'resposta_certa': 'c'
    },

}
for k, v in perguntas.items():
    print(f"{k}:{v['pergunta']}")
    print('escolha uma das opcões abaixo')
    for rk, rv in v['resposta'].items():
        print(f"[{rk}]: {rv}")
    print()
    resp = str(input("Sua resposta: "))
    if resp == v['resposta_certa']:
        print("Vc acertou :)")
    else:
        print("errou")