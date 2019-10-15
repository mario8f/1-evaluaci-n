#Identicador numero primo
def primo():
    numero=input("Escribir un numero ")
    primo=True
    for i in range(2,numero):
        if(numero%i==0):
            primo=False
    if (primo==True):
        print "Es rimo"
    else:
        print "No es primo"
primo()
