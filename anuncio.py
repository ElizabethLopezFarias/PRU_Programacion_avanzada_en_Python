from abc import ABC, abstractmethod
from campanna import Campanna
from error import SubTipoInvalidoException


class Anuncio(ABC):
    #métodos
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo:str):
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @abstractmethod
    def comprimir_anuncio(self):
        pass
    
    @abstractmethod
    def redimensionar_anuncio(self):
        pass

    @abstractmethod
    def modificar_subtipo(self, nuevo_subtipo):
        pass



    #metodo estático para mostrar los formatos y subtimos de las clases hijas
    @staticmethod
    def mostrar_formatos():
        print("Formatos disponibles para crear anuncios:")
        for cls in Anuncio.__subclasses__():
            print(f"{cls.FORMATO}:")
            print("=" * len(cls.FORMATO))
            for subtipo in cls.SUBTIPOS:
                print("-", subtipo)
            print()

     #Getter y Setter
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1

    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo

    @property
    def url_clic(self):
        return self.__url_clic
    
    @url_clic.setter
    def url_archivo(self, url_clic):
        self.__url_clic = url_clic

    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        self.__sub_tipo = sub_tipo
# Fin Clase Anuncio ----

# Clase hija Video ------
class Video(Anuncio):
    FORMATO = "Video"
    SUBTIPOS = ("instream", "outstream")

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self):
        pass

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self):
        pass    

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo:str, duracion: int):
        super().__init__(1, 1,url_archivo, url_clic, sub_tipo)
        self.__duracion = duracion if duracion >0 else 5

    def modificar_subtipo(self, nuevo_subtipo):
        if nuevo_subtipo not in self.SUBTIPOS:
            raise SubTipoInvalidoException("El nuevo subtipo no es válido para este tipo de anuncio.")
        self.__sub_tipo = nuevo_subtipo



    def comprimir_anuncio(self):
         print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
         print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")



# Fin Clase hija Video ------

# Clase hija Display ------
class Display(Anuncio):
    FORMATO = "Display"
    SUBTIPOS = ("tradicional", "native")
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

# Fin Clase hija Display ------

# Clase hija Social ------
class Social(Anuncio):
    FORMATO = "Social"
    SUBTIPOS = ("facebook", "linkedin")
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)    

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
