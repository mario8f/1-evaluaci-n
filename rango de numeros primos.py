#Detector en un rango de numeros primos
def rango_primo():
    a=input("Escribir un numero ")
    b=input("Escribir un numero ")
    primo=True
    for i in range(a,b+1):
        for n in range(2,i):
            if(i%n==0):
                primo=False
        if (primo==True):
             print i,"Es primo"
        else:
             print i,"No es primo"
        primo=True
rango_primo()
