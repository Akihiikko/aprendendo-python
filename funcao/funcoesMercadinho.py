estoque = {"✧ Teclado Gamer Rosinha ": 15, "✧ Mouse Razer Branco ": 22, "✧ Monitor 24' 100HZ ": 10}

mercadinho= {"಄ Feijão de Corda ": 3.59, "಄ Canjica ": 2.00, "಄ Carne Moída ": 19.00}

doceria = {"✿ Peppero Chocolate ": 5.99, "✿ Chocolate Branco Nestlê ": 10.00, "✿ Biscoitinhos Amanteigados ": 8.00}

jogos = {"♥ God of War: Laufey ": 140.00, "♥ Hello Kitty - Island Adventure ": 100.00, "♥ Wuthering Waves - BattlePass ":  25.00 }

#Com o def passando os parâmetros dessa forma não precisamos repetir o laço For várias vezes, por exemplo, deixando o código mais limpo e otimizado.

def imprimir_dic(dic, descricao):
    print(f"Imprimindo Dicionário com Coisas de {descricao}:")
    for k, v in dic.items():
        print(f"{k}:{v}")

imprimir_dic(estoque, "/ᐠっ˕ -マ Informatica")
print()

imprimir_dic(mercadinho, "૮ ◜ᵕ◝ ྀིა Mercadinho")
print()

imprimir_dic(doceria, "ꉂꉂ(ᵔᗜᵔ*) Doceria") # Saio importando apenas trocando o nome da variavel
print()

imprimir_dic(jogos, "૮ •ﻌ -ა♥ Joguinhos") # Saio importando apenas trocando o nome da variavel
print()