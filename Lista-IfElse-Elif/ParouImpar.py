#1) O usuário precisa inserir um número.
#2) O código deve verificar se é par ou impar com qualquer número. Com o resto da divisão por 2 é 0 é par se der qualquer q n seja 0 é impar
#3) Printar na tela a resposta correta.

print("      ⏔⏔⏔⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔⏔⏔⏔\n")
print("     Será que é Par ou Impar? ₍^. .^₎⟆\n")
print("      ⏔⏔⏔⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔⏔⏔⏔\n")

num1 = int(input("✿ Insira o número para verificação: ").replace(",",".")) # Aparece para o usuário a inserção de num.

resultado = num1 /2

if resultado == 0:
    print ("O {} é um número Par!".format(resultado))

else:
    print("O {} é um número Impar!".format(resultado))


