# Exercicio 08: areaulo de Área e quantidade em litros.

name = input("Digite seu nome: ")
apresentação = input(f"Olá {name}, Sejá bem vindo!")
largura = int(input("Digite a largura da parede:"))
altura = int(input("Digite a altura da parede: "))


area = largura * altura
tinta = float(area / 2) 

print(f"Certo {name}.Sua largura é {largura}m e altura de {altura}m. tem um total de {area}m², e precisa usar {tinta}L de tinta nas paredes.")
