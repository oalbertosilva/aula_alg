# faça um programa que mostre a contagem regressiva para estouro de fogos de artifício, de 10 até 0, com pausa de 1 segundo.
# c = 100
import time

for c in range(10, 0, -1):
    time.sleep(1)
    print(c)
time.sleep(1)
print("Fogos estouram!")
