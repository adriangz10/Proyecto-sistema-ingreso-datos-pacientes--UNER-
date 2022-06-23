from funciones import menu_principal, imprimir_titulo
from area_pacientes import inicio_area_pacientes
from area_historia_clinica import inicio_area_historia_clinica
from area_profesionaless import inicio_area_profesionales
import time

while True:

    imprimir_titulo("Instituto Medico las Lurcienegas")

    seleccion = menu_principal()

    if seleccion == 1:

        inicio_area_pacientes()

    elif seleccion == 2:

        inicio_area_historia_clinica()

    elif seleccion == 3:

        inicio_area_profesionales()

    elif seleccion == 0:
        print("Finalizando programa...")
        time.sleep(3)
        exit()