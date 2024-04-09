soma = 0
numeros_lista = []
ultimo_numero_digitado = "-1" 
print("Escreva seus numero em sequência, para finalizar basta digitar 0: ", ultimo_numero_digitado) 
print("----------------------------") 
while ultimo_numero_digitado != "0" : #or <0
   ultimo_numero_digitado = input(ultimo_numero_digitado)
   numeros_lista.append(ultimo_numero_digitado)
for i in numeros_lista:
   soma=soma+int(i) 

print("sua soma total é: ", soma)  