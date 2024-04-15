class Error(Exception):
    pass

class LargoExcedidoException(Exception):
    def __init__(self, mensaje="El nuevo nombre excede los 250 caracteres."):
        super().__init__(mensaje)

class SubTipoInvalidoException(Exception):
    def __init__(self, mensaje="El nuevo subtipo no es válido para este tipo de anuncio."):
        super().__init__(mensaje)
