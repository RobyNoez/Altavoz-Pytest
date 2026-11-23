
class Altavoz:
    def __init__(self, nombre, volumen):
        self.nombre = nombre  # nombre y volumen son propiedades, no atributos (mío)
        self.volumen = volumen
        self._encendido = False  # atributo interno (mío)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena texto")

        nombre = nombre.strip()

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío o contener solo espacios en blanco")

        self._nombre = nombre

    @property
    def volumen(self):
        return self._volumen

    @volumen.setter
    def volumen(self, volumen):
        if type(volumen) is not int:
            raise ValueError("El volumen debe ser un valor entero")

        if volumen < 0 or volumen > 100:
            raise ValueError("El volumen debe estar entre el 0 y 100")

        self._volumen = volumen

    @property
    def estado(self):
        if self._encendido:
            return "encendido"
        else:
            return "apagado"

    def encender(self):
        self._encendido = True

    def apagar(self):
        self._encendido = False
