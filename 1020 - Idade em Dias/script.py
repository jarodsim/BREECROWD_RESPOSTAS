# -*- coding: utf-8 -*-

def dias(valor):
    anos = int(valor // 365)
    meses = int((valor % 365)//30)
    dias = int((valor % 365) % 30)

    print(f"{anos} ano(s)")
    print(f"{meses} mes(es)")
    print(f"{dias} dia(s)")


entrada = input()

dias(int(entrada))
