
from procesos import Proceso, registrar_proceso, ejecutar_siguiente, ver_en_ejecucion, mostrar_pendientes
from clasproceso import Proceso


def mostrar_menu():
    # Despliega las opciones disponibles para la simulación CPU FIFO
    print("""
=== Simulacion: CPU FIFO ===
1. Registrar nuevo proceso
2. Ejecutar siguiente proceso
3. Ver proceso en ejecución
4. Mostrar procesos pendientes
5. Salir
""")
    
def main():
    # Inicializacion de la cola y el estado de ejecución
    cola = []                  # Lista FIFO para procesos pendientes
    estado = {'actual': None}  # Diccionario que guarda el proceso en ejecucion

    # Bucle principal que mantiene la simulación activa
    while True:
        mostrar_menu()  # Mostramos opciones al usuario
        opcion = input("Seleccione (1-5): ").strip()

        # Dirigimos la acción según la opción seleccionada
        if opcion == "1":
            registrar_proceso(cola)
        elif opcion == "2":
            ejecutar_siguiente(cola, estado)
        elif opcion == "3":
            ver_en_ejecucion(estado)
        elif opcion == "4":
            mostrar_pendientes(cola)
        elif opcion == "5":
            # Finalizamos la simulación
            print("Saliendo de la simulación. ¡Hasta luego!")
            break
        else:
            # Mensaje para opciones fuera de rango
            print("Opción inválida. Intente de nuevo.")

        # Línea separadora para claridad entre iteraciones
        print("-" * 40)


# Punto de entrada principal: ejecuta main() cuando el script se corre directamente
if __name__ == "__main__":
    main()