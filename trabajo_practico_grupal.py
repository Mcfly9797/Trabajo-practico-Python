
# Validacion de valores positivos, en este caso solo se tendra en cuenta este tipo de validacion
def es_positivo(valor):
    flag = False
    if valor > 0:  # Verifico que el valor no sea negativo
        flag = True
    return flag


# Valido que la calidad este entre 0.5 y 1
def valido_calidad(calidad):  # Recibo un valor
    flag = False
    # Valido que el numero ingresado sea mayor que cero.
    if calidad >= 0.5 and calidad <= 1:
        flag = True
    return flag


# Funcion que recepciona y orquesta la validacion de los datos ingresados, el valor id se ingresa previamente para validar si es nulo antes de ingresar a esta funcion
def ingreso_dat_buque(id, buques_id):

    while id in buques_id:  # Valido que el id ingresado no este repetido entre los que fueron ingresados
        id = str(input("Ingreso un buque repetido, vuelva a intentar:"))

    tipo_cereal = str(input("Escriba 'Soja' o 'Girasol' dependiendo del tipo de cereal:")).lower()
    print ('Ingreso este cereal en minuscula:{}'.format(tipo_cereal))
    while tipo_cereal in ['girasol','soja'] ==False:  # Valido que sea del tipo solicitado
        tipo_cereal = str(input("Ingreso valor erroneo, vuelva a intentar:")).lower()

    peso = int(input("Ingrese el peso del cereal en kg: "))
    while es_positivo(peso) == False:  # Valido que el peso sea un valor positivo
        peso = int(input("Ingreso valor negativo. Vuelva a intentar: "))

    calidad = float(input("Ingrese calidad de cereales entre 0.5 y 1: "))
    # Valido que el rango de calidad sea correcto
    while valido_calidad(calidad) == False:
        calidad = float(input("Ingreso calidad erronea. Vuelva a intentar: "))

    #print("El id del buque es {}, el tipo de cereal es {}, el peso del cereal es {}Kg y el coeficiente de calidad es {}".format (id,tipo_cereal,peso,calidad))

    return id, tipo_cereal, peso, calidad


def ingreso_dat_sem():
    dolar = int(input("Ingrese el precio del dolar: "))
    while es_positivo(dolar) == False:  # Valido que el peso sea un valor positivo
        dolar = int(input("Ingreso valor negativo. Vuelva a intentar: "))

    precio_grsl = int(input("Ingrese el precio del girasol: "))
    # Valido que el peso sea un valor positivo
    while es_positivo(precio_grsl) == False:
        precio_grsl = int(input("Ingreso valor negativo. Vuelva a intentar: "))

    precio_soja = int(input("Ingrese el precio de la soja: "))
    # Valido que el peso sea un valor positivo
    while es_positivo(precio_soja) == False:
        precio_soja = int(input("Ingreso valor negativo. Vuelva a intentar: "))

    return dolar, precio_grsl, precio_soja


def calculo_facturacion(valor_dolar, precio_cereal, peso, calidad, tipo_cereal):


    #Transformo el peso de los cereales a toneladas
    peso_tn = peso / 1000
    print("toneladas:", peso_tn) #debug
    #Calculo el tiempo de uso de la cinta transportadora (1200 tn/hora)
    tiempo_cinta = peso_tn / 1200
    print("tiempo_cinta:", tiempo_cinta) #debug
    #Calculo valor del cereal (precio del cereal por tn * cantidad * coeficiente calidad)
    valor_cereal = precio * peso_tn * calidad
    print("valor_cereal", valor_cereal) #debug
    #Calculo el monto de facturacion por embarque
    monto_facturacion = valor_cereal * 0.0020 + (500 * tiempo_cinta * valor_dolar)
    print("monto facturacion: ", monto_facturacion)
    #Calculo la cantidad de embarques acumulados por tipo de cereal
    
    # Calculo el monto de facturacion por embarque
    monto_facturacion = (precio_cereal * (peso / 1000) * calidad) * (0.0020 + (500 * ((peso / 1000) / 1200) * valor_dolar))

    return monto_facturacion


# Determino la máxima facturación
def calc_max(monto_facturacion, max_facturacion):
    if max_facturacion < monto_facturacion:
        max_facturacion = monto_facturacion
    return max_facturacion


# Flujo principal de programa
def main():

    # Inicializo variables y acumuladores
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

    buques_id = []  # Inicializo lista de ID de buques vacia para su posterior carga

    # Solicito datos generales semanales
    dolar, precio_grsl, precio_soja = ingreso_dat_sem()

    # Solicito por unica vez id de buque previo a ingresar al programa
    id = str(input('Ingrese id del buque. Finaliza al ingresar un valor vacio: '))
    while id != '':  # Espero datos de buque hasta que se ingrese un valor vacio

        id, tipo_cereal, peso, calidad = ingreso_dat_buque(id, buques_id)
        buques_id.append(id)  # Agrego el id al listado de ids de buque


        if tipo_cereal == "girasol":
            precio_cereal = precio_grsl         #Actualizo el precio del cereal actual dependiendo el cereal que ingreso
            embarq_sem_grsl += 1                # Aumento acumuladores de cantidad de cargamentos segun su tipo
            peso_total_girasol = peso/1000      # Calculo la cantidad total de cereal por tipo acumulado hasta el momento
        else:
            precio_cereal = precio_soja 
            embarq_sem_soja += 1
            peso_total_soja = peso/1000    

        # Realizo el calculo de monto facturacion
        monto_facturacion = calculo_facturacion(dolar, precio_cereal, peso, calidad, tipo_cereal)

        # Impresion monto facturacion por cada embarque
        print("La facturacion del embarque {} es de {}".format(id, monto_facturacion))

        # Sumo esta facturacion al monto total de facturacion semanal
        fact_total_semana += monto_facturacion

        # Calculo maximo de facturacion
        max_facturacion = calc_max(monto_facturacion, max_facturacion)

        
        print('---------------------------------------------------------------------------------------------')

        # Vuelvo a pedir el id al ingresar al buque
        id = str(input('Ingrese id del buque. Finaliza al ingresar un valor vacio: '))
    # Calculo la cantidad total de embarques despachados en la semana sumando los embarques por cada tipo de cereal
    embarques_totales = embarq_sem_grsl + embarq_sem_soja
    print('Carga finalizada')

    # Al finalizar carga semanal imprimo los datos solicitados
    print("Cantidad total de embarques de soja: {}".format(embarq_sem_soja))
    print("Cantidad total de embarques de girasol: {}".format(embarq_sem_grsl))
    print("Maxima facturacion registrada: {}".format(max_facturacion))
    print("El monto total de facturacion semanal es: ", fact_total_semana)
    input('Presione cualquier tecla para finalizar')


main()
