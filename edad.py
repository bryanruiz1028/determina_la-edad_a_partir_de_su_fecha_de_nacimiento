año_actual=2021
mes_actual=11
dia_actual=6
edad=0
a=1
bisiesto=1
bisiesto_actual=1
edadaño=0
edadmes=0
edaddia=0
casox=0
#ingreso el año verificando que sean correctos 
año_actual=int(input("ingresa el año actual  "))
while True:
    año=int(input("ingresa el año de nacimiento "))
    if (año>año_actual):
        print("porfaor ingrese su año de nacimiento correcto ")
    else :
        break 
#------------------------------
# tengo que saber si es año bisiesto 
if año_actual % 4!=0:
	    bisiesto_actual=0
elif año_actual % 4==0 and año_actual % 100!=0:
	    bisiesto_actual=1
elif año_actual % 4==0 and año_actual % 100==0 and año_actual % 400!=0:
	    bisiesto_actual=0
elif año_actual % 4==0 and año_actual % 100==0 and año_actual % 400==0:
	    bisiesto_actual=1

if año % 4!=0:
	    bisiesto=0
elif año % 4==0 and año_actual % 100!=0:
	    bisiesto=1
elif año % 4==0 and año_actual % 100==0 and año_actual % 400!=0:
	    bisiesto=0
elif año % 4==0 and año_actual % 100==0 and año_actual % 400==0:
	    bisiesto=1
#---------------------------------------------
#se ingresan el mes  y se verifican que esten correctos 
while True:
    mes_actual=int(input("ingresa el mes actual  "))
    if mes_actual<=12:
        break
    else :
        print("ingrese un mes actual correcto")

if  año==año_actual :
    casox=1

while casox==1:
    mes=int(input("ingresa el mes de nacimiento   "))

    if (mes<=12 )and (mes_actual >= mes ) :  
        break
    else :
        print("ingrese un mes de nacimiento  correcto")

while casox==0:
    mes=int(input("ingresa el mes de nacimiento   "))

    if (mes<=12 ) :  
        break
    else :
        print("ingrese un mes de nacimiento  correcto")

#se ingrea el dia actual verificando que se puedan ingresar los numeros correctos 
if (mes_actual==1 or mes_actual== 3 or mes_actual== 5 or mes_actual== 7 or mes_actual==  8 or mes_actual==  10 or mes_actual== 12 ): 
    while True:
        dia_actual=int(input("ingrese el dia actua "))
        if (dia_actual< 32 ):
            break
        else:
            print("ingrese el dia actual correcto ")
elif(mes_actual== 4 or mes_actual==6 or mes_actual==11 or mes_actual==9 ):
    while True:
        dia_actual=int(input("ingrese el dia actua "))
        if (dia_actual< 31):
            break
        else:
            print("ingrese el dia actual correcto ")
elif (mes_actual==2 and bisiesto_actual==1 ):
    while True:
        dia_actual=int(input("ingrese el dia actua "))
        if (dia_actual< 30):
            break
        else:
            print("ingrese el dia actual correcto ")
elif (mes_actual==2 and bisiesto_actual==0 ):
    while True:
        dia_actual=int(input("ingrese el dia actua "))
        if (dia_actual<= 28):
            break
        else:
            print("ingrese el dia actual correcto ")
#-------------ingresamos el dia de nacimiento y verificamos 
casox=0
if año_actual==año and mes==mes_actual:
    casox=1
while casox==0:
    if (mes==1 or mes== 3 or mes== 5 or mes== 7 or mes==  10 or mes== 12 ): 
        while True:
            dia=int(input("ingrese el dia de nacimiento "))
            if (dia< 32):
                casox=3
                break
            else:
                print("ingrese el dia de nacimiento correcto ")
    elif(mes== 4 or mes==6 or mes==11 or mes==9 ):
        while True:
            dia=int(input("ingrese el dia de nacimiento "))
            if (dia< 31):
                casox=3
                break
            else:
                print("ingrese el dia de nacimiento correcto ")
    elif (mes==2 and bisiesto==1 ):
        while True:
            dia=int(input("ingrese el dia de nacimiento "))
            if (dia< 30):
                casox=3
                break
            else:
                print("ingrese el dia de nacimiento correcto ")
    elif(mes==2 and bisiesto==0 ):
        while True:
            dia=int(input("ingrese el dia de nacimiento "))
            if (dia< 29):
                casox=3
                break
            else:
                print("ingrese el dia de nacimiento correcto ")
#--------------------------------------------------------
while casox==1:
    dia=int(input("ingrese el dia de nacimiento "))
    if dia<=dia_actual:
        break
    else:
        print("ingrese el dia de nacimiento correcto ")
#--------------------------------
print("fecha actual",año_actual,mes_actual,dia_actual)
print("fecha de nacimiento",año,mes,dia)
if mes_actual==mes and dia_actual==dia:
    print("FELIZ CUMPLE")

edadaño=año_actual-año
if mes>mes_actual:
    edadaño=edadaño-1
    mes_actual=mes_actual+12
    edadmes=mes_actual-mes
else :
    edadmes=mes_actual-mes
if dia>dia_actual:
    edadmes=edadmes-1
    dia_actual=dia_actual+30
    edaddia=dia_actual-dia
else:
    edaddia=dia_actual -dia
if edadmes<0:
    edadaño=edadaño-1
    edadmes=11
print("la edad ",edadaño,edadmes,edaddia)



