# A divisão inteira "//" sempre vai retornar um número inteiro, como exemplo: 5/2 == 2
# O resto da divisão "%", como o próprio nome já diz, é o resto, como exemplo 5%2 == 1
# Ordem de precedencia da execução dos operadores aritméticos:
# 1. ()
# 2. **
# 3. * / // %
# 4. + -

## Exercício calculadora##

usuario = input("Digite o seu nome: ")
print("Seja bem vindo a calculadora", usuario, "!")

operacao = input("Qual operação deseja realizar?: ")
# nesta linha eu não utilizei a comparação "==" após a variável "operacao", pois eu quero testar as 3 opções de entrada
if operacao in ("Adição", "soma", "adicao"):
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite outro valor: "))
    resultado = (n1 + n2)
    print("A soma dos números informados é: ", resultado)
else:
    print("Operação não encontrada, programa encerrado.")
