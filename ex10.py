#Este programa verifica se o usuário tem o peso ideal com base em seu peso e altura
print("Este programa verifica se você tem o peso ideal")
pes = float(input("Entre com o seu peso: "))
alt = float(input("Entre com o sua altura: "))
#As variáveis foram declaradas float para que não haja erro ou perda de precisão na multiplicação
R = pes/pow(alt,2)
#Para se manter no padrão criamos um valor R conforme exibido na tabela 
if (R < 20):
    print("Abaixo do peso")
elif (R >= 20):
    print("Acima do peso")
elif (20 <= R <25):
    print("Peso ideal")
#Foram especificados todos os casos para que o código fique mais claro
#Uma das declarações poderia ter tido sua condição omitida, dado que todos os casos possíveis são testados