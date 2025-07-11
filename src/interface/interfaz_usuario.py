"""
Módulo de interfaz de usuario para el sistema de análisis de CPU
Maneja toda la interacción con el usuario a través de menús y consultas
"""


class InterfazUsuario:
    """Clase que maneja toda la interfaz de usuario del sistema"""
    
    def __init__(self, centro_datos):
        """
        Inicializa la interfaz con una referencia al centro de datos
        
        Args:
            centro_datos: Instancia de CentroDeDatos
        """
        self.centro = centro_datos
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema"""
        print("SISTEMA DE ANÁLISIS DE CPU - CENTRO DE DATOS")
        print("="*60)
        print("1. Cargar datos desde archivo")
        print("2. Mostrar resumen de estadísticas")
        print("3. Calcular promedio mensual por servidor")
        print("4. Encontrar día con mayor carga total")
        print("5. Encontrar servidor con menor uso promedio")
        print("6. Análisis completo")
        print("7. Consultar datos de servidor específico")
        print("8. Consultar datos de día específico")
        print("0. Salir")
        print("-"*60)
    
    def mostrar_mensaje_carga(self):
        """Muestra mensaje de carga de datos"""
        print("Cargando datos...")
    
    def mostrar_mensaje_salida(self):
        """Muestra mensaje de salida del sistema"""
        print("Saliendo del sistema...")
    
    def mostrar_error_datos_no_cargados(self):
        """Muestra error cuando no hay datos cargados"""
        print("Error: Primero debe cargar los datos (opción 1)")
    
    def mostrar_opcion_invalida(self):
        """Muestra mensaje de opción inválida"""
        print("Opción inválida. Intente nuevamente.")
    
    def ejecutar_analisis_completo(self):
        """Ejecuta y muestra todos los análisis disponibles"""
        if not self.centro.datos_cargados:
            self.mostrar_error_datos_no_cargados()
            return
        
        print("\n" + "="*60)
        print("EJECUTANDO ANÁLISIS COMPLETO...")
        print("="*60)
        
        # Mostrar resumen
        self.centro.mostrar_resumen_estadisticas()
        
        # Realizar todos los análisis
        self.centro.calcular_promedio_mensual_por_servidor()
        self.centro.encontrar_dia_mayor_carga()
        self.centro.encontrar_servidor_menor_uso()
        
        print("\n" + "="*60)
        print("ANÁLISIS COMPLETADO")
        print("="*60)
    
    def consultar_servidor_especifico(self):
        """Permite consultar datos de un servidor específico"""
        if not self.centro.datos_cargados:
            print("Error: Primero debe cargar los datos")
            return
        
        self._mostrar_lista_servidores()
        
        try:
            opcion = input("\nIngrese el nombre del servidor o su número: ").strip()
            nombre_servidor = self._procesar_seleccion_servidor(opcion)
            
            if nombre_servidor:
                self._mostrar_datos_servidor(nombre_servidor)
                
        except ValueError:
            print("Entrada inválida")
    
    def consultar_dia_especifico(self):
        """Permite consultar datos de un día específico"""
        if not self.centro.datos_cargados:
            print("Error: Primero debe cargar los datos")
            return
        
        try:
            dia = int(input("Ingrese el día (1-30): "))
            
            if 1 <= dia <= 30:
                self._mostrar_datos_dia(dia)
            else:
                print("Día inválido. Debe estar entre 1 y 30")
                
        except ValueError:
            print("Entrada inválida. Debe ingresar un número")
    
    def solicitar_opcion(self):
        """Solicita y retorna la opción seleccionada por el usuario"""
        return input("Seleccione una opción: ").strip()
    
    def pausar_para_continuar(self):
        """Pausa la ejecución esperando que el usuario presione Enter"""
        input("\nPresione Enter para continuar...")
    
    def mostrar_error_inesperado(self, error):
        """Muestra un error inesperado"""
        print(f"Error inesperado: {error}")
    
    def mostrar_cancelacion_usuario(self):
        """Muestra mensaje de cancelación por parte del usuario"""
        print("\n\nOperación cancelada por el usuario.")
    
    def _mostrar_lista_servidores(self):
        """Muestra la lista de servidores disponibles"""
        print("\nServidores disponibles:")
        for i, nombre in enumerate(self.centro.nombres_servidores):
            if nombre:  # Solo mostrar servidores con datos
                print(f"{i+1:2d}. {nombre}")
    
    def _procesar_seleccion_servidor(self, opcion):
        """
        Procesa la selección del usuario para obtener el nombre del servidor
        
        Args:
            opcion: Opción ingresada por el usuario (número o nombre)
            
        Returns:
            str: Nombre del servidor o None si es inválido
        """
        # Verificar si es un número
        if opcion.isdigit():
            indice = int(opcion) - 1
            if 0 <= indice < 25 and self.centro.nombres_servidores[indice]:
                return self.centro.nombres_servidores[indice]
            else:
                print("Número de servidor inválido")
                return None
        else:
            return opcion
    
    def _mostrar_datos_servidor(self, nombre_servidor):
        """
        Muestra los datos detallados de un servidor específico
        
        Args:
            nombre_servidor: Nombre del servidor a consultar
        """
        datos = self.centro.obtener_datos_servidor(nombre_servidor)
        
        if datos is not None:
            print(f"\nDatos de {nombre_servidor}:")
            print("-" * 40)
            for dia in range(30):
                print(f"Día {dia+1:2d}: {datos[dia]:6.2f}%")
            
            # Calcular estadísticas
            promedio = self.centro.calculadora.calcular_promedio(datos)
            estadisticas = self.centro.calculadora.calcular_estadisticas(datos)
            
            print(f"\nEstadísticas de {nombre_servidor}:")
            print(f"Promedio: {promedio:.2f}%")
            print(f"Máximo: {estadisticas['maximo']:.2f}% (Día {estadisticas['indice_maximo']+1})")
            print(f"Mínimo: {estadisticas['minimo']:.2f}% (Día {estadisticas['indice_minimo']+1})")
        else:
            print(f"No se encontró el servidor '{nombre_servidor}'")
    
    def _mostrar_datos_dia(self, dia):
        """
        Muestra los datos de todos los servidores en un día específico
        
        Args:
            dia: Día a consultar (1-30)
        """
        datos = self.centro.obtener_datos_dia(dia)
        
        if datos is not None:
            print(f"\nDatos del día {dia} de junio:")
            print("-" * 40)
            
            for i in range(25):
                if self.centro.nombres_servidores[i]:
                    print(f"{self.centro.nombres_servidores[i]:<15}: {datos[i]:6.2f}%")
            
            # Calcular estadísticas del día
            suma_total = self.centro.calculadora.calcular_suma(datos)
            promedio_dia = self.centro.calculadora.calcular_promedio(datos)
            estadisticas = self.centro.calculadora.calcular_estadisticas(datos)
            
            print(f"\nEstadísticas del día {dia}:")
            print(f"Suma total: {suma_total:.2f}%")
            print(f"Promedio: {promedio_dia:.2f}%")
            print(f"Servidor con mayor uso: {self.centro.nombres_servidores[estadisticas['indice_maximo']]} ({estadisticas['maximo']:.2f}%)")
            print(f"Servidor con menor uso: {self.centro.nombres_servidores[estadisticas['indice_minimo']]} ({estadisticas['minimo']:.2f}%)")
        else:
            print("Error al obtener los datos del día")
