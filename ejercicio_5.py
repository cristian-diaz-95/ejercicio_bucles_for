"""
Caso. Un vendedor tiene N ventas, con 0 ≤ N ≤ 1000, y se recibe el importe no negativo de cada
una. Informe cuántas fueron de 200 o menos, cuántas superaron 200 sin llegar a 400 y cuántas
fueron de 400 o más. Una venta pertenece a un solo grupo.
Fórmula o relación: Grupo 1: v ≤ 200; grupo 2: 200 < v < 400; grupo 3: v ≥ 400.
"""
n=int(input("ingrese cantidad de ventas: "))
if 0<=n<=1000:
    menores_de_200=0
    entre_200_400=0
    mas_400=0
    for i in range(n):
        venta=int(input("ingrese valor de la venta: "))
        if venta<=200:
            menores_de_200=menores_de_200+1
        elif 200<venta<400:
            entre_200_400=entre_200_400+1
        elif 400<=venta:
            mas_400=mas_400+1
    print(" las ventas menores o iguales a 200 son: ",menores_de_200)
    print("las ventas entre 200 y 400 son: ",entre_200_400)
    print("las ventas iguales o superiores a 400 son: ",mas_400)
else:
    print("valor invalido")
