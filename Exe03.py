#Exercício 03: Soma de dois números.
name = input("Digite seu nome: ")
mensage = print(f"Olá {name} Seja bem vindo! vamos fazer uma soma de dois números?")
number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))

somanumber = number1 + number2

print(f"A Soma dos dois números inseridos é {somanumber:.3f}")