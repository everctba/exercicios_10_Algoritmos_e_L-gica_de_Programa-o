numero_digitado = input("Digite um numero de 1 a 9999: ")

milhar = 1000
centena = 100
dezena = 10
unidade = 1

numero_digitado = int(numero_digitado)

milhar = numero_digitado - (numero_digitado%1000)
centena = (numero_digitado - milhar) - (numero_digitado%100) 
dezena = (numero_digitado - centena - milhar) - (numero_digitado%10) 
unidade = (numero_digitado - dezena - centena - milhar) - (numero_digitado%1) 

print("o digitdo de milhar é: ", milhar)
print("o digitdo de centena é: ", centena)
print("o digitdo de dezena é: ", dezena)
print("o digitdo de unidade é: ", unidade)