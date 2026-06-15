#1) Desenvolva um script que peça para o usuário digitar 6 números inteiros e os armazene em uma lista. Ao final, o programa deve exibir
#2) A lista completa na ordem em que foi digitada.
#3) A soma de todos os valores da lista.
#4) O maior e o menor valor presente na lista.

print("     ⏔⏔⏔⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔⏔⏔⏔\n")
print("     Analista de Números ₍^. .^₎⟆\n")
print("     ⏔⏔⏔⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔⏔⏔⏔\n")

num1 = int(input('✿ Insira o primeiro número: '))
num2 = int(input('✿ Insira o segundo número: '))
num3 = int(input('✿ Insira o terceiro número: '))
num4 = int(input('✿ Insira o quarto número: '))
num5 = int(input('✿ Insira o quinto número: '))
num6: int = int(input('✿ Insira o sexto número: '))

numeros = [num1, num2, num3, num4, num5, num6]
ordenada = sorted(numeros) #ordena de forma crescente os números como solicitado.

print("\n ✿Os números de forma ordenada do menor ao maior ficam {}✿ !!\n".format(ordenada))

soma = num1 + num2 + num3 + num4 + num5 + num6
print(" ✿Os números quando somados resulta em:✿ {} !!".format(soma))

menor = numeros[0]
maior = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

print(f" ✿ O menor número é: {menor} ✿") # f string permite colocar as variaveis direto dentro do texto.
print(f" ✿ O maior número é: {maior} ✿")