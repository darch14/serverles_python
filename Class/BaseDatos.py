import pymysql
# import sshtunnel


class BaseDatos:
        
    def usuariosBuscar(sql, correo, password):
        try:
            # tunnel = sshtunnel.SSHTunnelForwarder(
            #     ('192.168.211.136', 22), 
            #     ssh_password= "finsocial123", 
            #     ssh_username= "root",
            #     remote_bind_address=("localhost", 3306)
            # )
            # tunnel.start()

            connection = pymysql.connect(
                host= '127.0.0.1',
                user= 'root',
                password= '',
                db= 'serverless',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            with connection:
                with connection.cursor() as cur:
                    # cur = connection.cursor()
                    cur.execute(sql, (correo, password))
                    myreturn = cur.fetchone()
                    
                    return myreturn
        
        except Exception as e:
            # print(f'ERROR: {e}')
            return str(e)
        