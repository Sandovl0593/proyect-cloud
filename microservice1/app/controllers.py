from app import app, db
from flask import jsonify, request
from flask_restful import Resource


class UserList(Resource):
    #  en vue se llama con fetch() a /users .... 
    #  y retorna un json con los datos y 
    #  de ahi se visualiza en la web
    def get(self):
        try:
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario")
            rows = cursor.fetchall()
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
            
            response = request.get_json()
            nombre = response['nombre']
            telefono = response['telefono']
            direccion = response['direccion']
            usuario = response['usuario']
            email = response['email']
            contrasenha = response['contrasenha']

            query = """INSERT INTO usuario(nombre, telefono, direccion, usuario, email, contrasenha) 
                       VALUES(%s, %s, %s, %s, %s, %s)"""
            
            cursor.execute(query, (nombre, telefono, direccion, usuario, email, contrasenha))
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
            cursor.execute('SELECT * FROM usuario WHERE username = %s', username_)
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

            response = request.get_json()
            nombre = response['nombre']
            telefono = response['telefono']
            direccion = response['direccion']
            email = response['email']
            contrasenha = response['contrasenha']

            query = """UPDATE usuario 
                    SET nombre=%s, telefono=%s, direccion=%s,  
                    usuario=%s, email=%s, contrasenha=%s"""
            
            cursor.execute(query, (nombre, telefono, direccion, username_, email, contrasenha))
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

            cursor.execute('DELETE FROM usuario WHERE username = %s', username_)
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
        


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)