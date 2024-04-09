i = 1
print("Escreva um número para ser mostrado todos os números divisíveis por 3 e 5:")
numero_usuario = input()
print("seu numero é:", numero_usuario)
print( "----------------------------------") 
if int(numero_usuario) <= 0:
   print("seu numero precisa ser MAIOR que 0:" )
   

while i <= int(numero_usuario):
   if i%3 == 0:
      print( "O número: ",i, " é divisivel por 3")
   i=i+1
i=1 
print( "----------------------------------")  
while i <= int(numero_usuario):       
   if i%5 == 0:
      print( "O número: ",i, " é divisivel por 5")
   i=i+1