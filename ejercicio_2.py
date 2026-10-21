"""
Caso. Se conoce el primer término A, la diferencia D y la cantidad N de términos de una
progresión. A y D son enteros entre -100 y 100, y N está entre 0 y 1000. Determine la suma de
los N términos; si N es cero, el total es cero.
Fórmula o relación: t1 = A; tk+1 = tk + D; S = t1 + t2 + ... + tn.
"""
a=int(input("ingrese termino A: "))
d=int(input("ingrese diferencia D: "))
n=int(input("cantidad N: "))
if -100 <= a <= 100 and -100 <= d <= 100 and 0 <= n <= 1000:
    suma=0
    t1=a
    for i in range(n):
        suma=suma+t1
        t1=t1+d
    print(suma)
else:
    print("valor invalido")
