"""
Caso. Una inversión ficticia inicia con capital C no negativo y mantiene una tasa anual
porcentual I con 0 < I < 100. Se recibe también un entero M entre 0 y 50. El interés de cada año

es el saldo al comienzo de ese año multiplicado por I y dividido entre 100; se suma al saldo al
final del año. Determine el saldo después de M años; con M = 0 conserva el capital inicial.
Fórmula o relación: Saldo nuevo = saldo anterior × (1 + I/100).
"""
capital=int(input(" ingrese la inversion inicial: "))
i_n=int(input("ingrese tasa anual porcentual: "))
m=int(input("ingrese cantidad de anos: "))
if (0<=capital) and (0<i_n<100) and (0<m<50):
    saldo_inicial=capital
    
    for i in range(m):
        saldo_inicial=saldo_inicial*(1+i_n/100)
    print("el saldo es ",saldo_inicial)
else:
    print("valores invalidos")
    
    