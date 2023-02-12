#O seguinte programa calcula a área de um retângulo e mostra 2 mensagens de acordo com o resultado
print("Este programa calcula a área de um retângulo, dadas sua altura e base e diz se ele é pequeno ou grande")
alt = float(input("Entre com a altura de um retângulo: "))
bas = float(input("Entre com a base de um retângulo: "))
#As variáveis foram declaradas float para que não haja erro ou perda de precisão na multiplicação
if ((alt*bas) > 100):
    print("Terreno grande")
else:
    print("Terreno pequeno")
