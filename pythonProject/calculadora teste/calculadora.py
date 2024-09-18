numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

while True:
    print(
        "*----------------------------------*\n"
        "| Escolha uma operação           |\n"
        "| 1. Para Soma                   |\n"
        "| 2. Para Subtração              |\n"
        "| 3. Para Divisão                |\n"
        "| 4. Para Multiplicação          |\n"
        "| 5. Para Digitar um novo número |\n"
        "| 6. Para sair                   |\n"
        "*----------------------------------*"
    )
    
    escolha = input("Digite sua escolha (1/2/3/4/5/6): ")
    
    if escolha == '6':
        print("Saindo do programa.")
        break
    
    if escolha == '5':
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        continue
    
    if escolha in ['1', '2', '3', '4']:
        if escolha == '1':
            resultado = numero1 + numero2
            print(f"{numero1} + {numero2} = {resultado}")
        elif escolha == '2':
            resultado = numero1 - numero2
            print(f"{numero1} - {numero2} = {resultado}")
        elif escolha == '3':
            if numero2 == 0:
                print("Erro: divisão por zero!")
            else:
                resultado = numero1 / numero2
                print(f"{numero1} / {numero2} = {resultado}")
        elif escolha == '4':
            resultado = numero1 * numero2
            print(f"{numero1} * {numero2} = {resultado}")
    else:
        print("Escolha inválida!")