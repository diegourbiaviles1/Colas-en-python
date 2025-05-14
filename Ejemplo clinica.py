def mostrar_menu():
    """
    Muestra las opciones disponibles al usuario.
    """
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
    nombre = input("Nombre del paciente: ").strip()
    if nombre:
        cola.append(nombre)
        print(f"→ Paciente '{nombre}' registrado correctamente.")
    else:
        print("¡Nombre inválido!")


def atender_siguiente(cola):
    """
    Si la cola no está vacía, atiende (desencola) al primer paciente.
    """
    if cola:
        paciente = cola.pop(0)
        print(f"→ Atendiendo a {paciente}.")
    else:
        print("→ No hay pacientes en espera.")


def mostrar_pacientes(cola):
    """
    Muestra la lista actual de pacientes en espera.
    """
    if cola:
        print("Pacientes en espera:")
        for idx, nombre in enumerate(cola, start=1):
            print(f"  {idx}. {nombre}")
    else:
        print("→ No hay pacientes en la cola.")


def main():
    # Cola inicial con algunos pacientes
    cola = ["María", "José", "Juan", "Pedro", "Ana"]
    print("Cola inicial:", cola)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            registrar_llegada(cola)
        elif opcion == "2":
            atender_siguiente(cola)
        elif opcion == "3":
            mostrar_pacientes(cola)
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

        # Para separar iteraciones
        print("-" * 40)


if __name__ == "__main__":
    main()
