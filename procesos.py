from clasproceso import Proceso

def registrar_proceso(cola):
    """
    Solicita datos del proceso al usuario y lo añade al final de la cola.
    """
    # Solicitamos al usuario el identificador y nombre
    pid = input("ID del proceso: ").strip()
    nombre = input("Nombre del proceso: ").strip()
    try:
        # Convertimos la duración ingresada a entero
        dur = int(input("Duración estimada (ms): ").strip())
    except ValueError:
        # En caso de entrada no numérica, informamos y salimos
        print("Duración inválida. Debe ser un número entero.")
        return
    # Creamos instancia de Proceso y la añadimos a la cola FIFO
    p = Proceso(pid, nombre, dur)
    cola.append(p)
    print(f"Proceso registrado: {p}")


def ejecutar_siguiente(cola, estado):
    """
    Desencola el siguiente proceso y lo marca como el que está en ejecución.
    """
    if cola:
        # Removemos el primer proceso y lo guardamos en el estado actual
        p = cola.pop(0)
        estado['actual'] = p
        print(f"Ejecutando: {p}")
    else:
        # Si no hay procesos pendientes
        print("No hay procesos en la cola.")


def ver_en_ejecucion(estado):
    """
    Muestra el proceso que está actualmente en ejecución.
    """
    if estado.get('actual'):
        print(f"Proceso en ejecución: {estado['actual']}")
    else:
        # Aún no se ha ejecutado ningún proceso desde el inicio
        print("Aún no se ha ejecutado ningún proceso.")


def mostrar_pendientes(cola):
    """
    Lista los procesos que están esperando en la cola.
    """
    if cola:
        print("Procesos pendientes:")
        # Enumeramos para mostrar posición y datos
        for i, p in enumerate(cola, start=1):
            print(f"  {i}. {p}")
    else:
        # No quedan procesos en espera
        print("No hay procesos pendientes.")