y=0
print("insira seu numero positivo:")
numero_usuario = int(input())
print("------------------")
if numero_usuario > 0:
  for x in range(numero_usuario):
    print(" ")
    for y in range(numero_usuario):
     print(y+1+x, end = " ")
else: 
  print("o Número precisa ser positivo")      
