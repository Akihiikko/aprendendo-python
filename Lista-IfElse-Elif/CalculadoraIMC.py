#1) Peça o peso e a altura para o usuário.
#2) Calcule o IMC com as informações e classifique como abaixo do peso, sobrepeso ou obeso.
#3) Mostre ao usuário suas informações e a classificação de seu IMC.

print("      ꒷꒦︶꒷꒦︶ ๋ ࣭ ⭑꒷꒦꒷꒦︶꒷꒦︶ ๋ ࣭ ⭑꒷꒦\n")
print("       Calculadora IMC („• ֊ •„)\n")
print("      ꒷꒦︶꒷꒦︶ ๋ ࣭ ⭑꒷꒦꒷꒦︶꒷꒦︶ ๋ ࣭ ⭑꒷꒦\n")

altura = float(input("಄ Digite sua altura: ").replace(",","."))
peso = float(input("಄ Digite seu peso:").replace(",","."))

# Se for menor ou igual 18,5 - Abaixo do Peso
# 24,9 - Peso normal
# 29,9 - Excesso de Peso
# 34,9 - Obesidade 1
# 39,9 - Obesidade 2
#Maior ou igual a 40,0 - Obesidade 3

imc = (peso / (altura ** 2))
# (:.2f) pede para o codigo APÓS 0 . pegar duas casas decimas do float.

if imc <= 18.5:
    print ("Seu IMC é {:.2f} ! Você está abaixo do peso".format(imc))
elif imc <= 24.9:
    print('Seu IMC é {:.2f}. Seu peso está normal!'.format(imc))
elif imc <= 29.9:
    print('Seu IMC é {:.2f}. Você está com sobrepeso!'.format(imc))
elif imc <= 34.9:
    print('Seu IMC é {:.2f}. Você está com Obesidade Grau 1'.format(imc))
elif imc <= 39.9:
    print('Seu IMC é {:.2f}. Você está com Obesidade Grau 2'.format(imc))
elif imc >= 40.0:
    print('Seu IMC é {:.2f}. Você está com Obesidade Grau 3'.format(imc))