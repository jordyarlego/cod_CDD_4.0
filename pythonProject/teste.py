hora1 = int(input("Digite a primeira hora (0-23): "))
minuto1 = int(input("Digite o primeiro minuto (0-59): "))
hora2 = int(input("Digite a segunda hora (0-23): "))
minuto2 = int(input("Digite o segundo minuto (0-59): "))


total_minutos1 = hora1 * 60 + minuto1
total_minutos2 = hora2 * 60 + minuto2


total_minutos_saida = total_minutos1 + total_minutos2


hora_saida = total_minutos_saida // 60
minuto_saida = total_minutos_saida % 60


hora_saida = hora_saida % 24


if hora_saida == 0:
    hora_12 = 12
    periodo = 'AM'
elif hora_saida < 12:
    hora_12 = hora_saida
    periodo = 'AM'
elif hora_saida == 12:
    hora_12 = 12
    periodo = 'PM'
else:
    hora_12 = hora_saida - 12
    periodo = 'PM'


print(f"O horário de saída é {hora_12}:{minuto_saida:02d} {periodo}.")