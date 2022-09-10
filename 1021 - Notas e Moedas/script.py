# -*- coding: utf-8 -*-

def notas(valor):
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    papeis = [100, 50, 20, 10, 5, 2]

    print('NOTAS:')
    for papel in papeis:
        qt_papeis = int(valor / papel)
        print('{} nota(s) de R$ {:.2f}'.format(qt_papeis, papel))
        valor -= qt_papeis * papel

    print('MOEDAS:')
    for moeda in moedas:
        # arredondando para apenas duas casas decimais
        valor = round(valor, 2)
        qt_moedas = int(valor / moeda)
        print('{} moeda(s) de R$ {:.2f}'.format(qt_moedas, moeda))
        valor -= qt_moedas * moeda


valor = float(input())

notas(valor)
