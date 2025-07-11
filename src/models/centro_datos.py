import numpy as np

from src.utils.calculadora import Calculadora



class CentroDeDatos:
    def __init__(self):
        """
        Inicializa el centro de datos con arrays numpy estáticos para almacenar 
        los datos de CPU y nombres de servidores
        """
        # Array numpy estático 25x30 para datos de CPU (25 servidores, 30 días)
        self.datos_cpu = np.zeros((25, 30), dtype=np.float64)
        
        # Array numpy estático para nombres de servidores
        self.nombres_servidores = np.empty(25, dtype=object)  # Strings de hasta 20 caracteres

        self.datos_cargados = False
        self.calculadora = Calculadora()
    
    def cargar_datos(self, archivo):
        """
        Carga los datos desde el archivo uso_cpu_junio.txt
        Separa nombres de servidores y valores numéricos y los almacena
        en arrays numpy estáticos
        """
        try:
            with open(archivo, 'r', encoding='utf-8') as file:
                lineas = file.readlines()
            
            if len(lineas) > 25:
                print("Advertencia: El archivo tiene más de 25 servidores. Solo se procesarán los primeros 25.")
            
            for i, linea in enumerate(lineas[:25]):  # Procesar máximo 25 servidores
                linea = linea.strip()
                if linea:
                    partes = linea.split(';')
                    
                    # Almacenar nombre del servidor en array numpy estático
                    self.nombres_servidores[i] = partes[0]
                    
                    # Almacenar valores de CPU en array numpy estático
                    valores_cpu = [float(valor) for valor in partes[1:31]]  # Máximo 30 días
                    
                    if len(valores_cpu) > 30:
                        print(f"Advertencia: {partes[0]} tiene más de 30 días. Solo se tomarán los primeros 30.")
                        valores_cpu = valores_cpu[:30]
                    
                    # Llenar el array estático con los valores
                    for j, valor in enumerate(valores_cpu):
                        self.datos_cpu[i, j] = valor
            
            self.datos_cargados = True
            print("Datos cargados exitosamente en arrays numpy estáticos:")
            print("- Array de datos CPU: {self.datos_cpu.shape}")
            print("- Array de nombres: {self.nombres_servidores.shape}")
            
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo {archivo}")
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
    
    def calcular_promedio_mensual_por_servidor(self):
        """
        Calcula el promedio mensual de uso de CPU por servidor
        usando arrays numpy pero implementando el cálculo manualmente
        """
        if not self.datos_cargados:
            print("No hay datos cargados")
            return
        
        print("\n=== PROMEDIO MENSUAL DE USO DE CPU POR SERVIDOR ===")
        print("-" * 60)
        
        # Crear array numpy estático para almacenar promedios
        promedios = np.zeros(25, dtype=np.float64)
        
        for i in range(25):
            # Usar método manual de la calculadora
            promedio = self.calculadora.calcular_promedio(self.datos_cpu[i, :])
            promedios[i] = promedio
            
            print(f"{self.nombres_servidores[i]:<15}: {promedio:.2f}%")
        
        return promedios
    
    def encontrar_dia_mayor_carga(self):
        """
        Determina el día con mayor carga total de CPU usando arrays numpy
        pero implementando la búsqueda manualmente
        """
        if not self.datos_cargados:
            print("No hay datos cargados")
            return
        
        # Crear array numpy estático para sumas diarias
        sumas_diarias = np.zeros(30, dtype=np.float64)
        
        # Calcular suma para cada día manualmente
        for dia in range(30):
            suma_dia = self.calculadora.calcular_suma(self.datos_cpu[:, dia])
            sumas_diarias[dia] = suma_dia
        
        # Encontrar el máximo manualmente
        dia_max_carga, max_carga = self.calculadora.encontrar_maximo(sumas_diarias)
        
        print("\n=== DÍA CON MAYOR CARGA TOTAL DE CPU ===")
        print("-" * 45)
        print(f"Día: {dia_max_carga + 1} de junio")
        print(f"Carga total: {max_carga:.2f}%")
        
        # Mostrar detalles del día usando el array numpy
        print(f"\nDetalles del día {dia_max_carga + 1}:")
        for i in range(25):
            print(f"{self.nombres_servidores[i]:<15}: {self.datos_cpu[i, dia_max_carga]:.2f}%")
        
        return dia_max_carga, max_carga
    
    def encontrar_servidor_menor_uso(self):
        """
        Identifica el servidor con menor uso promedio de CPU
        usando arrays numpy pero implementando la búsqueda manualmente
        """
        if not self.datos_cargados:
            print("Error: No hay datos cargados")
            return
        
        # Crear array numpy estático para promedios
        promedios = np.zeros(25, dtype=np.float64)
        
        # Calcular promedio para cada servidor manualmente
        for i in range(25):
            promedio = self.calculadora.calcular_promedio(self.datos_cpu[i, :])
            promedios[i] = promedio
        
        # Encontrar el mínimo manualmente
        servidor_min_uso, min_promedio = self.calculadora.encontrar_minimo(promedios)
        
        print("\n=== SERVIDOR CON MENOR USO PROMEDIO DE CPU ===")
        print("-" * 50)
        print(f"Servidor: {self.nombres_servidores[servidor_min_uso]}")
        print(f"Promedio de uso: {min_promedio:.2f}%")
        
        # Mostrar datos del servidor usando el array numpy
        print(f"\nPrimeros 10 días de {self.nombres_servidores[servidor_min_uso]}:")
        for dia in range(10):
            print(f"Día {dia + 1}: {self.datos_cpu[servidor_min_uso, dia]:.2f}%")
        
        return servidor_min_uso, min_promedio
    
    def mostrar_resumen_estadisticas(self):
        """
        Muestra un resumen completo de las estadísticas del centro de datos
        """
        if not self.datos_cargados:
            print("Error: No hay datos cargados")
            return
        
        print(f"\n{'='*60}")
        print("RESUMEN DEL CENTRO DE DATOS - JUNIO 2025")
        print(f"{'='*60}")
        print("Estructura de datos:")
        print(f"- Array numpy datos_cpu: {self.datos_cpu.shape} ({self.datos_cpu.dtype})")
        print(f"- Array numpy nombres_servidores: {self.nombres_servidores.shape} ({self.nombres_servidores.dtype})")
        print(f"- Total de mediciones: {self.datos_cpu.size}")
        print(f"- Memoria utilizada por datos_cpu: {self.datos_cpu.nbytes} bytes")
        print(f"- Memoria utilizada por nombres: {self.nombres_servidores.nbytes} bytes")
    
    def obtener_datos_servidor(self, nombre_servidor):
        """
        Obtiene los datos de un servidor específico
        """
        if not self.datos_cargados:
            return None
        
        # Buscar el servidor en el array numpy
        indices = np.nonzero(self.nombres_servidores == nombre_servidor)[0]
        if len(indices) > 0:
            return self.datos_cpu[indices[0], :]
        return None
    
    def obtener_datos_dia(self, dia):
        """
        Obtiene los datos de un día específico (1-30)
        """
        if not self.datos_cargados or dia < 1 or dia > 30:
            return None
        
        return self.datos_cpu[:, dia-1]
