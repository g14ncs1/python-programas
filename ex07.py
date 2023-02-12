#Este programa lê dois valores digitados e mostra o menor
print("Este programa exibirá o menor de dois valores dados pelo usuário")
val1 = float(input("Entre com o primeiro valor: "))
val2 = float(input("Entre com o segundo valor: "))
if (val1 < val2):
    print("O primeiro valor",val1,"é menor que o segundo",val2)
elif (val2 < val1):
    print("O segundo valor",val2,"é menor que o primeiro",val1)
#São realizados 2 testes para a exibição do maior valor
#Observação, não é realizado teste para o caso de ambos valores serem iguais

