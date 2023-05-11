from app import db
from flask import jsonify, request
from flask_restful import Resource
from random import randint, choice
from string import ascii_uppercase

class RegistrarCompra(Resource):
    def post(self):
        try:
            conn = db.connect()
            cursor = conn.cursor()

            nueva_compra = request.get_json()
            codigo_c = str(randint(1,1000))+choice([i for i in ascii_uppercase])
            
            codigo_p = nueva_compra['codigo_producto']
            comprador = nueva_compra['usuario_comprador']
            vendedor = nueva_compra['usuario_vendedor']

            query1 = "UPDATE proyecto.producto SET usuario_p=%s WHERE codigo_p=%s"
            cursor.execute(query1, (comprador, codigo_p))
            conn.commit()

            query2 = """INSERT INTO proyecto.compra(codigo_c, codigo_p, usuario_c, usuario_v)
                       VALUES(%s, %s, %s, %s)"""
            cursor.execute(query2, (codigo_c, codigo_p, comprador, vendedor))
            conn.commit()

            response = jsonify(message='Compra agregada exitosamente.', id=cursor.lastrowid)
            response.status_code = 200

        except Exception:
            response = jsonify(message='No se pudo agregar la compra.')
            response.status_code = 400

        finally:
            cursor.close()
            conn.close()
            return response


class Tienda(Resource):
    def post(self):
        try:
            conn = db.connect()
            cursor = conn.cursor()

            usuario_l = request.get_json()['usuario']
            
            query = "SELECT * FROM proyecto.producto WHERE usuario_p != %s"
            cursor.execute(query, (usuario_l,))
            productos_nl = cursor.fetchall()
 
            productos_d = []
            for i in productos_nl:
                producto_d = {"codigo": i[0], "usuario_nombre": i[1], "nombre": i[2],
                              "precio": i[3], "marca": i[4], "tipo": i[5]}
                productos_d.append(producto_d)
            
            response = jsonify(productos_d)
            response.status_code = 200

        except Exception:
            response = jsonify(message='Failed to get productos.')
            response.status_code = 400

        finally:
            cursor.close()
            conn.close()
            return response
        
class RegistrarProducto(Resource):
    def post(self):
        try:
            conn = db.connect()
            cursor = conn.cursor()

            nuevo_producto = request.get_json()
            codigo = nuevo_producto['codigo']
            usuario = nuevo_producto['usuario']
            nombre = nuevo_producto['nombre']
            precio = nuevo_producto['precio']
            marca = nuevo_producto['marca']
            categoria = nuevo_producto['categoria']

            query = """INSERT INTO proyecto.producto(codigo_p, usuario_p, nombre, precio, marca, categoria)
                       VALUES(%s, %s, %s, %s, %s, %s)"""

            cursor.execute(query, (codigo, usuario, nombre, precio, marca, categoria))
            conn.commit()

            response = jsonify(message='Producto agregado exitosamente.', id=cursor.lastrowid)
            response.status_code = 200

        except Exception:
            response = jsonify(message='No se pudo agregar el producto.')
            response.status_code = 400

        finally:
            cursor.close()
            conn.close()
            return response
