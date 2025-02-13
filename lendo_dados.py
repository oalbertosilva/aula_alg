# exercicio onde eu informo todas as características de um dado que foi informado pelo usuário.
# atribuí um input na variável "a", onde o usuario pode digitar qualquer coisa.
# o type retorna o tipo primitivo do dado informado
# a função isspace me informa se o dado informado é apenas um espaço e me retorna um valor booleano
# a função isnumeric me informa se o dado é um número e me retorna um valor booleano
# a função __len__ faz a contagem de caracteres do dado informado pelo usuário e me retorna o número de caracteres
# a função isnumeric consegue verificar, mesmo sendo str, se ela pode ser convertida para o tipo int, por isso, ao informar um número, retorna true.
# a função isalpha testa se a entrada do usário é alfabética
# a função isalnum testa se a entrada do usuário é alfanumérica

a = input("Digite qualquer coisa: ")
print("O tipo primitivo desse valor pertence a classe: ", type(a))
print("Só tem espaços?: ", a.isspace())
print("É um número?: ", a.isnumeric())
print("Qual é a quantidade de caracteres do que foi digitado?: ", a.__len__())
print("É alfabético?: ", a.isalpha())
print("É alfanumérico: ", a.isalnum())
