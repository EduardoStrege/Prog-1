vel = int(input("Digite a kilometragem percorrida: \n"))
temp = float(input("Digite o tempo gasto: \n"))
if temp == 0:
    print("Tempo invalido, tem que ser maior que zero")
else:
    media = (vel / temp)
    print(media)