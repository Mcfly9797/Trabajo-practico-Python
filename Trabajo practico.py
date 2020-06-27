
##Validacion id recorrida listas
def valido_id(id,lista_buques)
    flag = False
    for i in lista_buques():
        if id==lista_buques[i].[1]: ##REVISAR
            flag =True
    return flag

##Valido que cereal sea soja o girasol
def valido_cereal(tipo_cereal):
    flag = False
        if tipo_cereal == "Soja" or tipo_cereal == "Girasol"                                #Valido si el valor ingresado no coincide con los tipos de cereales 
            flag True   
    return flag

#Validacion de valores positivos, en este caso solo se tendra en cuenta este tipo de validacion
def es_positivo(valor)
    flag = False
    if valor >= 0:                                                                         #Verifico que el valor no sea negativo
        flag=True

    return Flag

##Valido que la calidad este entre 0.5 y 1
def valido_calidad(calidad):                                                                #Recibo un valor
    flag = False
    if calidad >= 0.5 and calidad <= 1:                                                     #Valido que el numero ingresado sea mayor que cero.
        flag=True

    return flag


##Funcion que recepciona y orquesta la validacion de los datos ingresados, el valor id se ingresa previamente para validar si es nulo antes de ingresar a esta funcion
def ingreso_dat_buque(lista_buques,id_buque):

    while !valido_id_repetido(id_buque,lista_buques):                                       #Valido que no se repita id
        id_buque = str(input("Ingreso un buque repetido, vuelva a intentar:"))              
    

    tipo_cereal = str(input("Escriba 'Soja' o 'Girasol' dependiendo del tipo de cereal:"))  
    while !valido_cereal(tipo_cereal)                                                       #Valido que sea del tipo solicitado
        tipo_cereal = str(input("Ingreso valor erroneo, vuelva a intentar:"))               
    

    
    
    peso = int(input("Ingrese el peso del cereal en kg: "))
    while !valido_positivo(peso)                                                            #Valido que el peso sea un valor positivo
        peso = int(input("Ingreso valor negativo. Vuelva a intentar: "))    
    
    
    
    
    calidad = float(input("Ingrese calidad de cereales entre 0.5 y 1: "))
    while !valido_calidad(calidad)                                                          #Valido que el rango de calidad sea correcto
        calidad = int(input("Ingreso calidad erronea. Vuelva a intentar: "))    




    nodo_buque = id_buque,tipo_cereal,peso,calidad                                          #Una vez validados todos los datos, creo un nodo y lo devuelvo para agregarlo a la lista

    return nodo_buque

#Datos generales semanales
input dolar
valido
input precio girasol
valido
input precio soja
valido



inicializo lista de buques

mientras el id buque ingresado no sea nulo entro a la funcion
    #Datos por buque seran solicitados hasta que el buque ingresado este "" (vacion)
    input idbuque
    valido id no repetido recorriendo lista de buques
    input tipo_cereal
    valido si es "soja" "girasol"
    input peso
    valido que sea positivo
    input calidad
    valido que tenga un rango entre 0.5 y 1

inicializo acumuladores
calculo costo operativo
realizo comparaciones de maximos solicitado


Al finalizar carga semanal imprimo los datos solicitados



