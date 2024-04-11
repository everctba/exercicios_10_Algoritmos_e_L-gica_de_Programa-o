flag_palindromo = True
print("Escreva uma palavra:")
palavra = str(input())
tamanho = len(palavra)
print("tamanho: ",tamanho )

media = int(tamanho/2)
print("MEDIA: ",media )
#print("-------------------------")
contador_acrescenta = 0

for i in palavra:
   ##print("letra = ",i )
   tamanho = tamanho-1
   #print("CONTADOR Crescente = ",contador_acrescenta)
   #print("CONTADOR Decrescente = ",tamanho)
   #print("-------------------------")
   #print(palavra[tamanho])
   if str(palavra[tamanho]) == str(palavra[contador_acrescenta]):
      flag_palindromo = True
   else:
      flag_palindromo = False
   #print("Flag Bool = ", flag_palindromo)   
   contador_acrescenta = contador_acrescenta+1
   

print("-------------------------")
if flag_palindromo:
   print("A palavra digitada É um PALINDROMO!" )   
else:  
   print("A palavra digitada NÃO é um PALINDROMO!") 