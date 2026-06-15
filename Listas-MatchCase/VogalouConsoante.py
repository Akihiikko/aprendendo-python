#1) Peça para o usuário digitar uma letra.
#2) Se for A E I O U Vogal, se não, consoante.
while True:

    print("      ꒷꒦︶꒷꒦︶ ๋ ࣭ ⭑꒷꒦꒷꒦︶꒷꒦︶ ๋ ࣭ ⭑꒷꒦\n")
    print("       É Vogal ou Consoante? („• ֊ •„)\n")
    print("      ꒷꒦︶꒷꒦︶ ๋ ࣭ ⭑꒷꒦꒷꒦︶꒷꒦︶ ๋ ࣭ ⭑꒷꒦\n")

    letra = str(input('✿ Insira uma letra, \n Caso contrário digite 0 para sair ｡°(°¯᷄◠¯᷅°)°｡: ').upper())
#Toda vez que for fazer algo comparativo e entre maiúsculo ou minúsculo, para verificar ambos com a resposta correta utilizar lower para min. UPPER para maiú.
    if letra == "0": # colocar o 0 () o transforma ele em string para ler, e não como um nome de variável.
        break

    match letra:
        case "A" | "E" | "I" | "O" | "U " :
            print("   . ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.. ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.\n")
            print(" \n \n {} é uma Vogal!! ૮ ˶ᵔ ᵕ ᵔ˶ ა \n \n".format(letra))
            print("   . ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.. ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.\n")
        case _:
            print("   . ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.. ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.\n")
            print(" \n  {} é uma Consoante!! ₍₍⚞(˶ˆᗜˆ˵)⚟⁾⁾ \n \n".format(letra))
            print("   . ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.. ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.\n")