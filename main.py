"""
Sistema de Análisis de CPU - Centro de Datos
Autor: Sistema de Análisis
Fecha: Julio 2025

Este sistema analiza el uso de CPU de 25 servidores durante el mes de junio
usando programación orientada a objetos y arrays numpy estáticos.

Punto de entrada principal del sistema.
"""

import sys
import os

# Agregar src al path para importaciones
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from controllers.controlador_principal import ejecutar_sistema


def main():
    """
    Función principal - Punto de entrada del sistema
    """
    try:
        ejecutar_sistema()
    except Exception as e:
        print(f"Error crítico del sistema: {e}")
        print("El sistema se cerrará.")


if __name__ == "__main__":
    main()