
# faça um programa que leia o sexo de uma pessoa, mas que só aceite os valores "M" e "F". Caso esteja errado,
# deverá pedir a digitação novamente até que os valores requisitados sejam atendidos.

sx = " "

while sx != "F":
    sx = input("Digite novamente: ")
if sx == "F":
    print("Fim!")
