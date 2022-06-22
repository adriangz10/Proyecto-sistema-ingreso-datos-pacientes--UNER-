import json
import time
from datetime import datetime, date

def datos_pacientes():

    while True:

        nombre = input("Nombre: ")
        control = nombre.isalpha()
        if control == False:
            print("Ingreso un parametro no valido")
            print("")
            time.sleep(3)
            continue

        apellido = input("Apellido: ")
        control = apellido.isalpha()
        if control == False:
            print("Ingreso un parametro no valido")
            print("Se reiniciara el sistema")
            time.sleep(3)
            continue

        dni = input("D.N.I: ")
        control = dni.isdigit()
        if control == False:
            print("No se permiten letras")
            print("Se reiniciara el sistema")
            time.sleep(3)
            continue
        
        nacionalidad = input("Nacionalidad: ")
        control = nacionalidad.isalpha()
        if control == False:
            print("Ingreso un parametro no valido")
            print("Se reiniciara el sistema")
            time.sleep(3)
            continue

        fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
        control = fecha_nacimiento.isalnum() 
        control_dos = fecha_nacimiento.isalpha()
        if control == True:
            print("Ingreso un parametro no valido")
            print("Se reiniciara el sistema")
            time.sleep(3)
            continue

        elif control_dos == True:
            print("No se permiten letras")
            print("Se reiniciara el sistema")
            time.sleep(3)
            continue

        datos = dict([("NOMBRE", nombre.upper()), ("APELLIDO", apellido.upper()), ("DNI", dni.upper()), ("NACIONALIDAD", nacionalidad.upper()), ("NACIMIENTO", fecha_nacimiento.upper())])
        
        return datos

def datos_profesionales ():

    while True:

        apellido = input("Apellido: ")
        control = apellido.isalpha()
        if control == False:
            print("Ingreso un parametro no valido")
            print("")
            time.sleep(3)
            continue

        nombre = input("Nombre: ")
        control = nombre.isalpha()
        if control == False:
            print("Ingreso un parametro no valido")
            print("")
            time.sleep(3)
            continue
        especialidad = input("Especialidad: ")
        control = especialidad.isalpha()
        if control == False:
            print("Ingreso un parametro no valido")
            print("")
            time.sleep(3)
            continue

        datos = dict([("APELLIDO", apellido.upper()), ("NOMBRE", nombre.upper()), ("ESPECIALIDAD", especialidad.upper())])

        return datos

def historia_clinica ():

    while True:

        fecha = input("Fecha: ")
        control = fecha.isalnum() 
        control_dos = fecha.isalpha()
        if control == True:
            print("Ingreso un parametro no valido")
            print("Se reiniciara el sistema")
            time.sleep(3)
            continue

        elif control_dos == True:
            print("No se permiten letras")
            print("Se reiniciara el sistema")
            time.sleep(3)
            continue

        enfermedad = input("Enfermedad/afeccion: ")
        control = enfermedad.isalpha()
        if control == False:
            print("Ingreso un parametro no valido")
            print("Se reiniciara el sistema")
            time.sleep(3)
            continue

        medico = input("Medico: ")
        control = medico.isalpha()
        if control == False:
            print("Ingreso un parametro no valido")
            print("Se reiniciara el sistema")
            time.sleep(3)
            continue

        observaciones = input("Observaciones: ")
        control = observaciones.isalpha()
        if control == False:
            print("Ingreso un parametro no valido")
            print("Se reiniciara el sistema")
            time.sleep(3)
            continue

        datos = dict([("FECHA", fecha.upper()), ("ENFERMEDAD", enfermedad.upper()), ("MEDICO", medico.upper()), ("OBSERVACIONES", observaciones.upper())])

        return datos

