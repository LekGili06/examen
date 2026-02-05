import random 


lista_trabajadores= ["Juan Perez","Maria Garcia","Carlos Lopez",
               "Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez",
               "Isabel Gomez","Francisco Diaz","Elena Fernandez"]
lista_sueldos= []

def Asignar_sueldos():
    global lista_trabajadores
    global lista_sueldos
    for i in range(len(lista_trabajadores)):
        sueldo = random.randint(300000,2500000)
        lista_sueldos.append(sueldo)
        print("\nSueldos asignados correctamente")
   
def Clasificar_sueldos():

    cantidad_menor=0
    cantidad_medio=0
    cantidad_mayor=0
    totales=0
    for i in range(len(lista_sueldos)):

        if lista_sueldos[i] < 800000:
            cantidad_menor=cantidad_menor+1
        elif lista_sueldos[i] >=800000 and lista_sueldos[i] <= 2000000:
            cantidad_medio=cantidad_medio+1
        else cantidad_mayor[i] >2500000:
            cantidad_mayor=cantidad_mayor+1

        totales=totales+lista_sueldos[i]

    print("\nSueldos menores a $800.000 Total:(len{menores})")
    print(f"{'nombre trabajador':<20}{'sueldo trabajador':>10}")
for n, s in lista_sueldos:
    print(f"{n:<20} ${s:>10}")
print("\nSueldos medios a $2.000.000 Total:(len{medios})")
print(f"{'nombre trabajador':<20}{'sueldo trabajador':>10}")
for n, s in lista_sueldos:
        print(f"{n:<20} ${s:>10}")       
print("\nSueldos maximos a $2.500.000 Total:(len{maximos})")
print(f"{'nombre trabajador':<20}{'sueldo trabajador':>10}")
for n, s in lista_sueldos:
        print(f"{n:<20} ${s:>10}")




def Estadisticas():
     if not lista_sueldos:
          print("\nError! No hay lista de sueldos")
          return

     


def Reporte_sueldos():     




def Salir(): 
    print("\nFinalizando programa....")
    print("Desarrollado por Kel Flores.")
    print("RUT 17.786.728-8")  
    break   


while True:
    print("----Bienvenido a RRHH----")
    print("1)Asignar sueldos aleatorios")
    print("2)Clasificar sueldos")
    print("3)Ver estadisticas")
    print("4)Reporte de sueldos")
    print("5)Salir del programa")

    opcion= input("Ingresa una opcion: ")

    match opcion:
        case 1:
            Asignar_sueldos()
        case 2:
            Clasificar_sueldos()
        case 3:
            Estadisticas()
        case 4:
            Reporte_sueldos()
        case 5:
            Salir()
            print("\nFinalizando programa....")
            print("Desarrollado por Kel Flores.")
            print("RUT 17.786.728-8")  
            break
        case _:
            print("Error!!!!,Ingresa una opcion valida")              

