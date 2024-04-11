#numero decimal para binário
resto = 0
quociente = 0
numero_em_binario = " "
numero_digitado = 100
numero_digitado = input("Digite seu número para ver em binário: ")
while int(numero_digitado) >= 1:
   quociente = int(int(numero_digitado)/2)
   #print("Quociente: ", quociente)
   resto = int(numero_digitado)%2
   #print("Resto: ", resto)
   numero_digitado = quociente
   if resto == 0:
      numero_em_binario = str("0") + numero_em_binario
   else:
      numero_em_binario = str("1") + numero_em_binario
print("--------------------")
print("Seu Número em Binário é: ", numero_em_binario)   
   
   
   
