def mostrar_menu():
    """
    Muestra las opciones disponibles al usuario.
    """
    # Imprime el menú principal con las opciones del sistema de atención de la clínica
    print("""
=== Clínica: Sistema de Atención ===
1. Registrar llegada de paciente
2. Atender siguiente paciente
3. Mostrar pacientes en espera
4. Salir
""")


def registrar_llegada(cola):
    """
    Pide al usuario el nombre del paciente y lo añade al final de la cola.
    """
    # Solicitamos el nombre y eliminamos espacios en blanco al inicio y fin
    nombre = input("Nombre del paciente: ").strip()
    # Verificamos que el usuario haya ingresado un nombre válido
    if nombre:
        cola.append(nombre)  # Añadimos al final de la lista (FIFO)
        print(f"Paciente '{nombre}' registrado correctamente.")
    else:
        # Informamos al usuario en caso de entrada inválida
        print("¡Nombre inválido!")


def atender_siguiente(cola):
    """
    Si la cola no está vacía, atiende (desencola) al primer paciente.
    """
    if cola:
        # pop(0) quita y devuelve el primer elemento de la lista
        paciente = cola.pop(0)
        print(f"Atendiendo a {paciente}.")
    else:
        # No hay pacientes en espera
        print(" No hay pacientes en espera.")


def mostrar_pacientes(cola):
    """
    Muestra la lista actual de pacientes en espera.
    """
    if cola:
        print("Pacientes en espera:")
        # Recorremos la cola y mostramos cada paciente con su posición
        for idx, nombre in enumerate(cola, start=1):
            print(f"  {idx}. {nombre}")
    else:
        # Indicamos que la cola está vacía
        print(" No hay pacientes en la cola.")


def main():
    # Cola inicial con algunos pacientes de ejemplo
    cola = ["María", "José", "Juan", "Pedro", "Ana"]
    # Mostramos el estado inicial de la cola antes de iniciar el bucle
    print("Cola inicial:", cola)

    # Bucle principal: se ejecuta hasta que el usuario elija salir
    while True:
        mostrar_menu()  # Desplegamos el menú de opciones
        opcion = input("Selecciona una opción (1-4): ").strip()

        # Lógica de control según la opción ingresada
        if opcion == "1":
            registrar_llegada(cola)
        elif opcion == "2":
            atender_siguiente(cola)
        elif opcion == "3":
            mostrar_pacientes(cola)
        elif opcion == "4":
            # Salimos del programa de manera limpia
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            # La entrada no corresponde a ninguna opción válida
            print("Opción no válida. Intenta de nuevo.")

        # Separa visualmente cada iteración para mayor claridad
        print("-" * 40)


# Punto de entrada principal: ejecuta main() solo si este archivo es ejecutado directamente
if __name__ == "__main__":
    main()
