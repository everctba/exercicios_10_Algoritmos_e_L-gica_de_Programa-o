#exercicio forma um triangulo

a = input("digitar o primeiro número para o triangulo: ")
b = input("digitar o segundo número para o triangulo: ")
c = input("digitar o terceiro número para o triangulo: ")
flag = False
if (a+b > c) and (a+c > b) and (b+c > a) :
   print("É um triângulo!")
   flag = True
else:
   print("Não forma um triangulo")
print("--------------------")

if flag==True:
   if (a==b and a == c):
      print("Forma um triangulo EQUILÁTERO")    
   elif (a==b or a==c or b==c):
      print("Forma um triangulo ISÓSCELES")
   else:
      print("Forma um triangulo ESCALENO")
