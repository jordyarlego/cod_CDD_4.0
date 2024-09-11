litros = float(input("quantidade de litros: "))
tipo = input("qual o tipo: ")
if tipo == "G" or tipo == "g":
    valor = litros * 5.8
    print(f" voce abasteceu com gasolina e gastou {valor}")
elif tipo == "E" or tipo == "e":
    valor = litros * 4.9
    print(f'voce abasteceu com etanol e gastou {valor}')
else:
    print("tipo de combustível inválido")