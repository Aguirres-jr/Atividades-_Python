from datetime import date
ano_atual = date.today().year

name = input("Digite seu nome: ")
ano_nascimento = int(input("Em que ano você nasceu: "))
idade = ano_atual - ano_nascimento

if idade >= 18: print(f"Sr. {name}, sua idade é {idade} e seu voto é Obrigatório")
elif idade >= 16: print(f"Sr. {name}, sua idade é {idade} e seu voto é Opcional")
else: print(f"Sr. {name}, sua idade é {idade} e seu voto é Negado")