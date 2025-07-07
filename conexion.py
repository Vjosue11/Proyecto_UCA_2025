# En conexion.py, modifica la función conectar():
import sqlite3
import os

def conectar():
    try:
        # Ruta absoluta a supermercado.db en la raíz del proyecto
        db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "supermercado.db")
        miConexion = sqlite3.connect(db_path)
        cursor = miConexion.cursor()

        # Crear la tabla de productos si no existe
        sql_productos = """ 
        CREATE TABLE IF NOT EXISTS supermercado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT NOT NULL UNIQUE,
            precio INTEGER NOT NULL,
            cantidad INTEGER NOT NULL,
            categoria TEXT NOT NULL,
            fecha TEXT NOT NULL
        )
        """
        cursor.execute(sql_productos)
        
        # Crear tabla para movimientos de entrada
        sql_entradas = """
        CREATE TABLE IF NOT EXISTS entradas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_producto INTEGER NOT NULL,
            producto TEXT NOT NULL,
            fecha TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            tipo TEXT NOT NULL,
            FOREIGN KEY (id_producto) REFERENCES supermercado(id)
        )
        """
        cursor.execute(sql_entradas)
        
        # Crear tabla para movimientos de salida
        sql_salidas = """
        CREATE TABLE IF NOT EXISTS salidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_producto INTEGER NOT NULL,
            producto TEXT NOT NULL,
            fecha TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            tipo TEXT NOT NULL,
            FOREIGN KEY (id_producto) REFERENCES supermercado(id)
        )
        """
        cursor.execute(sql_salidas)

        # Crear tabla de usuarios
        sql_usuarios = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            tipo TEXT NOT NULL CHECK(tipo IN ('admin', 'usuario'))
        )
        """
        cursor.execute(sql_usuarios)

        # Insertar usuarios por defecto si la tabla está vacía
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO usuarios (username, password, tipo) VALUES (?, ?, ?)", ("admin", "admin", "admin"))
            cursor.execute("INSERT INTO usuarios (username, password, tipo) VALUES (?, ?, ?)", ("usuario", "usuario", "usuario"))
            miConexion.commit()
        
        return miConexion

    except Exception as ex:
        print("Error al conectar a la base de datos:", ex)
        return None

    finally:
        try:
            cursor.close()
        except:
            pass