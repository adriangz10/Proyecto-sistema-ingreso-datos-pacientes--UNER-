from funciones import imprimir_titulo, menu_de_seleccion, historia_clinica, imprimir_una_sola_histoia_clinica, comprobar_si_json_tiene_datos, leer_datos_de_json, escribir_datos_en_json, seleccion_pacientes, seleccion_historias_clincas, imprimir_historia_clinica_con_paciente, buscador_pacientes, menu_historias_clinicas
import time

def inicio_area_historia_clinica():

    while True:

        imprimir_titulo("HISTORIAS CLINICAS")

        seleccion = menu_historias_clinicas()

        if seleccion == 1:
            
            imprimir_titulo("Nueva historia clinica")

            datos = historia_clinica()

            imprimir_una_sola_histoia_clinica(datos)
        
            time.sleep(4)

            base = []

            nombre_archivo = "Trabajo integrador/datos_historia_clinica.json"

            if comprobar_si_json_tiene_datos(nombre_archivo):
                base = leer_datos_de_json(nombre_archivo)

            base.append(datos)

            escribir_datos_en_json(base, nombre_archivo)
                                    
        elif seleccion == 2:

            imprimir_titulo("Asignar hiatoria clinica a paciente")

            nombre_archivo_pacientes = "Trabajo integrador/datos_pacientes.json"

            nombre_archivo_historias_clinicas = "Trabajo integrador/datos_historia_clinica.json"

            datos = leer_datos_de_json(nombre_archivo_pacientes)

            historia = leer_datos_de_json(nombre_archivo_historias_clinicas)

            dos_datos = seleccion_pacientes(datos)
            indice = dos_datos[1]
            nuevo_dato = dos_datos[0]
            del datos[indice]

            dos_datos_clinica = seleccion_historias_clincas(historia)
            indice_dos = dos_datos_clinica[1]
            nueva_clinica = dos_datos_clinica[0]
            del historia[indice_dos]

            escribir_datos_en_json(datos, nombre_archivo_pacientes)

            escribir_datos_en_json(historia, nombre_archivo_historias_clinicas)

            union = nuevo_dato | nueva_clinica

            imprimir_historia_clinica_con_paciente(union)

            time.sleep(5)

            base = []

            nombre_archivo_union = "Trabajo integrador/datos_union_clinica_paciente.json"

            if comprobar_si_json_tiene_datos(nombre_archivo_union):
                base = leer_datos_de_json(nombre_archivo_union)

            base.append(union)

            escribir_datos_en_json(base, nombre_archivo_union)

        elif seleccion == 3:

            nombre_archivo = "Trabajo integrador/datos_union_clinica_paciente.json"

            busqueda = leer_datos_de_json(nombre_archivo)

            imprimir_titulo("Buscar Paciente")

            datos = buscador_pacientes(busqueda)

        elif seleccion == 0:
            print("Saliendo...")
            time.sleep(3)
            break