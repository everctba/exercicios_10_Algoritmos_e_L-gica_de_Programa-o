soma = 0
numeros_lista = []
flag = True
ultimo_numero_digitado = "Digite o Valor: "
print("Escreva seus numeros para fazer a SOMA, para finalizar basta digitar 0: ") 
print("----------------------------") 
ultimo_numero_digitado = input(ultimo_numero_digitado)
while flag:
   ultimo_numero_digitado = input("próximo valor: \n")
   
   if int(ultimo_numero_digitado) >= 1: #or <0
      numeros_lista.append(int(ultimo_numero_digitado))
   else:
      flag = False
for i in numeros_lista:
   soma=soma+int(i) 

print("sua soma total é: ", soma) 
#exercicio 4 