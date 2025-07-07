import conexion 
from datetime import datetime

def save(producto):
    try:
        db = conexion.conectar()
        if db is None:
            return {"respuesta": False, "mensaje": "Error de conexión a la base de datos"}
        cursor = db.cursor()
        
        # Generar fecha automática (YYYY-MM-DD)
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        
        # Asegurar que todos los campos necesarios están presentes
        datos_completos = {
            "producto": producto["producto"],
            "precio": producto["precio"],
            "cantidad": producto["cantidad"],
            "categoria": producto.get("categoria", "General"),  # Valor por defecto si no se proporciona
            "fecha": fecha_actual
        }

        columnas = ', '.join(datos_completos.keys())
        placeholders = ', '.join(['?'] * len(datos_completos))
        valores = tuple(datos_completos.values())

        sql = f"INSERT INTO supermercado ({columnas}) VALUES ({placeholders})"
        cursor.execute(sql, valores)
        db.commit()

        return {
            "respuesta": True,
            "mensaje": "Producto registrado exitosamente"
        }

    except Exception as ex:
        if "UNIQUE" in str(ex):
            return {"respuesta": False, "mensaje": "El producto ya existe"}
        return {"respuesta": False, "mensaje": f"Error al guardar: {str(ex)}"}

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals() and db is not None: db.close()

def findAll(order_by="producto ASC"):
    try:
        db = conexion.conectar()
        if db is None:
            return {"respuesta": False, "mensaje": "Error de conexión a la base de datos"}
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM supermercado ORDER BY {order_by}")
        productos = cursor.fetchall()
        # Resto del código igual...
        
        return {
            "respuesta": True,
            "producto": productos,
            "mensaje": "OK" if productos else "No hay productos registrados"
        }

    except Exception as ex:
        return {"respuesta": False, "mensaje": f"Error al consultar: {str(ex)}"}

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals() and db is not None: db.close()

def update(producto):
    try:
        db = conexion.conectar()
        if db is None:
            return {"respuesta": False, "mensaje": "Error de conexión a la base de datos"}
        cursor = db.cursor()

        sql = """
        UPDATE supermercado 
        SET producto = ?, precio = ?, cantidad = ?, categoria = ?
        WHERE producto = ?
        """
        valores = (
            producto["producto"],
            producto["precio"],
            producto["cantidad"],
            producto["categoria"],
            producto["anterior"]
        )

        cursor.execute(sql, valores)
        db.commit()

        return {
            "respuesta": cursor.rowcount > 0,
            "mensaje": "Producto actualizado" if cursor.rowcount > 0 else "No se encontró el producto"
        }

    except Exception as ex:
        return {"respuesta": False, "mensaje": f"Error al actualizar: {str(ex)}"}

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals() and db is not None: db.close()

def delete(idproducto):
    try:
        db = conexion.conectar()
        if db is None:
            return {"respuesta": False, "mensaje": "Error de conexión a la base de datos"}
        cursor = db.cursor()

        cursor.execute("DELETE FROM supermercado WHERE id = ?", (idproducto,))
        db.commit()

        return {
            "respuesta": cursor.rowcount > 0,
            "mensaje": "Producto eliminado" if cursor.rowcount > 0 else "ID no encontrado"
        }

    except Exception as ex:
        return {"respuesta": False, "mensaje": f"Error al eliminar: {str(ex)}"}
    
    # Agregar esta nueva función al final del archivo productos_datos.py
def find_low_stock(threshold=5):
    try:
        db = conexion.conectar()
        if db is None:
            return {"respuesta": False, "mensaje": "Error de conexión a la base de datos"}
        cursor = db.cursor()
        cursor.execute("SELECT * FROM supermercado WHERE cantidad < ? ORDER BY cantidad ASC", (threshold,))
        productos = cursor.fetchall()
        
        return {
            "respuesta": True,
            "producto": productos,
            "mensaje": f"Productos con stock bajo (menos de {threshold} unidades)" if productos else "No hay productos con stock bajo"
        }

    except Exception as ex:
        return {"respuesta": False, "mensaje": f"Error al consultar stock bajo: {str(ex)}"}

def search_suggestions(search_term):
    """Busca productos cuyos nombres coincidan parcialmente con el término de búsqueda"""
    try:
        db = conexion.conectar()
        if db is None:
            return []
        cursor = db.cursor()
        
        # Buscar productos que contengan el término de búsqueda (insensible a mayúsculas)
        cursor.execute("""
            SELECT id, producto, precio, cantidad, categoria, fecha 
            FROM supermercado 
            WHERE LOWER(producto) LIKE LOWER(?) 
            ORDER BY producto
            LIMIT 5
        """, (f"%{search_term}%",))
        
        return cursor.fetchall()
        
    except Exception as ex:
        print(f"Error al buscar sugerencias: {str(ex)}")
        return []
        
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals() and db is not None: db.close()

def autenticar_usuario(username, password):
    try:
        db = conexion.conectar()
        if db is None:
            return None
        cursor = db.cursor()
        cursor.execute("SELECT es_admin FROM usuarios WHERE username=? AND password=?", (username, password))
        row = cursor.fetchone()
        if row:
            # Si es_admin es 1, es admin; si es 0, es usuario
            return "admin" if row[0] == 1 else "usuario"
        return None
    except Exception as ex:
        print(f"Error en autenticación: {str(ex)}")
        return None
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals() and db is not None: db.close()