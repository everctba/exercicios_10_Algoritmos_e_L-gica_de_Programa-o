

#eleitores = input("Escreva a quantidade de eleitores: ")
votos_validos = input("Escreva a quantidade de votos válidos: ")
votos_nulos = input("Escreva a quantidade de votos nulos: ")
votos_branco = input("Escreva a quantidade de votos em branco: ")

total = 0

total = (int(votos_validos) + int(votos_nulos) + int(votos_branco))
print("------------------------")
print("Total de votos de ELEITORES: ",total, "= 100%")

#votos_validos
n1 = total
n2 = 100 #porcentagem máxima
n3 = int(votos_validos)
x = (n3*n2/n1)
print (f"A porcentagem de votos válidos é: {x:.2f}%" )

#votos_nulos
n1 = total
n2 = 100 #porcentagem máxima
n3 = int(votos_nulos)
x = (n3*n2/n1)
print (f"A porcentagem de votos nulos é: {x:.2f}%" )

#votos_branco
n1 = total
n2 = 100 #porcentagem máxima
n3 = int(votos_branco)
x = (n3*n2/n1)
print (f"A porcentagem de votos brancos é: {x:.2f}%" )

