
celsius = float(input("Qual é a temperatura atual?: "))
faren = float(celsius * 1.8) + 32

print("A temperatura atual após conversão é de: ", (faren))
if faren >= 90:
    print("Convén usar protetor solar")

else:
    print("O dia está ótimo para um passeio ao ar livre!")
