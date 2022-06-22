from funciones import imprimir_titulo, menu_de_seleccion, leer_datos_de_json, ver_listado_profesionales,datos_profesionales, imprimir_un_solo_dato_profesional, comprobar_si_json_tiene_datos, escribir_datos_en_json
import time

while True:

    imprimir_titulo("PROFESIONALES")

    seleccion = menu_de_seleccion()

    if seleccion == "7":

        imprimir_titulo("Listado de medicos")

        nombre_archivo = "Trabajo integrador/datos_profesionales.json"

        datos = leer_datos_de_json(nombre_archivo)

        ver_listado_profesionales(datos)

    elif seleccion == "8":

        imprimir_titulo("Agregar nuevo profesional")

        datos = datos_profesionales()

        imprimir_un_solo_dato_profesional(datos)
    
        time.sleep(5)

        base = []

        nombre_archivo = "Trabajo integrador/datos_profesionales.json"

        if comprobar_si_json_tiene_datos(nombre_archivo):
            base = leer_datos_de_json(nombre_archivo)

        base.append(datos)

        escribir_datos_en_json(base, nombre_archivo)