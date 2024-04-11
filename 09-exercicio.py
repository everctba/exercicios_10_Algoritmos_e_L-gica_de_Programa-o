palavra: str
palavra_input = "temp"
print("Escreva uma palavra:")
##ler input
palavra_input = input()
tamanho = len(palavra_input)
## Reverter string modo automático
print("Sua palavra revertida:", palavra_input[::-1])
print("-------------------")
## Reverter string modo feito na unha
for i in palavra_input:
   print(palavra_input[tamanho-1],end='')
   tamanho = tamanho-1
   ##i = i+1
print(" ")   
print("-------------------")