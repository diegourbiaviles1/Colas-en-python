"""Desarrolle un programa en Python que simule una cola de atención en una clínica. El sistema
debe permitir agregar pacientes a la cola (registro de llegada), atender al siguiente paciente
(eliminar el primero en la cola) y mostrar en pantalla la lista actual de pacientes en espera. El
docente implementará el programa paso a paso, explicando cada parte del código, mientras los
estudiantes proponen mejoras, prueban con distintos datos y analizan el comportamiento de la
estructura tipo cola."""

# Programa principal que utiliza el modulo sistema_clinica.py

from SistemaClinica import ColaClinica

# Funcion que muestra las opciones del menu
def mostrar_menu():
    print("""
=== Clinica: Sistema de Atencion ===
1. Registrar llegada de paciente
2. Atender siguiente paciente
3. Ver proximo paciente (peek)
4. Mostrar pacientes en espera
5. Verificar si la cola esta vacia
6. Salir
""")

# Funcion principal que controla el flujo del programa
def main():
    cola = ColaClinica()  # Creamos una nueva cola vacia

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion (1-6): ").strip()

        # Registrar paciente
        if opcion == "1":
            nombre = input("Nombre del paciente: ").strip()
            if nombre:
                cola.enqueue(nombre)
            else:
                print("-> Nombre invalido.")

        # Atender siguiente paciente
        elif opcion == "2":
            cola.dequeue()

        # Ver el proximo paciente en ser atendido
        elif opcion == "3":
            cola.peek()

        # Mostrar todos los pacientes en espera
        elif opcion == "4":
            cola.mostrar_pacientes()

        # Verificar si la cola esta vacia
        elif opcion == "5":
            if cola.is_empty():
                print("-> La cola esta vacia.")
            else:
                print("-> Hay pacientes en espera.")

        # Salir del programa
        elif opcion == "6":
            print("Saliendo del sistema. Hasta luego.")
            break

        # Opcion invalida
        else:
            print("Opcion no valida. Intenta de nuevo.")

        # Separador entre iteraciones
        print("-" * 40)

# Punto de entrada del programa
if __name__ == "__main__":
    main()
