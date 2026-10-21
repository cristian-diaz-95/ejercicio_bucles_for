"""
Caso. Se reciben N empleados, con 1 ≤ N ≤ 40. Cada registro contiene, en este orden,
identificador entero positivo único, edad entera no negativa en años y años enteros de
antigüedad entre 1 y 50. El sueldo ficticio es la suma de una base de 100 unidades monetarias,
el valor numérico de la edad y la suma de los enteros desde 1 hasta la antigüedad; toda esa
suma se divide entre los años de antigüedad. La edad y la suma de años se consideran aportes
numéricos en unidades monetarias dentro de este modelo ficticio. Informe el sueldo de cada

empleado, el total de la nómina y los identificadores con mayor y menor sueldo. En empate
conserve el primero recibido.
Fórmula o relación: Sueldo = (100 + edad + (1 + 2 + ... + antigüedad))/antigüedad.
"""
n=int(input("cantidad de empleados: "))
salida=""
sueldo=0
anti=0
menor=0
mayor=0
mayor_suel=0
menor_suel=0
nomina=0
if 1<=n<=40:
    for i in range(n):
        identificador=int(input("identificador unico del empleado: "))
        edad=int(input("ingrese edad del empleado: "))
        antiguedad=int(input("ingrese antiguedad del empleado: "))
        if (0<=identificador)and(0<edad)and(1<=antiguedad<=50):
                anti=(antiguedad * (antiguedad + 1)) // 2
                sueldo=(100+edad+anti)/antiguedad
                nomina+=sueldo
                salida += str(identificador) + ": " + str(sueldo)+"  "
                if menor==0 or mayor==0:
                    menor=sueldo
                    mayor=sueldo
                    mayor_suel=identificador
                    menor_suel=identificador
                if menor>sueldo:
                    menor=sueldo
                    menor_suel=identificador
                if sueldo>mayor:
                    mayor=sueldo
                    mayor_suel=identificador                  
        else:
            print("no cumple parametros") 
    print(salida)
    print("menor: ",menor_suel) 
    print("mayor: ",mayor_suel)
    print("la nomina es: ",nomina)           