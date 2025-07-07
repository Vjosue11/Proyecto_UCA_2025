import conexion
import os

def limpiar_base_datos():
    try:
        db = conexion.conectar()
        if db is None:
            print("Error: No se pudo conectar a la base de datos")
            return
        
        cursor = db.cursor()
        
        # Limpiar todas las tablas
        print("Limpiando tabla supermercado...")
        cursor.execute("DELETE FROM supermercado")
        
        print("Limpiando tabla entradas...")
        cursor.execute("DELETE FROM entradas")
        
        print("Limpiando tabla salidas...")
        cursor.execute("DELETE FROM salidas")
        
        print("Limpiando tabla usuarios...")
        cursor.execute("DELETE FROM usuarios")
        
        # Reinicializar usuarios por defecto
        print("Creando usuarios por defecto...")
        cursor.execute("INSERT INTO usuarios (username, password, es_admin) VALUES (?, ?, ?)", ("admin", "admin123", 1))
        cursor.execute("INSERT INTO usuarios (username, password, es_admin) VALUES (?, ?, ?)", ("usuario", "usuario", 0))
        
        db.commit()
        print("Base de datos limpiada exitosamente!")
        print("Usuarios por defecto creados:")
        print("- admin / admin123 (administrador)")
        print("- usuario / usuario (usuario normal)")
        
    except Exception as ex:
        print(f"Error al limpiar la base de datos: {str(ex)}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals() and db is not None: db.close()

if __name__ == "__main__":
    limpiar_base_datos() 