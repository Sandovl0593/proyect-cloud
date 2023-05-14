from app import db
from flask import jsonify, request
from flask_restful import Resource

class Productos(Resource):
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
                producto_d = {"codigo": i[0], "nombre": i[2], "precio": i[3], 
                              "marca": i[4], "categoria": i[5]}
                productos_d.append(producto_d)

            response = jsonify(productos_d)

        except Exception:
            response = jsonify(message='Failed to get productos.')

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

            query = """SELECT c.codigo_c, p.nombre, p.precio, c.usuario_v 
                    FROM proyecto.compra c, proyecto.producto p 
                    WHERE c.usuario_c = %s AND c.codigo_p = p.codigo_p"""

            cursor.execute(query, (usuario_l,))
            compras_l = cursor.fetchall()

            compras_d = []
            for i in compras_l:
                compra_d = {"codigo_c": i[0], "nombre": i[1],
                            "precio": i[2], "usuario_v": i[3]}
                compras_d.append(compra_d)

            response = jsonify(compras_d)

        except Exception:
            response = jsonify(message='No se pudo obtener el inventario.')

        finally:
            cursor.close()
            conn.close()
            return response
