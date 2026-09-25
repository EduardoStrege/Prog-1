n1 = int(input("Digite seu numero: \n"))
n2 = int(input("Digite seu outro numero: \n"))
if n2 == 0:
    print("Denominador igual a 0, impossivel realizar a conta! ")
else:
    resultado = n1 / n2
    print(f"Resultado é {resultado}") 