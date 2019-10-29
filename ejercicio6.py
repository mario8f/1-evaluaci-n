def calculadora():
    a=input("Introduzca un valor ")
    b=input("Introduzca el segundo valor ")
    c=raw_input("Introduzca el tipo de operacion (S,R,M,D) ")
    if c=='S':
        print a+b
    if c=='R':
        print a-b
    if c=='M':
        print a*b
    if c=='D':
        print a/b
calculadora()
    
    
