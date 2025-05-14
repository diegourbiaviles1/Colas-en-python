class Proceso:
    """
    Representa un proceso para el microprocesador.
    Cada proceso tiene un identificador, un nombre y una duración en milisegundos.
    """
    def __init__(self, pid: str, nombre: str, duracion_ms: int):
        self.pid = pid
        self.nombre = nombre
        self.duracion_ms = duracion_ms

    def __str__(self):
        return f"[PID={self.pid} | {self.nombre} | {self.duracion_ms} ms]"


def mostrar_menu():
    print("""
=== Simulación: CPU FIFO ===
1. Registrar nuevo proceso
2. Ejecutar siguiente proceso
3. Ver proceso en ejecución
4. Mostrar procesos pendientes
5. Salir
""")


def registrar_proceso(cola):
    pid = input("ID del proceso: ").strip()
    nombre = input("Nombre del proceso: ").strip()
    try:
        dur = int(input("Duración estimada (ms): ").strip())
    except ValueError:
        print("→ Duración inválida. Debe ser un número entero.")
        return
    p = Proceso(pid, nombre, dur)
    cola.append(p)
    print(f"→ Proceso registrado: {p}")


def ejecutar_siguiente(cola, estado):
    """
    Desencola el siguiente proceso y lo marca como en ejecución.
    """
    if cola:
        p = cola.pop(0)
        estado['actual'] = p
        print(f"→ Ejecutando: {p}")
    else:
        print("→ No hay procesos en la cola.")


def ver_en_ejecucion(estado):
    """
    Muestra el proceso que está actualmente en ejecución.
    """
    if estado.get('actual'):
        print(f"Proceso en ejecución: {estado['actual']}")
    else:
        print("→ Aún no se ha ejecutado ningún proceso.")


def mostrar_pendientes(cola):
    """
    Lista los procesos que están esperando en la cola.
    """
    if cola:
        print("Procesos pendientes:")
        for i, p in enumerate(cola, start=1):
            print(f"  {i}. {p}")
    else:
        print("→ No hay procesos pendientes.")


def main():
    cola = []                    # Cola de procesos pendientes
    estado = {'actual': None}    # Guarda el proceso en ejecución

    while True:
        mostrar_menu()
        opcion = input("Seleccione (1-5): ").strip()

        if opcion == "1":
            registrar_proceso(cola)
        elif opcion == "2":
            ejecutar_siguiente(cola, estado)
        elif opcion == "3":
            ver_en_ejecucion(estado)
        elif opcion == "4":
            mostrar_pendientes(cola)
        elif opcion == "5":
            print("→ Saliendo de la simulación. ¡Hasta luego!")
            break
        else:
            print("→ Opción inválida. Intente de nuevo.")

        print("-" * 40)


if __name__ == "__main__":
    main()
