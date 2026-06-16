def PI():
    return 3.14

def somar(n1, n2):
    soma = n1 + n2
    return soma

def subtrair(n1, n2):
    return n1 - n2

estoque = {"✧ Teclado Gamer Rosinha": 15, "✧ Mouse Razer Branco": 22, "✧ Monitor 24' 100HZ": 10}

mercadinho= {"಄ Feijão de Corda": 3.59, "಄ Canjica": 2.00, "಄ Carne Moída": 19.00}

doceria = {"✿ Peppero Chocolate": 5.99, "✿ Chocolate Branco Nestlê": 10.00, "✿ Biscoitinhos Amanteigados": 8.00}

#Com o def passando os parametros dessa forma precisamos repetir o lacho for por exemplo, deixando o codigo mais limpo e otimizado

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