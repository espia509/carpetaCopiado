import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil

# Carpeta de origen
carpeta_origen = 'Dirección_Carpeta'

# Carpeta de destino
carpeta_destino = 'Dirección_Carpeta'


class Event(FileSystemEventHandler):
    def on_created(self, event):
        # Comprueba si se ha creado o añadidio un archivo
        if not event.is_directory:
            ruta_archivo = event.src_path
            shutil.copy2(ruta_archivo, carpeta_destino)
            print(f"Se ha copiado el archivo {ruta_archivo} a la carpeta de destino.")

# Crear un observador
observador = Observer()
observador.schedule(Event(), carpeta_origen, recursive=False)
observador.start()

try:
    # Mantener el programa en ejecución
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observador.stop()


observador.join()