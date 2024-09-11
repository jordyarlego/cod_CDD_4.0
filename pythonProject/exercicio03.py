#dados os valores de horarios abaixo, decifre a logica e faça um código para executar
hora1 = int(input("Digite a primeira entrada"))
minuto1 = int(input("digite a segunda entrada"))
hora2 = int(input("Digite a segunda hora"))
minuto2 = int(input("Digite o segundo minuto"))

horasresultado1 = hora1+ hora2
minutosresultado1 = minuto1+minuto2
restoMinutos =  minutosresultado1  % 60
restoHoras = horasresultado1 % 12
horasAdd = restoHoras +1

if minutosresultado1>60:
    print(f"{horasAdd}:0{restoMinutos}")
else:
    print(f"{restoHoras}:0{restoMinutos}")













