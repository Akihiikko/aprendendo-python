#Alocação de informações via variáveis.

n1 = int(input("Digite o 1 numero:"))
n2 = int(input("Digite o 2 numero:"))

resultado = n1 // n2 #  Divide e mostra o valor inteiro 
resultado2 = n1 % n2 # Mostra o resto da divisão
resultado3 = n1 ** n2 # Potencia

print("resultado da parte inteira da divisão é :", resultado)
print("resultado2 do resto da divisão é", resultado2)
print("resultado3 da potencia é :", resultado3)

#Opewradores Relacionais
# == -  IGUAL
# > maior
# < menor
# >= maior ou igual
# <= menor ou igual
# != não igual. Diferente
# Na programacao o sinal de = é para receber algo, já == é igual.
# \n quebra a linha
# n1:n2 - (n1+n2)/2 é um float - Aritmetico
#media >=78 - Relacional
print ("_________________________________________________")
print ("  OPERADORES RELACIONAIS    ")
print ("_________________________________________________")

relacao1 = n1 > n2 # é boolean pois so retorna true or false
relacao2 = n1 < n2
relacao3 = n1 >= n2
relacao4 = n1 <= n2
relacao5 = n1 == n2
relacao6 = n1 != n2

print("Os resultados das relações estarão abaixo \n{} \n{} \n{} \n{} \n{} \n{}".format(relacao1, relacao2, relacao3, relacao4, relacao5, relacao6))
