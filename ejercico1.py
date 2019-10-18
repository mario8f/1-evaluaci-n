#multiplicacion
def ejercicio1():
    print "Escriba la multiplicacion"
    producto=0
    while(producto==0):
        a=input(" Dime la a= ")
        b=input(" Dime la b= ")
        c=input(" Dime la c= ")
        d=input(" Dime la d= ")
        producto=a*b*c*d
        if(producto==0):
           print "Error"
        else:
            print producto
    
ejercicio1()
