# -*- coding: utf-8 -*-

from decimal import Decimal
def maior_numero(num1, num2, num3):
    return maiorAB(maiorAB(num1, num2), num3)
    
def maiorAB(a,b):
    return (a + b + abs(a - b))//2
    
    
linha = input().split()
num1, num2, num3 =  list(map(int, linha)) 

x = maior_numero(num1, num2, num3)

print(f"{x} eh o maior")