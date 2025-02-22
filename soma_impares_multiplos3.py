# Crie um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3, num intervalo de 1 e 21
soma = 0
cont = 0

for c in range(1, 21):
    if c % 3 == 0:
        impares = c
        print("Os números ímpares são: ", impares)

        soma += impares
        cont += 1
        print(soma)
