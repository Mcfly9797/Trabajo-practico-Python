# Validacion id recorrida listas
def valido_id(id, buques_id):
    flag = True
    for i in buques_id:
        print('id ingresado {} id actual. {}'.format(id, i))
        if id == i:  # REVISAR                                                  #Recorro lista para buscar id repetido
            flag = False
    print('devuelvo un ', flag)
    return flag


# Valido que cereal sea soja o girasol
def valido_cereal(tipo_cereal):
    flag = False
    tipo_cereal = tipo_cereal.lower()
    # Valido si el valor ingresado no coincide con los tipos de cereales
    if tipo_cereal == "soja" or tipo_cereal == "girasol":
        flag = True
    return flag


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
    while (valido_id(id, buques_id) == False):  # Valido que no se repita id
        id = str(input("Ingreso un buque repetido, vuelva a intentar:"))

    tipo_cereal = str(
        input("Escriba 'Soja' o 'Girasol' dependiendo del tipo de cereal:"))
    while valido_cereal(tipo_cereal) == False:  # Valido que sea del tipo solicitado
        tipo_cereal = str(input("Ingreso valor erroneo, vuelva a intentar:"))

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


def calculo_facturacion(valor_dolar, precio_grsl, precio_soja, peso, calidad, tipo_cereal):

    if tipo_cereal == 'soja':
        precio_cereal = precio_soja
    else:
        precio_cereal = precio_grsl

    monto_facturacion = (precio_cereal * (peso / 1000) * calidad) * (0.0020 + (500 * (
        (peso / 1000) / 1200) * valor_dolar))  # Calculo el monto de facturacion por embarque

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
    id = int(input('Ingrese id del buque. Finaliza al ingresar un valor vacio: '))
    while id != '':  # Espero datos de buque hasta que se ingrese un valor vacio
        id, tipo_cereal, peso, calidad = ingreso_dat_buque(id, buques_id)

        buques_id.append(id)  # Agrego el id al listado de ids de buque

        # Realizo el calculo de monto facturacion
        monto_facturacion = calculo_facturacion(
            dolar, precio_grsl, precio_soja, peso, calidad, tipo_cereal)

        # Impresion monto facturacion por cada embarque
        print("La facturacion del embarque {} es de {}".format(
            id, monto_facturacion))

        # Sumo esta facturacion al monto total de facturacion semanal
        fact_total_semana += monto_facturacion

        # Calculo maximo de facturacion
        max_facturacion = calc_max(monto_facturacion, max_facturacion)

        if tipo_cereal == "girasol":
            embarq_sem_grsl += 1  # Aumento acumuladores de cantidad de cargamentos segun su tipo
            # Calculo la cantidad total de cereal por tipo acumulado hasta el momento
            peso_total_girasol = peso/1000
        else:
            embarq_sem_soja += 1
            peso_total_soja = peso/1000
        print('---------------------------------------------------------------------------------------------')

        # Vuelvo a pedir el id al ingresar al buque
        id = int(input('Ingrese id del buque. Finaliza al ingresar un valor vacio: '))
    # Calculo la cantidad total de embarques despachados en la semana sumando los embarques por cada tipo de cereal
    embarques_totales = embarq_sem_grsl + embarq_sem_soja
    print('Carga finalizada')

    # Al finalizar carga semanal imprimo los datos solicitados
    print("Cantidad de embarques soja Embarques totales: {}".format(embarq_sem_soja))
    print("Cantidad de embarques girasol Embarques totales: {}".format(embarq_sem_grsl))
    print("Maxima facturacion registrada: {}".format(max_facturacion))
    print("El monto total de facturacion semanal es: ", fact_total_semana)


main()
