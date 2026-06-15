print("     ༶𓍊 ༶𓋼 ༶𓍊 ༶𓋼 ༶𓍊 ༶༶𓍊 ༶𓋼 ༶𓍊 ༶𓋼 ༶𓍊 ༶\n")
print("    Calculadora de Dia da Semana 𓆩❤︎𓆪\n")
print("     ༶𓍊 ༶𓋼 ༶𓍊 ༶𓋼 ༶𓍊 ༶༶𓍊 ༶𓋼 ༶𓍊 ༶𓋼 ༶𓍊 ༶\n")

dia = input("Insira um Dia da Semana (˵◝ ⩊ ◜˵マ: \n")
while dia != 0:
    dia = int(input("𓆩❤︎𓆪 Informe um numero, ou 0 para sair: 𓆩❤︎𓆪"))

    match dia:
        case 1:
            print("✿ Domingo ✿ ")
        case 2:
            print("✿ Segunda-Feira ✿")
        case 3:
            print("✿ Terça-Feira ✿")
        case 4:
            print("✿ Quarta-Feira ✿")
        case 5:
            print("✿ Quinta-Feira ✿")
        case 6:
            print("✿ Sexta-Feira ✿")
        case 7:
            print("✿ Sábado-Feira ✿")
        case _:
            print("✿ Digite um dia válido!")