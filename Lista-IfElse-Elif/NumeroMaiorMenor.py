#1) Peça para o usuário 2 números e faça variáveis para alocá-las
#2) Faça a identificação e compare se o número x ou y é maior ou menor
#3) Mostre ao usuário se ele é menor ou maior.

print("      ⏔⏔⏔⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔⏔⏔⏔\n")
print("    Será que Maior ou Menor? ₍^. .^₎⟆\n")
print("      ⏔⏔⏔⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔⏔⏔⏔\n")

num2 = int(input('✿ Insira o primeiro número: ').replace(",","."))
num3 = int(input('✿ Insira o segundo número: ').replace(",","."))

if num2 > num3:
    print('\n O número {} é maior que {}'.format(num2, num3))

else:
    print("\n O número {} é menor que {}".format(num3, num2))
