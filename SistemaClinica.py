"""Desarrolle un programa en Python que simule una cola de atención en una clínica. El sistema
debe permitir agregar pacientes a la cola (registro de llegada), atender al siguiente paciente
(eliminar el primero en la cola) y mostrar en pantalla la lista actual de pacientes en espera. El
docente implementará el programa paso a paso, explicando cada parte del código, mientras los
estudiantes proponen mejoras, prueban con distintos datos y analizan el comportamiento de la
estructura tipo cola."""

# Modulo que contiene la logica de la estructura de cola y la clase Paciente

class Paciente:
    """
    Representa a un paciente de la clinica.
    """
    def __init__(self, nombre):
        self.nombre = nombre  # Guarda el nombre del paciente

    def __str__(self):
        return self.nombre  # Permite imprimir el paciente directamente


class ColaClinica:
    """
    Estructura de datos tipo cola para simular la atencion por orden de llegada.
    """
    def __init__(self):
        self.cola = []  # Lista que almacena los pacientes

    def is_empty(self):
        """
        Verifica si la cola esta vacia.
        """
        return len(self.cola) == 0

    def enqueue(self, nombre):
        """
        Agrega un nuevo paciente al final de la cola (registro de llegada).
        """
        paciente = Paciente(nombre)
        self.cola.append(paciente)
        print(f"-> Paciente '{nombre}' registrado correctamente.")

    def dequeue(self):
        """
        Atiende (elimina) al primer paciente en la cola.
        """
        if not self.is_empty():
            paciente = self.cola.pop(0)
            print(f"-> Atendiendo a {paciente}")
        else:
            print("-> No hay pacientes en espera.")

    def peek(self):
        """
        Muestra el paciente que esta al frente de la cola, sin eliminarlo.
        """
        if not self.is_empty():
            print(f"-> Proximo paciente: {self.cola[0]}")
        else:
            print("-> No hay pacientes en la cola.")

    def mostrar_pacientes(self):
        """
        Lista los pacientes en espera en orden de llegada.
        """
        if self.is_empty():
            print("-> No hay pacientes en espera.")
        else:
            print("Pacientes en espera:")
            for i, paciente in enumerate(self.cola, start=1):
                print(f"  {i}. {paciente}")
