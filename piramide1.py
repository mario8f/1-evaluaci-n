def piramide_1():
    filas=input("Dime la altura de pisos ")
    espacios=' '
    asteriscos='*'
    for i in range(filas):
        for nespacios in range(1,filas-i-1):
            espacios=espacios+' '
        for nasteriscos in range(1,2*i):
            asteriscos=asteriscos+'*'
        #escribo de golpe toda la fila
        print espacios + asteriscos
        espacios=' '
        asteriscos='*'
        #paso a la siguinte fila
        
piramide_1()
    
