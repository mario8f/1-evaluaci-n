#Identificadorfecha
def fecha():
    c=input("introduzca un año ")
    repetir=True
    while (repetir==True):
        a=input("introduzca un dia del mes ")
        repetir= (a<1) or (a>31)
        if(repetir==True):
            print("error: has introduciodo un dia inexistente ")
       
    repetir=True
    while (repetir==True):
        b=input("introduzca un mes del año ")
        repetir= (b<1) or (b>12)
        if(repetir==True):
            print("error: has introducido un mes inexistente ")
     
    if b==1:
        b= "Enero"
    if b==2:
        b= "Febrero"
    if b==3:
        b= "Marzo"
    if b==4:
        b= "Abril"
    if b==5:
        b= "Mayo"
    if b==6:
        b= "Junio"
    if b==7:
        b= "Julio"
    if b==8:
       b= "Agosto"
    if b==9:
       b= "Septiembre"
    if b==10:
        b= "Octubre"
    if b==11:
        b= "Noviembre"
    if b==12:
        b= "Diciembre"
    print a," ",b," ",c
fecha()
    
