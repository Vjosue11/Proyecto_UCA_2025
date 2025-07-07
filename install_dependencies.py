#!/usr/bin/env python3
"""
Script de instalación automática para el Sistema de Supermercado
"""

import sys
import os
import subprocess
import importlib
import sqlite3
from pathlib import Path

def print_header():
    print("=" * 70)
    print("🔧 INSTALADOR AUTOMÁTICO - SISTEMA DE SUPERMERCADO")
    print("=" * 70)

def check_python_version():
    """Verifica la versión de Python"""
    version = sys.version_info
    print(f"🐍 Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print("❌ ERROR: Se requiere Python 3.6 o superior")
        return False
    
    print("✅ Versión de Python compatible")
    return True

def check_module(module_name, description):
    """Verifica si un módulo está disponible"""
    try:
        importlib.import_module(module_name)
        print(f"✅ {description} ({module_name}) - DISPONIBLE")
        return True
    except ImportError as e:
        print(f"❌ {description} ({module_name}) - NO DISPONIBLE")
        print(f"   Error: {e}")
        return False

def install_pip_package(package_name):
    """Instala un paquete usando pip"""
    try:
        print(f"📦 Instalando {package_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"✅ {package_name} instalado correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al instalar {package_name}: {e}")
        return False

def check_database():
    """Verifica y crea la base de datos si es necesario"""
    try:
        db_path = Path("supermercado.db")
        if db_path.exists():
            # Verificar que la base de datos es accesible
            conn = sqlite3.connect("supermercado.db")
            cursor = conn.cursor()
            
            # Verificar si las tablas existen
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cursor.fetchall()]
            
            required_tables = ['supermercado', 'entradas', 'salidas']
            missing_tables = [table for table in required_tables if table not in tables]
            
            if missing_tables:
                print(f"⚠️  Faltan tablas en la base de datos: {missing_tables}")
                print("   Se crearán automáticamente al ejecutar el programa")
            else:
                print("✅ Base de datos completa con todas las tablas")
            
            conn.close()
        else:
            print("⚠️  Base de datos no encontrada")
            print("   Se creará automáticamente al ejecutar el programa")
        
        return True
    except Exception as e:
        print(f"❌ Error al verificar base de datos: {e}")
        return False

def test_tkinter():
    """Prueba que Tkinter funcione correctamente"""
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # Ocultar ventana
        
        # Crear un widget de prueba
        entry = tk.Entry(root)
        entry.pack()
        entry.focus_set()
        
        # Verificar que el foco funciona
        focused_widget = root.focus_get()
        if focused_widget == entry:
            print("✅ Tkinter funciona correctamente (foco OK)")
        else:
            print("⚠️  Tkinter funciona pero puede haber problemas con el foco")
        
        root.destroy()
        return True
    except Exception as e:
        print(f"❌ Error al probar Tkinter: {e}")
        return False

def create_sample_data():
    """Crea datos de ejemplo si la base de datos está vacía"""
    try:
        conn = sqlite3.connect("supermercado.db")
        cursor = conn.cursor()
        
        # Verificar si hay productos
        cursor.execute("SELECT COUNT(*) FROM supermercado")
        count = cursor.fetchone()[0]
        
        if count == 0:
            print("📝 Creando datos de ejemplo...")
            
            # Insertar productos de ejemplo
            sample_products = [
                ("Manzanas", 150, 50, "Frutas"),
                ("Leche", 80, 30, "Lácteos"),
                ("Pan", 45, 100, "Panadería"),
                ("Arroz", 120, 25, "Granos"),
                ("Aceite", 95, 40, "Aceites")
            ]
            
            for producto, precio, cantidad, categoria in sample_products:
                cursor.execute("""
                    INSERT INTO supermercado (producto, precio, cantidad, categoria, fecha)
                    VALUES (?, ?, ?, ?, date('now'))
                """, (producto, precio, cantidad, categoria))
            
            conn.commit()
            print("✅ Datos de ejemplo creados")
        else:
            print(f"✅ Base de datos contiene {count} productos")
        
        conn.close()
        return True
    except Exception as e:
        print(f"⚠️  No se pudieron crear datos de ejemplo: {e}")
        return True  # No es crítico

def main():
    print_header()
    
    # Verificar versión de Python
    if not check_python_version():
        return False
    
    print("\n🔍 Verificando módulos requeridos...")
    
    # Lista de módulos requeridos
    required_modules = [
        ("tkinter", "Interfaz gráfica (Tkinter)"),
        ("sqlite3", "Base de datos SQLite"),
        ("re", "Expresiones regulares"),
        ("datetime", "Manejo de fechas y horas")
    ]
    
    all_modules_ok = True
    for module_name, description in required_modules:
        if not check_module(module_name, description):
            all_modules_ok = False
    
    if not all_modules_ok:
        print("\n❌ Faltan módulos críticos")
        print("   Estos módulos son parte de la biblioteca estándar de Python")
        print("   Verifica tu instalación de Python")
        return False
    
    print("\n🗄️  Verificando base de datos...")
    check_database()
    
    print("\n🧪 Probando Tkinter...")
    test_tkinter()
    
    print("\n📊 Creando datos de ejemplo...")
    create_sample_data()
    
    print("\n" + "=" * 70)
    print("🎉 INSTALACIÓN COMPLETADA")
    print("✅ El sistema está listo para usar")
    print("\n📋 Para ejecutar el sistema:")
    print("   python prueba/main.py")
    print("\n📋 Para la versión de usuario:")
    print("   python prueba/main_usuario.py")
    print("=" * 70)
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 