
leds = {
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6,
    '0': 6
}


def quantidade_lampadas(valor):
    total = 0
    [total := total + leds[x] for x in valor]

    print(f"{total} leds")


quantidade = int(input())

for i in range(quantidade):
    valor = input()

    quantidade_lampadas(valor)