def buscador_pacientes(datos):
    while True:
        
        try:
            seleccion = int(input("""
            1 - NOMBRE
            2 - APELLIDO
            3 - FECHA DE ATENCION
            4 - ENFERMEDAD/AFECCION
            5 - MEDICO
            6 - NACIONALIDAD
            N°: """))
        except ValueError:
            print("No se permiten letras")
            time.sleep(3)
            continue
        if seleccion == 1:
            busqueda = input("NOMBRE: ").upper()
            i= 0
            d = 1
            while i < len(datos):

                for j in datos[i].items():
                    if busqueda in j:

                        print("PACIENTE", d)
                        for clave, valor in datos[i].items():
                            print("*",clave.upper(), ":", valor)
                            if clave == "NACIMIENTO":
                                edad = datetime.strptime(valor, '%d/%m/%Y')
                                dia = edad.day
                                mes = edad.month
                                ano = edad.year
                                actual = date.today()

                                armar_fecha = date(ano, mes, dia)
                                cumple = actual.year - armar_fecha.year
                                print("* EDAD PACIENTE:", cumple)
                                time.sleep(4)

                i = i + 1
                d = d + 1

        elif seleccion == 2:
            busqueda = input("APELLIDO: ").upper()
            i= 0
            d = 1
            while i < len(datos):

                for j in datos[i].items():
                    if busqueda in j:

                        print("PACIENTE", d)
                        for clave, valor in datos[i].items():
                            print("*",clave.upper(), ":", valor)
                            if clave == "NACIMIENTO":
                                edad = datetime.strptime(valor, '%d/%m/%Y')
                                dia = edad.day
                                mes = edad.month
                                ano = edad.year
                                actual = date.today()

                                armar_fecha = date(ano, mes, dia)
                                cumple = actual.year - armar_fecha.year
                                print("* EDAD PACIENTE:", cumple)
                                time.sleep(4)

                i = i + 1
                d = d + 1

        elif seleccion == 3:
            busqueda = input("FECHA DE ATENCION: ").upper()
            i= 0
            d = 1
            while i < len(datos):

                for j in datos[i].items():
                    if busqueda in j:

                        print("PACIENTE", d)
                        for clave, valor in datos[i].items():
                            print("*",clave.upper(), ":", valor)
                            if clave == "NACIMIENTO":
                                edad = datetime.strptime(valor, '%d/%m/%Y')
                                dia = edad.day
                                mes = edad.month
                                ano = edad.year
                                actual = date.today()

                                armar_fecha = date(ano, mes, dia)
                                cumple = actual.year - armar_fecha.year
                                print("* EDAD PACIENTE:", cumple)
                                time.sleep(4)

                i = i + 1
                d = d + 1

        elif seleccion == 4:
            busqueda = input("ENFERMEDAD/AFECCION: ").upper()
            i= 0
            d = 1
            while i < len(datos):

                for j in datos[i].items():
                    if busqueda in j:

                        print("PACIENTE", d)
                        for clave, valor in datos[i].items():
                            print("*",clave.upper(), ":", valor)
                            if clave == "NACIMIENTO":
                                edad = datetime.strptime(valor, '%d/%m/%Y')
                                dia = edad.day
                                mes = edad.month
                                ano = edad.year
                                actual = date.today()

                                armar_fecha = date(ano, mes, dia)
                                cumple = actual.year - armar_fecha.year
                                print("* EDAD PACIENTE:", cumple)
                                time.sleep(4)

                i = i + 1
                d = d + 1

        elif seleccion == 5:
            busqueda = input("MEDICO ").upper()
            i= 0
            d = 1
            while i < len(datos):

                for j in datos[i].items():
                    if busqueda in j:

                        print("PACIENTE", d)
                        for clave, valor in datos[i].items():
                            print("*",clave.upper(), ":", valor)               
                            if clave == "NACIMIENTO":
                                edad = datetime.strptime(valor, '%d/%m/%Y')
                                dia = edad.day
                                mes = edad.month
                                ano = edad.year
                                actual = date.today()

                                armar_fecha = date(ano, mes, dia)
                                cumple = actual.year - armar_fecha.year
                                print("* EDAD PACIENTE:", cumple)
                                time.sleep(4)

                i = i + 1
                d = d + 1
        
        elif seleccion == 6:
            busqueda = input("NACIONALIDAD ").upper()
            i= 0
            d = 1
            while i < len(datos):

                for j in datos[i].items():
                    if busqueda in j:

                        print("PACIENTE", d)
                        for clave, valor in datos[i].items():
                            print("*",clave.upper(), ":", valor)               
                            if clave == "NACIMIENTO":
                                edad = datetime.strptime(valor, '%d/%m/%Y')
                                dia = edad.day
                                mes = edad.month
                                ano = edad.year
                                actual = date.today()

                                armar_fecha = date(ano, mes, dia)
                                cumple = actual.year - armar_fecha.year
                                print("* EDAD PACIENTE:", cumple)
                                time.sleep(4)

                i = i + 1
                d = d + 1

        return datos

def eliminar_paciente(datos):
    corte = int
    while corte != 0:
        i = 0
        d = 1
        print()
        while i < len(datos):

            print("PACIENTE", d)
            for clave, valor in datos[i].items():
                print("*",clave.upper(), ":", valor)
            print()
            i = i + 1
            d = d + 1 
        try:
            indice = int(input("Numero de paciente a eliminar: "))
        except ValueError:
            print("No se permiten letras")
            time.sleep(2)
            break

        indice = indice -1
        if indice == "0":
            print("0 no esta permitido")
            time.sleep(3)
            break

        try:
            del datos[indice]
        except IndexError:
            print("El numero ingresado no contiene un paciente registrado")
            time.sleep(3.5)
            break

        time.sleep(1)
        i = 0
        d = 1
        print()
        while i < len(datos):

            print("PACIENTE", d)
            for clave, valor in datos[i].items():
                print("*",clave.upper(), ":", valor)
            print()
            i = i + 1
            d = d + 1 
        try :
            corte = int(input("Para finalizar presione 0. Para continuar 1 "))
        except ValueError:
            print("No se permiten letras")
            continue

        if corte == 1:
            continue

    return datos

