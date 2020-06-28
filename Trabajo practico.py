
##Validacion id recorrida listas
def valido_id(id,buques):
    flag = False
    if len(buques)>0:                                                                       #Valido que no sea una lista vacia
        for i in lista_buques():
            if id==lista_buques[i]: ##REVISAR                                               #Recorro lista para buscar id repetido
                flag =True
    else:                                                                                   #Si la lista esta vacia el id ingresado no es repetido
        flag =True

    return flag



##Valido que cereal sea soja o girasol
def valido_cereal(tipo_cereal):
    flag = False
        if tipo_cereal == "Soja" or tipo_cereal == "Girasol"                                #Valido si el valor ingresado no coincide con los tipos de cereales 
            flag True   
    return flag



#Validacion de valores positivos, en este caso solo se tendra en cuenta este tipo de validacion
def es_positivo(valor):
    flag = False
    if valor > 0:                                                                           #Verifico que el valor no sea negativo
        flag=True

    return flag



##Valido que la calidad este entre 0.5 y 1
def valido_calidad(calidad):                                                                #Recibo un valor
    flag = False
    if calidad >= 0.5 and calidad <= 1:                                                     #Valido que el numero ingresado sea mayor que cero.
        flag=True

    return flag



##Funcion que recepciona y orquesta la validacion de los datos ingresados, el valor id se ingresa previamente para validar si es nulo antes de ingresar a esta funcion
def ingreso_dat_buque(buques,id):

    while !valido_id(id,lista_buques):                                       #Valido que no se repita id
        id = str(input("Ingreso un buque repetido, vuelva a intentar:"))              
    
    tipo_cereal = str(input("Escriba 'Soja' o 'Girasol' dependiendo del tipo de cereal:"))  
    while !valido_cereal(tipo_cereal)                                                       #Valido que sea del tipo solicitado
        tipo_cereal = str(input("Ingreso valor erroneo, vuelva a intentar:"))
    
    peso = int(input("Ingrese el peso del cereal en kg: "))
    while !es_positivo(peso)                                                                #Valido que el peso sea un valor positivo
        peso = int(input("Ingreso valor negativo. Vuelva a intentar: "))
    
    calidad = float(input("Ingrese calidad de cereales entre 0.5 y 1: "))
    while !valido_calidad(calidad)                                                          #Valido que el rango de calidad sea correcto
        calidad = int(input("Ingreso calidad erronea. Vuelva a intentar: "))   

    print("El id del buque es {}, el tipo de cereal es {}, el peso del cereal es {}Kg y el coeficiente de calidad es {}".format (id,cereal,peso,calidad))
        
    nodo_buque = id,tipo_cereal,peso,calidad                                          #Una vez validados todos los datos, creo un nodo y lo devuelvo para agregarlo a la lista

    return nodo_buque



def ingreso_dat_sem():


    dolar = int(input("Ingrese el peso del cereal en kg: "))
    while !es_positivo(dolar)                                                                #Valido que el peso sea un valor positivo
        dolar = int(input("Ingreso valor negativo. Vuelva a intentar: "))

    precio_grsl = int(input("Ingrese el peso del cereal en kg: "))
    while !es_positivo(precio_grsl)                                                          #Valido que el peso sea un valor positivo
        precio_grsl = int(input("Ingreso valor negativo. Vuelva a intentar: "))

    precio_soja = int(input("Ingrese el peso del cereal en kg: "))
    while !es_positivo(precio_soja)                                                          #Valido que el peso sea un valor positivo
        precio_soja = int(input("Ingreso valor negativo. Vuelva a intentar: "))

    nodo_dat_sem = dolar,precio_grsl,precio_soja                                             #Creo y doy valor a la tupla que devolvera los datos
    
    return nodo_dat_sem


def calculo_facturacion(valor_dolar, precio_grsl, precio_soja, peso, calidad, tipo_cereal):
    
                                                                                                            
    peso_tn = peso / 1000                                                                                       #Transformo el peso de los cereales a toneladas
    tiempo_cinta = peso_tn / 1200                                                                               #Calculo el tiempo de uso de la cinta transportadora (1200 tn/hora)
    if tipo_cereal == 'soja':                                                                                   
        valor_cereal = precio_soja * peso_tn * calida                                                           #Calculo valor del cereal (precio del cereal por tn * cantidad * coeficiente calidad)
    else
        valor_cereal = precio_grsl * peso_tn * calida                                                           #Calculo valor del cereal (precio del cereal por tn * cantidad * coeficiente calidad)
    monto_facturacion = valor_cereal * 0.0020 + (500 * tiempo_cinta * valor_dolar)                              #Calculo el monto de facturacion por embarque
    
    
    return monto_facturacion




#Flujo principal de programa
def main()

#Inicializo variables y acumuladores
embarq_sem_grsl = 0
embarq_sem_soja = 0
fact_total_semana = 0
max_facturacion = 0
peso_total_soja = 0
peso_total_girasol = 0
fact_total_semana = 0
peso_tn = 0
tiempo_cinta = 0
monto_facturacion = 0
valor_cereal = 0
embarques_totales = 0

buques_id = [ ]                                                                       #Inicializo lista de ID de buques vacia para su posterior carga


# Solicito datos generales semanales
dat_sem = ingreso_dat_sem()

id = int(input('Ingrese id del buque. Finaliza al ingresar un valor vacio'))          #Solicito por unica vez id de buque previo a ingresar al programa
    while id != '':                                                                   #Espero datos de buque hasta que se ingrese un valor vacio
        buque_dat = ingreso_dat_buque(buques,id)                                      #Recibo tupla con los datos del buque actual
        buques_id.append(buque_dat[1])                                                #Agrego el id al listado de ids, la posicion 1 es la posicion del id en las tuplas
        
        calculo_facturacion(dat_sem[1], )                                            #Realizo el calculo de costos operativos
        
        
        #calculo costo operativo
        #realizo comparaciones de maximos solicitado        



print ('Carga finalizada')

#Al finalizar carga semanal imprimo los datos solicitados



