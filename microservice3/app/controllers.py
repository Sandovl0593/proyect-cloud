from app import db
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
                producto_d = {"codigo": i[0], "nombre": i[2], "precio": i[3], "marca": i[4], "categoria": i[5]}
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
        
class Inventario(Resource):
    def post(self):
        try:
            conn = db.connect()
            cursor = conn.cursor()

            compra_u = request.get_json()
            usuario_l = compra_u['usuario']

            query = "SELECT * FROM proyecto.compra WHERE usuario_c = %s"

            cursor.execute(query, (usuario_l,))
            compras_l = cursor.fetchall()

            compras_d = []
            for i in compras_l:
                compra_d = {"codigo_c": i[0], "codigo_p": i[1],
                            "usuario_c": i[2], "usuario_v": i[3]}
                compras_d.append(compra_d)

            response = jsonify(compras_d)
            response.status_code = 200

        except Exception as e:
            response = jsonify(message='No se pudo obtener el inventario.')
            response.status_code = 400
            print(e)

        finally:
            cursor.close()
            conn.close()
            return response
