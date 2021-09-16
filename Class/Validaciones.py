import re

class Validacion:

    def __init__(self, array_datos):
        self.array_datos = array_datos

    def soloLetras(seft, campo, valor):
        if valor.isalpha():
            return {
                "state": 200,
                "message": f"El {campo} es de solo letras"
            }
        else:
            return {
                "state": 500,
                "message": f"El {campo} debe ser solo letras"
            }

    def letrasEspacios(self, campo, valor):
        patron_texto = "/^[a-zA-ZáéíóúÁÉÍÓÚäëïöüÄËÏÖÜàèìòùÀÈÌÒÙ\s]+$/";
        matched = re.match(patron_texto, valor)
        is_match = bool(matched)
        if is_match:
            return {
                "state": 200,
                "message": f"El {campo} tiene solo letras y espacios"
            }
        else:
            return {
                "state": 500,
                "message": f"El {campo} debe ser solo letras y espacios"
            }
    
    def numeroEntero(self, campo, valor):
        if valor.isdigit():
            return {
                "state": 200,
                "message": f"El {campo} es un entero"
            }
        else:
            return {
                "state": 500,
                "message": f"El {campo} debe ser un entero"
            }

    def cadena(self, campo, valor):
        val = valor.replace(" ", "")
        if val.isalpha():
            return {
                "state": 200,
                "message": f"El {campo} es una cadena"
            }
        else:
            return {
                "state": 500,
                "message": f"El {campo} debe ser una cadena"
            }

    def correo(self, campo, valor):
        patron_texto = "/^[A-z0-9ñÑ\\._-]+@[A-z0-9][A-z0-9-]*(\\.[A-z0-9_-]+)*\\.([A-z]{2,6})$/";
        matched = re.match(patron_texto, valor)
        is_match = bool(matched)
        if is_match:
            return {
                "state": 200,
                "message": f"El {campo} es un correo"
            }
        else:
            return {
                "state": 500,
                "message": f"El {campo} debe ser un correo"
            }
    
    def decimales(self, campo, valor):
        patron_texto = "/^\d*\.?\d*$/";
        matched = re.match(patron_texto, valor)
        is_match = bool(matched)
        if is_match:
            return {
                "state": 200,
                "message": f"El {campo} es un decimal"
            }
        else:
            return {
                "state": 500,
                "message": f"El {campo} debe ser un decimal"
            }

    def contra(self, campo, valor):
        valid = True
        if len(valor) >= 8 and len(valor) <= 16:
            valid = False
        elif re.search('[0-9]',valor) is None:
            valid = False
        elif re.search('[A-Z]',valor) is None: 
            valid = False
        elif re.search('[a-z]',valor) is None: 
            valid = False
        if valid:
            return {
                "state": 200,
                "message": f"El {campo} es una contraseña valida"
            }
        else:
            return {
                "state": 500,
                "message": f"El {campo} tener entre 8 a 16 caracteres, contener mayuzcula, minuscula y numero"
            }

    def validUno(self):
        array_datos = self.array_datos
        operador = array_datos['operador']
        campo = array_datos['campo']
        valor = array_datos['valor']
        swithch_valid = {
            1: self.soloLetras(campo, valor),
            2: self.letrasEspacios(campo, valor),
            3: self.numeroEntero(campo, valor),
            4: self.cadena(campo, valor),
            5: self.correo(campo, valor),
            5: self.decimales(campo, valor),
            6: self.contra(campo, valor)
        }

        error = {
            "status": 500,
            "message": "Ocurrio un error"
        }
        return swithch_valid.get(operador, error)


