"""
Controlador principal del sistema de análisis de CPU
Maneja el flujo del programa y coordina entre la interfaz y el modelo de datos
"""

from models.centro_datos import CentroDeDatos
from interface.interfaz_usuario import InterfazUsuario


class ControladorPrincipal:
    """
    Controlador que maneja el flujo principal del sistema
    """
    
    def __init__(self, archivo_datos="uso_cpu_junio.txt"):
        """
        Inicializa el controlador con el modelo y la vista
        
        Args:
            archivo_datos: Ruta al archivo de datos de CPU
        """
        self.centro_datos = CentroDeDatos()
        self.interfaz = InterfazUsuario(self.centro_datos)
        self.archivo_datos = archivo_datos
        self.ejecutando = True
    
    def iniciar_sistema(self):
        """
        Inicia el bucle principal del sistema
        """
        while self.ejecutando:
            try:
                self._ejecutar_ciclo_menu()
            except KeyboardInterrupt:
                self.interfaz.mostrar_cancelacion_usuario()
                break
            except Exception as e:
                self.interfaz.mostrar_error_inesperado(e)
            
            if self.ejecutando:
                self.interfaz.pausar_para_continuar()
    
    def _ejecutar_ciclo_menu(self):
        """Ejecuta un ciclo completo del menú principal"""
        self.interfaz.mostrar_menu_principal()
        opcion = self.interfaz.solicitar_opcion()
        self._procesar_opcion(opcion)
    
    def _procesar_opcion(self, opcion):
        """
        Procesa la opción seleccionada por el usuario
        
        Args:
            opcion: Opción seleccionada como string
        """
        opciones = {
            "0": self._salir_sistema,
            "1": self._cargar_datos,
            "2": self._mostrar_resumen,
            "3": self._calcular_promedios,
            "4": self._encontrar_dia_mayor_carga,
            "5": self._encontrar_servidor_menor_uso,
            "6": self._ejecutar_analisis_completo,
            "7": self._consultar_servidor,
            "8": self._consultar_dia
        }
        
        accion = opciones.get(opcion, self._opcion_invalida)
        accion()
    
    def _salir_sistema(self):
        """Termina la ejecución del sistema"""
        self.interfaz.mostrar_mensaje_salida()
        self.ejecutando = False
    
    def _cargar_datos(self):
        """Carga los datos desde el archivo"""
        self.interfaz.mostrar_mensaje_carga()
        self.centro_datos.cargar_datos(self.archivo_datos)
    
    def _mostrar_resumen(self):
        """Muestra el resumen de estadísticas"""
        self.centro_datos.mostrar_resumen_estadisticas()
    
    def _calcular_promedios(self):
        """Calcula y muestra los promedios mensuales por servidor"""
        self.centro_datos.calcular_promedio_mensual_por_servidor()
    
    def _encontrar_dia_mayor_carga(self):
        """Encuentra y muestra el día con mayor carga total"""
        self.centro_datos.encontrar_dia_mayor_carga()
    
    def _encontrar_servidor_menor_uso(self):
        """Encuentra y muestra el servidor con menor uso promedio"""
        self.centro_datos.encontrar_servidor_menor_uso()
    
    def _ejecutar_analisis_completo(self):
        """Ejecuta el análisis completo del sistema"""
        self.interfaz.ejecutar_analisis_completo()
    
    def _consultar_servidor(self):
        """Permite consultar datos de un servidor específico"""
        self.interfaz.consultar_servidor_especifico()
    
    def _consultar_dia(self):
        """Permite consultar datos de un día específico"""
        self.interfaz.consultar_dia_especifico()
    
    def _opcion_invalida(self):
        """Maneja las opciones inválidas"""
        self.interfaz.mostrar_opcion_invalida()


def ejecutar_sistema():
    """
    Función de entrada principal para ejecutar el sistema
    """
    controlador = ControladorPrincipal()
    controlador.iniciar_sistema()
