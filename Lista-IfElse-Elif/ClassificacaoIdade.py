#1) Peça um número ao usuário para classificar a idade dele.
#2) Faça o calculo referente a data de nascimento e o ano atual.
#3) Mostre ao usuário e sua classificação etária.

print("     ⏔⏔⏔⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔⏔⏔⏔\n")
print("    Classificação de Idade ₍^. .^₎⟆\n")
print("     ⏔⏔⏔⏔⏔⏔ ꒰ ᧔ෆ᧓ ꒱ ⏔⏔⏔⏔⏔⏔\n")

data1 = int(input(" Informe o ano de seu nascimento: "))

result = data1 - 2026

if result <= 17:
    print("˙𐃷˙ Você tem {} anos e é menor de idade!".format(result))
elif result >= 59:
    print('◝(ᵔᵕᵔ)◜ Você tem {} anos é maior de idade!'.format(result))
elif result >= 60:
    print('Você tem {} anos e é idoso!(๑ᵔ⤙ᵔ๑)'.format(result))