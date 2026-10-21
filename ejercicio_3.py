"""
Caso. Una empresa tiene N empleados, con 0 ≤ N ≤ 1000. Se recibe el sueldo no negativo de
cada empleado y se desea el total de la nómina. Para una empresa sin empleados, el total es
cero.
Fórmula o relación: Nómina = sueldo1 + sueldo2 + ... + sueldon.
"""
n=int(input("ingrese numero de empleados: "))
nomina=0
if 0<=n<=1000:
    for i in range(n):
        sueldo=int(input("ingrese el sueldo: "))
        nomina=nomina+sueldo
    print(nomina)
else:
    print("valores invalidos")
