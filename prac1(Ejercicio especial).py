################ funcion de decifrado ###########
rango="abcdefghijklmnopqrstuvwxyz"
def decifrado(contra,clave):
    decifracion=""
    for i in contra:
        posicion=rango.find(i)- clave
        mod=int(posicion)% len(rango)
        decifracion=decifracion+str(rango[mod])
    return decifracion.lower()
################

def divicionsinop(a,b):
    #a=int(input("ingresa el dividendo:  "))
    #b=int(input("ingresa el divisor:  "))
    if(a>=b and b!=0):
        aux=a
        cociente=0
        a=a-b
        print(aux," - ",b,"=",a)
        while a>=0:
            a=a-b
            resta=a-b
            if a>0 and resta>0:
                print(a," - ",b, " = ",resta)
            cociente=cociente+1
        #print("la cociente es:  ",cociente)
        #resto=aux-b*cociente
        #print("El residuo es:  ",resto)
        return cociente
    else:
        print("el divisor es mas grande que el dividendo\n no puedo dividir con decimales por el momento\n O talves quieres dividir entre cero y eso es algo que no esta definido!!!")

def residuo(a,b):
    #a=int(input("ingresa el dividendo:  "))
    #b=int(input("ingresa el divisor:  "))
    if(a>=b and b!=0):
        aux=a
        cociente=0
        a=a-b
        #print(aux," - ",b,"=",a)
        while a>=0:
            a=a-b
            #resta=a-b
            #if a>0 and resta>0:
                #print(a," - ",b, " = ",resta)
            cociente=cociente+1
        #print("la cociente es:  ",cociente)
        resto=aux-b*cociente
        #print("El residuo es:  ",resto)
    else:
        print("el divisor es mas grande que el dividendo\n no puedo dividir con decimales por el momento\n O talves quieres dividir entre cero y eso es algo que no esta definido!!!")
    return resto

def menu():
    print("Ahora decide que operacion deseas realizar: ")
    print(" \n=======%/=%/=%/°°°°°°°/=%/=%/======")
    print("1. División de 2 Números:\n2. Divisores:\n3. Números Capicua:\n4. Cambio de Base:\n5. SALIR")
    print("=======%/=%/=%/°°°°°°°/=%/=%/======")
    
def identificadordecapicuasdeunacadena(a):
    c=""
    for i in a:
        c=i+c
    #   print(c)
    if c.lower()==a.lower():
        controldetamaño=len(c)
        if controldetamaño!=1 and controldetamaño!=2:
            print("capicua encontrado", c)
        else:
            print("este numero es capicua:  ",c," pero no se lo toma en cuenta por ser cararter de:  ",controldetamaño)
    #else:
        #print("no espalindrome")

def divicionsinopV2(a,b):
    #a=int(input("ingresa el dividendo:  "))
    #b=int(input("ingresa el divisor:  "))
    if(a>=b and b!=0):
        #aux=a
        cociente=0
        a=a-b
        #print(aux," - ",b,"=",a)
        while a>=0:
            a=a-b
            #resta=a-b
            #if a>0 and resta>0:
                #print(a," - ",b, " = ",resta)
            cociente=cociente+1
        #print("la cociente es:  ",cociente)
        #resto=aux-b*cociente
        #print("El residuo es:  ",resto)
        return cociente
    else:
        print("el divisor es mas grande que el dividendo\n no puedo dividir con decimales por el momento\n O talves quieres dividir entre cero y eso es algo que no esta definido!!!")

def residuoV2(a,b):
    #a=int(input("ingresa el dividendo:  "))
    #b=int(input("ingresa el divisor:  "))
    if(a>=b and b!=0):
        aux=a
        cociente=0
        a=a-b
        #print(aux," - ",b,"=",a)
        while a>=0:
            a=a-b
            #resta=a-b
            #if a>0 and resta>0:
                #print(a," - ",b, " = ",resta)
            cociente=cociente+1
        #print("la cociente es:  ",cociente)
        resto=aux-b*cociente
        #print("El residuo es:  ",resto)
    else:
        print("el divisor es mas grande que el dividendo\n no puedo dividir con decimales por el momento\n O talves quieres dividir entre cero y eso es algo que no esta definido!!!")
    return resto

