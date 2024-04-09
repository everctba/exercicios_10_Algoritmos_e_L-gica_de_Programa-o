

eleitores = input("Escreva a quantidade de eleitores: ")
votos_validos = input("Escreva a quantidade de votos válidos: ")
votos_nulos = input("Escreva a quantidade de votos nulos: ")
votos_branco = input("Escreva a quantidade de votos em branco: ")

total = 0

total = (int(votos_validos) + int(votos_nulos) + int(votos_branco)) / 3

print("Total de votos: ",total)


