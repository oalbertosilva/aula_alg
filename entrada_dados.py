# nome = input("Digite o seu nome: ") #aqui solicitei a entrada de dados do usuário, no caso, seu nome.
# print("O nome digitado é: ", nome) #aqui eu exibo na tela o que foi digitado

## Teste de conhecimento utilizando variaáveis, operadores e entrada de dados##

# o construtor, ou seja para que tipo de dado a string será convertida, entra antes do input


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

print("A média é: ", media)  # teste pra o github

if media >= 6.0:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
