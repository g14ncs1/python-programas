#Este programa calcula a média aritmética de 4 dados valores
print("Este programa realiza a média aritmética de quarto valores dados")
val1 = float(input("Entre com um número para o primeiro valor dado: "))
val2 = float(input("Entre com um número para o segundo valor dado: "))
val3 = float(input("Entre com um número para o terceiro valor dado: "))
val4 = float(input("Entre com um número para o quarto valor dado: "))
#As variáveis foram definidas float para que não haja erro ou perda de dados durante a multiplicação e divisão
print("A média aritmética dos valores ",val1,", ",val2,", ",val3," e ",val4," é ",(val1+val2+val3+val4)/4, sep='')
#Foi trocada a separação pois o uso da vírgula é somente utilizado com espaço à sua esquerda