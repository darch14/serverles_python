from Class.BaseDatos import BaseDatos
import json

class Usuarios(BaseDatos):
    
    def login(correo, password):
        sql = "SELECT id, usuario, correo FROM usuarios WHERE usuario = %s AND `contra` = %s AND estado = 1;";
        try:
            usuarios = BaseDatos.usuariosBuscar(sql, correo, password)
            if bool(usuarios):
                return {
                    "state": True,
                    "data": usuarios
                }
            else:
                return {
                    "state": False,
                    "message": "Verificar los datos"
                } 
        except Exception as e:
            # print(f'ERROR: {e}')
            # v = "Error:23 {e}";
            return {
                "state": False,
                "message": str(e)
            }