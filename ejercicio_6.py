"""
Caso. Se reciben los tiempos de N ciclistas, con 1 ≤ N ≤ 20, sobre una vuelta de 250 metros.
Cada registro contiene identificador entero positivo único, minutos enteros no negativos,
segundos entre 0 y 59 y centésimas entre 0 y 99. Cada tiempo total es positivo. Informe la
velocidad media de cada ciclista en kilómetros por hora y el identificador del ganador. En
empate de tiempo gana el primero recibido.
Fórmula o relación: Tiempo en segundos T = 60 × minutos + segundos + centésimas/100;
velocidad = 900/T. Menor T determina el ganador.
"""
n=int(input("ingrese cantidad de ciclistas: "))
salida=""
menor=0
v=0
if 1<=n<=20:
    for i in range(n):
        identi=int(input("identificador del ciclista: "))
        minutos=int(input("minutos que se demoro "))
        segundos=int(input("segundos que demoro "))
        centesi=int(input("centesimas que demoro "))
        if (0<=identi)and(0<=minutos)and(0<=segundos<=59)and(0<=centesi<=99):
            t=(60*minutos)+segundos+(centesi/100)
            v=900/t
            salida+=str(identi)+": "+str(v)+" km/h"+"  "
            if menor==0:
                menor=t
            if t<menor:
                menor=t
                ganador=identi
        else:
            print("valores invalidos")
    print(salida)                       
    print("ganador:",ganador)         
else:
    print("cantidad invalida")          
        
        