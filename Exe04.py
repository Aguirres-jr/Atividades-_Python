# Exercicio04: Média das notas
name = input("Digite seu nome: ")
mensage = print(f"Olá {name}, insira os valores para fazer a média das notas: ")
nota1 = float (input("Digite a primera nota: "))
nota2 = float (input("Digite a segunda nota: "))
nota3 = float (input("Digite a terceira nota: "))

media_final = (nota1 + nota2 + nota3) / 3

if media_final >= 7:
    print(f"Parabéns {name}, Você foi Aprovado!")
elif media_final > 5:
    print(f"Infelizmente Você reprovou {name}, mas poderá fazer recuperação!")
else:  
    print(f"Que noticia triste {name}, Infelizmente Você foi reprovado!")

print (f"{media_final:.2f}")
