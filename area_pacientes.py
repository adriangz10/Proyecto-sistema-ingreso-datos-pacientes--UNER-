from funciones import imprimir_titulo, menu_de_seleccion, datos_pacientes, imprimir_un_solo_paciente, comprobar_si_json_tiene_datos, leer_datos_de_json, escribir_datos_en_json, eliminar_paciente, editar_datos_pacientes
import time

def inicio_area_pacientes():
    
    while True:

        imprimir_titulo("Instituto Medico las Lurcienegas")

        seleccion = menu_de_seleccion()

        if seleccion == 1:

            imprimir_titulo("Agregar un paciente")

            datos = datos_pacientes()

            imprimir_un_solo_paciente(datos)

            time.sleep(5)

            base = []

            nombre_archivo = "Trabajo integrador/datos_pacientes.json"

            if comprobar_si_json_tiene_datos(nombre_archivo):
                base = leer_datos_de_json(nombre_archivo)

            base.append(datos)

            escribir_datos_en_json(base, nombre_archivo)

        elif seleccion == 2:

            nombre_archivo = "Trabajo integrador/datos_pacientes.json"

            eliminar = leer_datos_de_json(nombre_archivo)

            imprimir_titulo("ELIMNAR UN PACIENTE")

            datos = eliminar_paciente(eliminar)
            
            blanco = ()
            escribir_datos_en_json(blanco, nombre_archivo)

            escribir_datos_en_json(eliminar, nombre_archivo)

        elif seleccion == 3:

            nombre_archivo = "Trabajo integrador/datos_pacientes.json"

            editar = leer_datos_de_json(nombre_archivo)

            imprimir_titulo("EDITAR DATOS PACIENTE")

            datos = editar_datos_pacientes(editar)

            escribir_datos_en_json(datos, nombre_archivo)

        elif seleccion == 0:
            print("Saliendo...")
            time.sleep(3)
            break
        