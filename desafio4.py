# CALCULADORA

n1 = float(input("Selecione um número: "))
n2 = float(input("Selecione outro número: "))

operacao = input("Escolha uma operação (soma, subtração, multiplicação ou divisão): ")

if operacao == "soma":
    print(n1 + n2)

elif operacao == "subtração":
    print(n1 - n2)

elif operacao == "multiplicação":
    print(n1 * n2)

elif operacao == "divisão":
    print(n1 / n2)

else:
    print("Essa operação não existe"
