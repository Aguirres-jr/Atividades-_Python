# Exercicio 08: Calculo de Área e quantidade em litros.

name = input("Digite seu nome: ")
apresentação = input(f"Olá {name}, Sejá bem vindo!")
largura = int(input("Digite a largura da parede:"))
altura = int(input("Digite a altura da parede: "))


calc = largura * altura
tinta = calc / 2 

print(f"Certo {name}. O calculo da área é {calc}m², e precisa usar {tinta}L de tinta nas paredes.")