def imprimir_titulo(titulo):
    print("================================")
    print(titulo)
    print("================================")

def comprobar_si_json_tiene_datos(nombre):
    with open(nombre, 'r') as f:
        if (len(f.read(1)) > 0):
            f.seek(0)
            base = json.load(f)

    return base

def escribir_datos_en_json(base, nombre):
     with open(nombre, 'w') as f:
        f.seek(0)
        json.dump(base, f, indent = 4)

def leer_datos_de_json(nombre):
    with open(nombre, 'r') as f:
        busqueda = json.load(f)
    
    return busqueda

def menu_de_seleccion():
    while True:
        menu = input("""
    PACIENTES
        1 - Agregar un paciente nuevo.
        2 - Eliminar un paciente.
        3 - Editar datos de un paciente

    HISTORIA CLINICA
        4 - Crear historia clinica.
        5 - Asignar historia clinica a un paciente.
        6 - Buscar paciente

    PROFESIONALES
        7 - Ver lista de medicos.
        8 - Agregar nuevo medico.

    PARA SALIR 0
    """).upper()
        control = menu.isdigit()
        if control == False:
            print("No se permiten letras")
            print("Re intentar")
            time.sleep(3)
            continue

        return menu

def imprimir_un_solo_paciente(datos):
    print("")
    print("PACIENTE: ")
    for clave, valor in datos.items():
        print("*",clave.upper(), ":", valor)
        if clave == "NACIMIENTO":
            edad = datetime.strptime(valor, '%d/%m/%Y')
            dia = edad.day
            mes = edad.month
            ano = edad.year
            actual = date.today()

            armar_fecha = date(ano, mes, dia)
            cumple = actual.year - armar_fecha.year
            print("* EDAD PACIENTE:", cumple)
    print("")

def imprimir_todos_los_pacientes(datos, indice):
    print("")
    print("PACIENTE: ")
    for clave, valor in datos[indice].items():
        print("*",clave.upper(), ":", valor)
        if clave == "NACIMIENTO":
            edad = datetime.strptime(valor, '%d/%m/%Y')
            dia = edad.day
            mes = edad.month
            ano = edad.year
            actual = date.today()

            armar_fecha = date(ano, mes, dia)
            cumple = actual.year - armar_fecha.year
            print("* EDAD PACIENTE:", cumple)
    print("")

def menu_edicion():
    while True:
        print("Seleccione el dato a cambiar")
        seleccion = input("""
                1 - Nombre
                2 - Apellido
                3 - DNI
                4 - Nacionalidad
                5 - Nacimiento
                """)
        control = seleccion.isdigit()
        if control == False:
            print("No se permiten letras")
            time.sleep(2)
            continue
        
        return seleccion

def editar_datos_pacientes(datos):
    corte = str
    while corte != "N":
        
        i = 0
        d = 1
        print()
        while i < len(datos):
            print("PACIENTES", d)
            for clave, valor in datos[i].items():
                print("*",clave.upper(), ":", valor)
            print()
            i = i + 1
            d = d + 1 
        
        try:
            editar = int(input("Seleccione un paciente por el N°: "))
        except ValueError:
            print("Solo se permiten numeros")
        
        if editar == 0:
            print("Ingreso un parametro no valido")
            time.sleep(2)
            break

        seleccion = menu_edicion()

        if seleccion == "1":

            editar = editar - 1
            nuevo_dato = datos[editar]
            nombre = input("NOMBRE: ").upper()

            for key, value in nuevo_dato.items():
                if key == "NOMBRE":
                    nuevo_dato[key] = nombre

        elif seleccion == "2":

            editar = editar - 1
            nuevo_dato = datos[editar]
            apellido = input("APELLIDO: ").upper()

            for key, value in nuevo_dato.items():
                if key == "APELLIDO":
                    nuevo_dato[key] = apellido

        elif seleccion == "3":

            editar = editar - 1
            nuevo_dato = datos[editar]
            dni = input("DNI: ").upper()

            for key, value in nuevo_dato.items():
                if key == "DNI":
                    nuevo_dato[key] = dni

        elif seleccion == "4":

            editar = editar - 1
            nuevo_dato = datos[editar]
            nacimiento = input("NACIMIENTO: ").upper()

            for key, value in nuevo_dato.items():
                if key == "NACIMIENTO":
                    nuevo_dato[key] = nacimiento

        i = 0
        d = 1
        print()
        while i < len(datos):
            print("PACIENTES", d)
            for clave, valor in datos[i].items():
                print("*",clave.upper(), ":", valor)
            print()
            i = i + 1
            d = d + 1 

        corte = input("¿Editar mas datos? S/N: ").upper()
        print("")
        if corte == "S":
            continue
    
    return datos

