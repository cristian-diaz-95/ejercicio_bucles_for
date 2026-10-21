"""
Caso. Una pantalla debe presentar todos los enteros comprendidos entre dos límites A y B,
ambos incluidos, empezando por A y terminando en B. Los límites son enteros entre -100 y
100. Si coinciden, presente ese único valor.
Fórmula o relación: El paso entre términos es 1 si A ≤ B y -1 si A > B.
"""
a=int(input(" ingrese entero A: "))
b=int(input("ingrese entero B: "))
if (-100< a and b) and (a and b <100):
    if a <=b:
        for i in range(a,b+1,1):
            print(i)
    elif a>b:
        for i in range(a,b-1,-1):
            print(i)
else:
    print("supera los limites")