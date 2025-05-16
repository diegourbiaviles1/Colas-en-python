class Proceso:
    """
    Representa un proceso para el microprocesador.
    Cada proceso tiene un identificador, un nombre y una duración en milisegundos.
    """
    def __init__(self, pid: str, nombre: str, duracion_ms: int):
        # Cada atributo identifica las propiedades principales del proceso
        self.pid = pid               # Identificador único del proceso
        self.nombre = nombre         # Nombre descriptivo del proceso
        self.duracion_ms = duracion_ms  # Tiempo estimado de ejecución en milisegundos

    def __str__(self):
        # Formato legible para mostrar el proceso
        return f"[ID={self.pid} | {self.nombre} | {self.duracion_ms} ms]"