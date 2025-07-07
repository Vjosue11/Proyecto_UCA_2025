#!/usr/bin/env python3
"""
Script para verificar las dependencias del Sistema de Supermercado
"""

import sys
import importlib

def check_module(module_name, description):
    """Verifica si un módulo está disponible"""
    try:
        importlib.import_module(module_name)
        print(f"✅ {description} ({module_name}) - DISPONIBLE")
        return True
    except ImportError:
        print(f"❌ {description} ({module_name}) - NO DISPONIBLE")
        return False

def main():
    print("=" * 60)
    print("VERIFICACIÓN DE DEPENDENCIAS - SISTEMA DE SUPERMERCADO")
    print("=" * 60)
    
    # Lista de módulos requeridos
    required_modules = [
        ("tkinter", "Interfaz gráfica (Tkinter)"),
        ("sqlite3", "Base de datos SQLite"),
        ("re", "Expresiones regulares"),
        ("datetime", "Manejo de fechas y horas")
    ]
    
    all_available = True
    
    for module_name, description in required_modules:
        if not check_module(module_name, description):
            all_available = False
    
    print("\n" + "=" * 60)
    
    if all_available:
        print("🎉 TODAS LAS DEPENDENCIAS ESTÁN DISPONIBLES")
        print("✅ El sistema está listo para ejecutarse")
        print("\nPara ejecutar el sistema:")
        print("   python prueba/main.py")
    else:
        print("❌ FALTAN DEPENDENCIAS")
        print("⚠️  Algunos módulos no están disponibles")
        print("\nNota: Este proyecto utiliza solo módulos de la biblioteca estándar de Python.")
        print("Si faltan dependencias, verifica tu instalación de Python.")
    
    print("=" * 60)

if __name__ == "__main__":
    main() 