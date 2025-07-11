import numpy as np


class Calculadora:
    """
    Clase que implementa cálculos manuales
    """
    
    def calcular_promedio(self, array_datos):
        """
        Calcula el promedio de un array numpy 
        
        Args:
            array_datos: Array numpy con los datos
            
        Returns:
            float: Promedio calculado 
        """
        suma = 0.0
        contador = 0
        
        # Iterar manualmente por todos los elementos del array
        for valor in array_datos:
            suma += valor
            contador += 1
        
        if contador == 0:
            return 0.0
        
        return suma / contador
    
    def calcular_suma(self, array_datos):
        """
        Calcula la suma de un array numpy 
        
        Args:
            array_datos: Array numpy con los datos
            
        Returns:
            float: Suma calculada manualmente
        """
        suma = 0.0
        
        # Iterar manualmente por todos los elementos del array
        for valor in array_datos:
            suma += valor
        
        return suma
    
    def encontrar_maximo(self, array_datos):
        """
        Encuentra el valor máximo y su índice
        
        Args:
            array_datos: Array numpy con los datos
            
        Returns:
            tuple: (índice_máximo, valor_máximo)
        """
        if len(array_datos) == 0:
            return -1, 0.0
        
        max_valor = array_datos[0]
        max_indice = 0
        
        # Iterar manualmente para encontrar el máximo
        for i in range(1, len(array_datos)):
            if array_datos[i] > max_valor:
                max_valor = array_datos[i]
                max_indice = i
        
        return max_indice, max_valor
    
    def encontrar_minimo(self, array_datos):
        """
        Encuentra el valor mínimo y su índice de forma manual
        
        Args:
            array_datos: Array numpy con los datos
            
        Returns:
            tuple: (índice_mínimo, valor_mínimo)
        """
        if len(array_datos) == 0:
            return -1, 0.0
        
        min_valor = array_datos[0]
        min_indice = 0
        
        # Iterar manualmente para encontrar el mínimo
        for i in range(1, len(array_datos)):
            if array_datos[i] < min_valor:
                min_valor = array_datos[i]
                min_indice = i
        
        return min_indice, min_valor
    
    def calcular_estadisticas(self, array_datos):
        """
        Calcula estadísticas básicas
        
        Args:
            array_datos: Array numpy con los datos
            
        Returns:
            dict: Diccionario con las estadísticas calculadas
        """
        if len(array_datos) == 0:
            return {
                'promedio': 0.0,
                'suma': 0.0,
                'maximo': 0.0,
                'minimo': 0.0,
                'indice_maximo': -1,
                'indice_minimo': -1
            }
        
        # Calcular todas las estadísticas en una sola pasada
        suma = 0.0
        max_valor = array_datos[0]
        min_valor = array_datos[0]
        max_indice = 0
        min_indice = 0
        
        for i, valor in enumerate(array_datos):
            suma += valor
            
            if valor > max_valor:
                max_valor = valor
                max_indice = i
            
            if valor < min_valor:
                min_valor = valor
                min_indice = i
        
        promedio = suma / len(array_datos)
        
        return {
            'promedio': promedio,
            'suma': suma,
            'maximo': max_valor,
            'minimo': min_valor,
            'indice_maximo': max_indice,
            'indice_minimo': min_indice,
            'total_elementos': len(array_datos)
        }
    
    def comparar_arrays(self, array1, array2):
        """
        Compara dos arrays elemento por elemento 
        
        Args:
            array1: Primer array numpy
            array2: Segundo array numpy
            
        Returns:
            dict: Diccionario con los resultados de la comparación
        """
        if len(array1) != len(array2):
            return {'error': 'Los arrays tienen diferentes tamaños'}
        
        elementos_iguales = 0
        diferencias = []
        
        for i in range(len(array1)):
            if abs(array1[i] - array2[i]) < 1e-10:  # Consideramos iguales con tolerancia
                elementos_iguales += 1
            else:
                diferencias.append({
                    'indice': i,
                    'valor1': array1[i],
                    'valor2': array2[i],
                    'diferencia': abs(array1[i] - array2[i])
                })
        
        return {
            'elementos_iguales': elementos_iguales,
            'elementos_diferentes': len(diferencias),
            'porcentaje_igualdad': (elementos_iguales / len(array1)) * 100,
            'diferencias': diferencias
        }
