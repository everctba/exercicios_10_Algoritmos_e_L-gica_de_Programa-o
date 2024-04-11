#exercicio forma um triangulo

a = input("digitar o primeiro número para o triangulo: ")
b = input("digitar o segundo número para o triangulo: ")
c = input("digitar o terceiro número para o triangulo: ")

if a+b > c or a+c > b or b+c > c :
   print("é um triângulo")
else:
   print("não forma um triangulo")
   