def imprimir_una_sola_histoia_clinica(datos):
    print("")
    print("HISTORIA CLINICA: ")
    for clave, valor in datos.items():
        print("*",clave.upper(), ":", valor)
    print("")

def imprimir_historia_clinica_con_paciente(union):
    
    clave = union["NACIMIENTO"]
    edad = datetime.strptime(clave, '%d/%m/%Y')
    dia = edad.day
    mes = edad.month
    ano = edad.year
    actual = date.today()

    armar_fecha = date(ano, mes, dia)
    cumple = actual.year - armar_fecha.year
    
    print("PACIENTE: ")
    print("* NOMBRE: ", union["NOMBRE"])
    print("* APELLIDO: ", union["APELLIDO"])
    print("* DNI: ", union["DNI"])
    print("* NACIONALIDAD: ", union["NACIONALIDAD"])
    print("* FECHA DE NACIMIENTO: ", union["NACIMIENTO"])
    print("* EDAD PACIENTE:", cumple)
    print()
    print("HISTORIA CLINICA")
    print("* FECHA ATENCION: ", union["FECHA"])
    print("* ENFERMEDAD: ", union["ENFERMEDAD"])
    print("* MEDICO: Dr.", union["MEDICO"])
    print("* OBSERVACIONES: ", union["OBSERVACIONES"])
    print("")

def ver_listado_profesionales(datos):

    while True:

        if datos:
            i = 0
            d = 1
            print()
            while i < len(datos):
                print("MEDICOS", d)
                for clave, valor in datos[i].items():
                    print("*",clave.upper(), ":", valor)
                print()
                i = i + 1
                d = d + 1 
            try:
                corte = int(input("Para salir presiones 0 "))
            except ValueError:
                print("No se permiten letras")
                continue
            if corte != 0:
                print("Solo se permite el cero")
                continue
            else:
                break
        else:
            print("No hay profesionales registrados")
            time.sleep(3)
            break

def seleccion_pacientes(datos):
    while True:

        i = 0
        d = 1
        print()
        while i < len(datos):
            print("PACIENTE", d)
            for clave, valor in datos[i].items():
                print("*",clave.upper(), ":", valor)
                if clave == "NACIMIENTO":
                    edad = datetime.strptime(valor, '%d/%m/%Y')
                    dia = edad.day
                    mes = edad.month
                    ano = edad.year
                    actual = date.today()

                    armar_fecha = date(ano, mes, dia)
                    cumple = actual.year - armar_fecha.year
                    print("* EDAD PACIENTE:", cumple)
            print()
            i = i + 1
            d = d + 1 
        try:
            paciente = int(input("Seleccione paciente a asignar historia clinica, segun su Numero: "))
        except ValueError:
            print("No se permiten letras. Vuelva a intentarlo")
            time.sleep(3)
            continue
        if paciente == 0:
            print("No se permite cero")
            time.sleep(3)
            continue
        paciente = paciente - 1
        try:
            primerDato = datos[paciente]
        except IndexError:
            print("No existe paciente ingresado con ese indice. Vuelva a intentarlo")
            time.sleep(3)
            continue

        return [primerDato, paciente]

def seleccion_historias_clincas(historia):
    while True:

        i = 0
        d = 1
        print()
        while i < len(historia):
            print("HISTORIAS CLINICAS", d)
            for clave, valor in historia[i].items():
                print("*",clave.upper(), ":", valor)
            print()
            i = i + 1
            d = d + 1 

        try:
            clinica = int(input("Seleccione historia clinica a asignar segun su numero: "))
        except ValueError:
            print("No se permiten letras. Vuelva a intentarlo")
            time.sleep(3)
            continue
        if clinica == 0:
            print("No se permite cero")
            time.sleep(3)
            continue
        clinica = clinica - 1
        try:
            segundoDato = historia[clinica]
        except IndexError:
            print("No existe historia clinica ingresada con ese indice. Vuelva a intentarlo")
            time.sleep(3)
            continue

        return [segundoDato, clinica]

def imprimir_un_solo_dato_profesional(datos):
    print("")
    print("MEDICO: ")
    for clave, valor in datos.items():
        print("*",clave.upper(), ":", valor)
    print("")