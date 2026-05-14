#1) Faça o usuário inserir dois números para armazenar como nota
#2) Faça o cálculo da média entre eles pela (variável1 + variável2)/2 (divisão)
#3) Mostre se ele foi reprovado, aprovado ou está na recuperação.

print("                       ✧˖°. ⋆｡˚✧˖°. ⋆｡˚(✿ᴗ͈ˬᴗ͈)｡･:*˚:✧˖°. ⋆｡˚✧｡\n")
print("                       ૮꒰˶• ༝ •˶꒱ა  Boletim escolar  (*ᴗ͈ˬᴗ͈)ꕤ*.ﾟ\n")
print("                        ✧˖°. ⋆｡˚✧˖°. ⋆｡˚(✿ᴗ͈ˬᴗ͈)｡･:*˚:✧｡✧˖°. ⋆｡˚\n")

frequencia = int(input("Informe quantos dias o aluno compareceu as aulas: ")) #input aparece na tela

if frequencia > 0 :
    n1 = float(input("Digite a primeira nota: ").replace(",",".")) #ele pega qualquer string e substitui pelo oq vc deseja.
    n2 = float(input("Digite a segunda nota: ").replace(",","."))

    media = (n1+n2) / 2

    if media == 10:
        print("OMG (๑˃̵ᴗ˂̵)و Você tirou a nota máxima!! {}!!!".format(media)) #.format(variável) chama e dá print na tela do qeu está armazenado
    if media >=7: 
        print("Parabéns! Você tirou {} e passou de ano!! ♡(.◜ω◝.)♡".format(media))
    elif media >=5:
        print("Você tirou {} e está na recuperação! Procure o professor para fazer sua prova! (•﹏•;)".format(media))
    elif media < 5:
        print("Você tirou {} e foi reprovado! (¯﹃¯*)".format(media))
else:
    print("\nNão tem como ter nota se você não vai pra escola né (._.)\n")
