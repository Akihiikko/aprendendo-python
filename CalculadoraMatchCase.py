# 1) Crie um menu interativo de calculadora utilizando while True. O programa deve exibir na tela:
#Subtrair
#Somar
#Multiplicar
#Dividir
#Sair
#O programa deve executar a ação escolhida e mostrar o menu novamente. Ele só deve encerrar de verdade quando o usuário digitar a opção 5.
while True:
    print("Escolha uma operaça: \n 1 - Somar \n 2 - Subtrair \n 3 - Multiplicar \n 4 - Dividir \n 5 - Sair")
    opcao = int(input("Escolha a operacao que deseja realizar: "))


    match opcao: #Combinacao igual tinder. Caso 1 faca isso... Se n tiver mais o caso, precisa ter um default
        case 1:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
            result = num1 + num2
            print("O resultado é: {result} ")
        case 2:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
            result = num1 - num2
            print("O resultado é: {result} ")
        case 3:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
            result = num1 * num2
            print("O resultado é: {result} ")
        case 4:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
            if(num2 == 0):
                print("Não é possível fazer a divisão por zero!")
                continue
            result = num1 / num2
            print("O resultado é: {result}")
        case _:
            print("Escolha uma das opcoes acima!!")
# O break para a reprectcao e interrompe tudo. Já o continue continua deixando o codigo rodando.