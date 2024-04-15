from datetime import datetime
from error import LargoExcedidoException


class Campanna:
    def __init__(self, nombre: str, fecha_inicio: datetime, fecha_termino: datetime, anuncios: list):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = anuncios  # Lista para almacenar los anuncios


    def __str__(self):
        cant_video = 0
        cant_display = 0
        cant_social = 0

        for elemento in self.__anuncios:
            if isinstance(elemento, Video):
                cant_video +=1
            elif isinstance(elemento, Display):
                cant_display +=1
            elif isinstance(elemento, Social):
                cant_social +=1

        return f"""
        Nombre de la campaña: {self.__nombre}
        Anuncios: 
        Video: {cant_video}, Display: {cant_display}, Social: {cant_social}
        """

    def modificar_nombre(self, nuevo_nombre):
        if len(nuevo_nombre) <= 250:
            self.__nombre = nuevo_nombre
        else:
            raise LargoExcedidoException("El nuevo nombre excede los 250 caracteres.")

    # Getter para el atributo anuncios
    @property
    def anuncios(self):
        return self.__anuncios

    # Setter para el atributo fecha_inicio
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha_inicio):
        self.__fecha_inicio = nueva_fecha_inicio

    # Setter para el atributo fecha_termino
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self, nueva_fecha_termino):
        self.__fecha_termino = nueva_fecha_termino