repeat = "S"
while (repeat == "S"):

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    media = (n1 + n2 + n3) / 3
    print("A média obtida foi: ", media)
    if media >= 6.0:
        print("Aluno aprovado!")
    else:
        print("O aluno não obteve a média necessária. Aluno reprovado!")

    repeat = input(("quer continuar? S/N: "))
    if repeat == "N":
        print("Fim do programa!")
