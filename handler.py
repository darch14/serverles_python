import json
import re
from Class.Usuarios import Usuarios

def hello(event, context):
    # variables = event['body'] 
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def validar_numero(event, context):

    try:
        variables = event['numero_prueba']
        # variables = "123"
        matched = re.match('[0-9]', variables)
        is_match = bool(matched)

        if is_match:
            body = {
                "status": 1,
                "message": "Validacion Correcta de variale " + variables
            }
        else:
            body = {
                "status": 0,
                "message": "Validacion Incorrecta variale " + variables
            }
        
        return {
            "statusCode": 200,
            "body": json.dumps(body)
        }
        
    except AssertionError as error:
        body = {
            "status": 0,
            "message": "Ops A Ocurrido Un Error" + error
        }
        return {
            "statusCode": 500,
            "body": json.dumps(body)
        }
        
def login(event, context):
    body = json.loads(event['body'])
    usuario = body['usuario']
    contrasena = body['password']
    try:
        classUsuarios = Usuarios.login(usuario, contrasena)
        print(classUsuarios)
        if classUsuarios['state']:
            return {
                "statusCode": 200,
                "body": json.dumps(classUsuarios)
            }
        else:
            return {
                "statusCode": 400,
                "body": json.dumps(classUsuarios)
            }
    except AssertionError as error:
        body = {
            "status": 0,
            "message": "Ops A Ocurrido Un Error" + error
        }
        return {
            "statusCode": 500,
            "body": json.dumps(body)
        }
# Proporciona el alto:
# Proporciona el ancho:
# Area: <area>
# Perímetro:
