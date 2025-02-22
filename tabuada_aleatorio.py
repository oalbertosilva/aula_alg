# Desenvolva um programa que leia qualquer número e e faça a tabuada dele;

import time
tab = 0

num = int(input("Digite um número inteiro: "))
for c in range(1, 11):
    tab = num * c
    time.sleep(0.5)
    print(num, "x", c, "= ", tab)
print("Fim da execução!")

# O "c" no ange pode ser qualquer coisa
# O "num" é a varável que recebe a entrada de dados
# O "tab" é a variável - que se inicia com 0 -  e recebe o valor de num (entrada) X o range
