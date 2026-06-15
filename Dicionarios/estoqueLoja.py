estoque = {"Teclado": 15, "Mouse": 22, "Monitor": 8}

print(estoque)
atualiza_estoque = False
continuar = "s"
while continuar == "s":
    nome, quantidade = input("""૮(ྀི づ 𖥦◝ )ྀིაﾟ Digite o nome do produto que voce deseja comprar e a quantidade separados por virgula: """.split(","))

    for chave, valor in estoque.items():
        if nome.lower() == chave.lower():
            if valor == 0 :
                print ("Estoque Esgotado!!( ⌯′-′⌯)")
                continue
            if valor < int(quantidade):
                print("Estoque Insuficiente!!")
                continue
            else:
                estoque[chave] -= int(quantidade) # Ele reduz a quantidade que tem na lista de produtos
                atualiza_estoque = True

if atualiza_estoque:

    continuar = input("Quer dar continuidade? ƪ(˘⌣˘)ʃ s/n")[0].lower()
