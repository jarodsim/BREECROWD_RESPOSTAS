# -*- coding: utf-8 -*-

def triangulo(a, b, c):
    interable = [a, b, c]

    if a + b > c and a + c > b and b + c > a:
        print(f"Perimetro = {sum(interable):.1f}")
    else:
        print(f"Area = {((a + b) *  c) / 2:.1f}")


a, b, c = input().split()

triangulo(float(a), float(b), float(c))