def cambiodebase(n,x):
    if n>x:
        cociente=divicionsinopV2(n,x) #n//x
        restoauxi=residuoV2(n,x)#n%x
        recive=""
        while cociente>=x:
            restos=residuoV2(cociente,x) #cociente%x
            res=str(restos)
            recive=res+recive
            #print(restos)
            cociente=divicionsinopV2(cociente,x)#cociente//x
            #print(cociente)
            
            

        coci=str(cociente)
        res=str(restoauxi)  
        num=coci+recive+res
        print("El numero: ",n," en base: ",x,"es igual a :  ",num)
# funciones y procedimientos

def analizador(entrada):
    print("la entera es: " + entrada)
    tamañodecadena=int(len(entrada))
    sum1=0
    sum2=3
    cont=0
    #envio=0
    while cont<tamañodecadena:
        subcadena=entrada[sum1:sum2]
        envio=subcadena
        identificadordecapicuasdeunacadena(envio)
        #print(subcadena)
        sum1+=1
        sum2+=1
        cont+=1
        #print("el contador icremento en : ",cont)

usuario="eleazar"
entrada=str(input("ingresa el nombre de usuario:  "))
if entrada.lower()==usuario:
    #EL usuario es : eleazar
    #la contraseña es:  lznyfw
    # la clave numerica es : 5
    contraseña=str(input("======== ¡CORRECTO! ========\nAhora ingresa la contraseña:  "))
    clavenum=int(input("ingresa la clave numerica: "))
    contradeci=decifrado(contraseña,clavenum)
    if contradeci=="guitar":
        print(" \n==================\nCONTRA SEÑA CORRECTA\n==================\n \n========/*-/*-/*-/*-/*-/*-/*-/*-========\n        INICIA EL PROGRAMA\n========/*-/*-/*-/*-/*-/*-/*-/*-========")
        menu()
        sw=int(input(" \n==== ELIGE UNA OPCION ====\nIngresa el numero de operacion que elegiste:  "))
        while sw!=5:
            menu()
            if sw==1:
                print(" \n °°°°°° ELEGISTE LA OPCION 1 °°°°°°\nDivisión de 2 Números: ")
                a=int(input("ingresa el dividendo:  "))
                b=int(input("ingresa el divisor:  "))
                print("la cociente es:  ",divicionsinop(a,b))
                print("El residuo es:  ",residuo(a,b)) 
                menu()
            elif sw==2:
                print(" \n /%/%/%/%/  ELEGISTE LA OPCION 2 /%/%/%/%/\nDivisores: ")
                N=int(input("Ingrese el numero "))
                for i in range(1,(N+1),1):
                    if residuo(N,i)==0:
                        print("el divisor es:  ",i)
                menu()
            elif sw == 3:
                print(" \n//////// ELEGISTE LA OPCION 3 //////////\nNúmeros Capicua: ")
                x = str(input("ingrese el numero:  "))
                analizador(x)
                #pruebe con : 33323121454
                #DEBERIA SALIRLE ALGO SIMILAR AL COMENTARIO QUE ESTA DEBAJO DE ESTA LINEA
                #   la entera es: 33323121454
                #   capicua encontrado 333
                #   capicua encontrado 323
                #   capicua encontrado 121
                #   capicua encontrado 454
                #   no se imprime:   4 por ser cararter de:   1
                menu()
            elif sw == 4:
                print(" \n°--°--°--°  ELEGISTE LA OPCION 4  °--°--°--°\nCambio de Base: ")
                a=int(input("Ingrese el numero:   "))
                b=int(input("Ingrese la base de dentino:  "))
                cambiodebase(a,b)
                menu()
            sw=int(input("/+/+/+/+/°°°°°°¨¨¨¨¨¨°°°°°°/+/+/+/+/\nLA OPERACION TERMINO(mira arriba del menu)\n/+/+/+/+/°°°°°°¨¨¨¨¨¨°°°°°°/+/+/+/+/\n \nAhora decide que otra operacion del menu deseas realizar:   "))
            
        print(" \n%/=%/=%/=%/=%/=%/====°°°°¨¨¨¨°°°°====%/=%/=%/=%/=%/=%/\n        EL PROGRAMA TERMINO :) VUELVA PRONTO ;)\n%/=%/=%/=%/=%/=%/====°°°°¨¨¨¨°°°°====%/=%/=%/=%/=%/=%/")
    else:
        print("contraseña incorrecta!!")
else:
    print("no ingresaste el usuario correcto!! \n vuele a intentarlo :)")