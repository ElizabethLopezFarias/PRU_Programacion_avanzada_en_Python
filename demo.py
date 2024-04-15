from datetime import datetime
from campanna import Campanna, LargoExcedidoException
from anuncio import Video, SubTipoInvalidoException
from error import LargoExcedidoException, SubTipoInvalidoException


# Crear una instancia de Campanna con un anuncio de tipo Video
fecha_inicio = datetime(2024, 4, 1)
fecha_termino = datetime(2024, 4, 15)
anuncio_video = Video(1920, 1080, "video.mp4", "url_clic", "instream", 30)
campanna = Campanna("Campaña de prueba", fecha_inicio, fecha_termino, [anuncio_video])

try:
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
    campanna.modificar_nombre(nuevo_nombre)
except LargoExcedidoException as e:
    with open("error.log", "a") as file:
        file.write(f"{str(e)}\n")

try:
    nuevo_sub_tipo = input("Ingrese el nuevo sub_tipo para el anuncio: ")
    anuncio_video.modificar_subtipo(nuevo_sub_tipo)
except SubTipoInvalidoException as e:
    with open("error.log", "a") as file:
        file.write(f"{str(e)}\n")

try:
    with open("error.log", "r") as file:
        contenido = file.read()
        if contenido:
            print("Errores encontrados:")
            print(contenido)
except FileNotFoundError:
    print("No se encontraron errores en el archivo de registro.")