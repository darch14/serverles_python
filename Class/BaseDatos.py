import pymysql

class BaseDatos:
        
    def usuariosBuscar(sql, correo, password):
        try:
            connection = pymysql.connect(
                host= '192.168.211.136',
                user= 'root',
                password= 'Finsocial123#',
                db= 'serverless'
            )
            
            cur = connection.cursor()
            cur.execute(sql, (correo, password))
            myreturn = cur.fetchall()
            
            return myreturn
        
        except Exception as e:
            print(f'ERROR: {e}')
            return "Error: "
        