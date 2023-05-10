from app import app, db
from flask import jsonify, request
from flask_restful import Resource

class Vender(Resource):
    def post(self):
        try:
            conn = db.connect()
            cursor = conn.cursor()

            producto_u = request.get_json()
            usuario_l = producto_u['usuario']
            query = "SELECT * FROM proyecto.producto WHERE usuario_p = %s"
            cursor.execute(query, (usuario_l,))
            productos_l = cursor.fetchall()

            productos_d = []
            for i in productos_l:
                producto_d = {"codigo": i[0], "nombre": i[1],
                              "precio": i[2], "marca": i[3], "tipo": i[4]}
                productos_d.append(producto_d)

            response = jsonify(productos_d)
            response.status_code = 200

        except Exception as e:
            response = jsonify(message='Failed to get productos.')
            response.status_code = 400
            print(e)

        finally:
            cursor.close()
            conn.close()
            return response


