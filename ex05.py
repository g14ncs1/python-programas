#Este programa converte milhas marítmas em quilômetros
print("Este programa realiza a conversão de milhas marítmas em quilômetros")
mil = float(input("Entre com o valor de milhas para realizar a conversão:"))
#Milhas foi declarado em float pois possibilita a multiplicação sem erro ou perda de dados
print("O número de quilômetros equivalente ao valor dado é de ", mil*1.852,"km",sep='')
#1 Milha equivale a 1852 metros e portanto 1,852