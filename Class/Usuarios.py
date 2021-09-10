from Class.BaseDatos import BaseDatos
import json

class Usuarios(BaseDatos):
    
    def login(correo, password):
        sql = "SELECT * FROM usuarios WHERE correo = %s AND `password` = %s AND estado = 1;";
        print(sql);
        try:
            usuarios = BaseDatos.usuariosBuscar(sql, correo, password)
            return {
                "state": True,
                "data": ""
            }
            
        except Exception as e:
            print(f'ERROR: {e}')
            # v = "Error:23 {e}";
            return {
                "state": False,
                "message": "error"
            }