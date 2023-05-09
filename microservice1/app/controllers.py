from app import db
from flask import jsonify, request
from flask_restful import Resource

class Index(Resource):
    def get(self):
        return "Init microservice"

class UserList(Resource):
    #  en vue se llama con fetch() a /users .... 
    #  y retorna un json con los datos y 
    #  de ahi se visualiza en la web
    def get(self):
        try:
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM proyecto.usuario")
            rows = cursor.fetchall()
            print(rows)
            response = jsonify(rows)

        except Exception:
            response = jsonify(message='Failed to show usuarios.')
        
        finally:
            cursor.close()
            conn.close()
            return response
    
    #  en el Vue se llama con fetch() a /user? 
    #  con parametros del form mientras realiza el
    #  ejecucion en el backend y
    #  al final visualiza en la web la confirmacion
    def post(self):
        try:
            conn = db.connect()
            cursor = conn.cursor()
            
            new = request.get_json()
            nombre = new['nombre']
            telefono = new['telefono']
            direccion = new['direccion']
            nombre_usuario = new['nombre_usuario']
            email = new['email']
            contrasenha = new['contrasenha']

            query = """INSERT INTO proyecto.usuario(name, phone, address, username, email, password) 
                       VALUES(%s, %s, %s, %s, %s, %s)"""
            
            cursor.execute(query, (nombre, telefono, direccion, nombre_usuario, email, contrasenha))
            conn.commit()

            response = jsonify(message='Usuario added successfully.', id=cursor.lastrowid)
            response.status_code = 200

        except Exception:
            response = jsonify(message='Failed to add usuario.')
            response.status_code = 400

        finally:
            cursor.close()
            conn.close()
            return response
            

class User(Resource):
    def get(self, username_):
        try:
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM proyecto.usuario WHERE username = %s', username_)
            rows = cursor.fetchall()
            return jsonify(rows)

        except Exception:
            response = jsonify(message='Failed to get usuario.')
        
        finally:
            cursor.close()
            conn.close()
            return response

    def put(self, username_):
        try:
            conn = db.connect()
            cursor = conn.cursor()

            new = request.get_json()
            telefono = new['telefono']
            direccion = new['direccion']
            email = new['email']
            contrasenha = new['contrasenha']

            query = """UPDATE proyecto.usuario 
                    SET phone=%s, address=%s, username=%s, email=%s, password=%s"""
            
            cursor.execute(query, (telefono, direccion, username_, email, contrasenha))
            conn.commit()

            response = jsonify('Usuario updated successfully.')
            response.status_code = 200

        except Exception:
            response = jsonify('Failed to update usuario.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)

    def delete(self, username_):
        try:
            conn = db.connect()
            cursor = conn.cursor()

            cursor.execute('DELETE FROM proyecto.usuario WHERE username = %s', username_)
            conn.commit()
            response = jsonify('Usuario deleted successfully.')
            response.status_code = 200

        except Exception:
            response = jsonify('Failed to delete usuario.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)
