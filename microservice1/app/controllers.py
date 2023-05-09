from app import db
from flask import jsonify, request
from flask_restful import Resource

class Index(Resource):
    def get(self):
        return "Init microservice"


class UserList(Resource):
    def get(self):
        try:
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM proyecto.usuario")
            rows = cursor.fetchall()
            response = jsonify(rows)

        except Exception:
            response = jsonify(message='Failed to show usuarios.')
        
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
                    SET username=%s, phone=%s, address=%s, email=%s, password=%s"""
            
            cursor.execute(query, (username_, telefono, direccion, email, contrasenha))
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

class Register(Resource):
    def post(self):
        try:
            conn = db.connect()
            cursor = conn.cursor()
            
            new = request.get_json()
            nombre_usuario = new['nombre_usuario']
            nombre = new['nombre']
            telefono = new['telefono']
            direccion = new['direccion']
            email = new['email']
            contrasenha = new['contrasenha']

            query = """INSERT INTO proyecto.usuario(username, name, phone, address, email, password) 
                       VALUES(%s, %s, %s, %s, %s, %s)"""
            
            cursor.execute(query, (nombre_usuario, nombre, telefono, direccion, email, contrasenha))
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
        
class Login(Resource):
    def post(self):
        try:
            conn = db.connect()
            cursor = conn.cursor()
            
            usuario_v = request.get_json()
            l_usuario = usuario_v['nombre_usuario']
            l_contrasenha = usuario_v['contrasenha']
            
            query = """SELECT * FROM proyecto.usuario WHERE username=%s AND password=%s"""

            cursor.execute(query, (l_usuario, l_contrasenha))
            
            if (cursor.fetchall()):
                response = jsonify({"nombre_usuario":l_usuario, "contrasenha": l_contrasenha})
            else:
                response = jsonify(message='Usuario does not exist')
        
        except Exception:
            response = jsonify(message='Failed to add usuario.')
            response.status_code = 400

        finally:
            cursor.close()
            conn.close()
            return response