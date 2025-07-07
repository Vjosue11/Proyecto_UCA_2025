#!/usr/bin/env python3
"""
Script de prueba para verificar el login modernizado
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os

# Agregar el directorio actual al path para importar los módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from main import mostrar_login
    print("✅ Módulo main importado correctamente")
    
    # Verificar que las funciones existen
    if 'mostrar_login' in globals():
        print("✅ Función mostrar_login encontrada")
    else:
        print("❌ Función mostrar_login no encontrada")
        
    print("\n🚀 Iniciando aplicación de login...")
    print("📝 Usuarios de prueba disponibles:")
    print("   - admin/admin (Administrador)")
    print("   - usuario/usuario (Usuario)")
    print("\n💡 Presiona Ctrl+C para salir")
    
    # Iniciar la aplicación
    mostrar_login()
    
except ImportError as e:
    print(f"❌ Error al importar módulos: {e}")
except Exception as e:
    print(f"❌ Error inesperado: {e}") 