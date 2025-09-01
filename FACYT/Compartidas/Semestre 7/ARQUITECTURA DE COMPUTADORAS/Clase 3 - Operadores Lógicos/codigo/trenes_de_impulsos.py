import matplotlib.pyplot as plt
import numpy as np

# Para un ejemplo podrias varias con las siguientes combinaciones:
# Entrada A: 0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0
# Entrada B: 0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0
# Entrada C: 1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0
# Entrada A2: 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
# Entrada A3: 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1

def operacion_logica(operador, *entradas):
    """
    Aplica la operación lógica especificada a las entradas.
    
    Args:
        operador (str): Tipo de operación ('and', 'or', 'nand', 'nor', 'xor', 'xnor')
        *entradas: Arrays de valores binarios (0 y 1)
    
    Returns:
        list: Resultado de la operación lógica
    """
    longitud = len(entradas[0])
    salida = []
    
    for i in range(longitud):
        valores = [entrada[i] for entrada in entradas]
        
        if operador.lower() == 'and':
            resultado = all(valores)
        elif operador.lower() == 'or':
            resultado = any(valores)
        elif operador.lower() == 'nand':
            resultado = not all(valores)
        elif operador.lower() == 'nor':
            resultado = not any(valores)
        elif operador.lower() == 'xor':
            resultado = sum(valores) % 2 == 1
        elif operador.lower() == 'xnor':
            resultado = sum(valores) % 2 == 0
        else:
            raise ValueError(f"Operador '{operador}' no reconocido")
        
        salida.append(int(resultado))
    
    return salida

def crear_entradas_desde_input():
    """
    Crea las entradas basándose en la configuración del usuario.
    
    Returns:
        tuple: (entradas, nombres_entradas, operador)
    """
    print("=== CONFIGURACIÓN DEL SIMULADOR DE COMPUERTAS LÓGICAS ===")
    
    # Número de entradas
    num_entradas = int(input("Número de entradas (2-5): "))
    if num_entradas < 2 or num_entradas > 5:
        print("Número de entradas debe estar entre 2 y 5. Usando 2.")
        num_entradas = 2
    
    # Longitud de los arrays
    longitud = int(input("Longitud de los arrays de entrada: "))
    
    # Operador lógico
    print("\nOperadores disponibles: AND, OR, NAND, NOR, XOR, XNOR")
    operador = input("Selecciona el operador lógico: ").strip()
    
    # Crear nombres de entradas
    nombres_entradas = []
    for i in range(num_entradas):
        nombres_entradas.append(chr(65 + i))  # A, B, C, D, E
    
    # Obtener valores de entrada
    entradas = []
    print(f"\nIngresa los valores para cada entrada ({longitud} valores separados por comas):")
    print("Ejemplo: 0,1,0,1,1,0")
    
    for i, nombre in enumerate(nombres_entradas):
        while True:
            try:
                valores_str = input(f"Entrada {nombre}: ")
                valores = [int(x.strip()) for x in valores_str.split(',')]
                
                if len(valores) != longitud:
                    print(f"Error: Debes ingresar exactamente {longitud} valores")
                    continue
                
                if not all(v in [0, 1] for v in valores):
                    print("Error: Solo se permiten valores 0 y 1")
                    continue
                
                entradas.append(valores)
                break
                
            except ValueError:
                print("Error: Formato inválido. Usa números 0 y 1 separados por comas")
    
    return entradas, nombres_entradas, operador

def mostrar_tabla_verdad(entradas, nombres_entradas, salida, operador):
    """
    Muestra la tabla de verdad en la consola.
    """
    print(f"\n=== TABLA DE VERDAD - COMPUERTA {operador.upper()} ===")
    
    # Encabezados
    header = " | ".join(nombres_entradas) + " | Salida"
    print(header)
    print("-" * len(header))
    
    # Filas de datos
    for i in range(len(entradas[0])):
        fila = " | ".join([f"  {entrada[i]}  " for entrada in entradas])
        fila += f" |   {salida[i]}"
        print(fila)

def crear_grafica(entradas, nombres_entradas, salida, operador):
    """
    Crea la gráfica de formas de onda.
    """
    longitud = len(entradas[0])
    tiempo = np.arange(longitud)
    num_entradas = len(entradas)
    
    # Crear subplots dinámicamente
    fig, axes = plt.subplots(num_entradas + 1, 1, sharex=True, 
                            figsize=(12, 2 + num_entradas * 1.5))
    
    # Si solo hay un subplot, convertir a lista para consistencia
    if num_entradas == 1:
        axes = [axes[0], axes[1]]
    
    # Colores para las entradas
    colores = ['red', 'green', 'orange', 'purple', 'brown']
    
    # Graficar entradas
    for i, (entrada, nombre, color) in enumerate(zip(entradas, nombres_entradas, colores)):
        axes[i].step(tiempo, entrada, where='post', color=color, linewidth=2)
        axes[i].set_ylabel(f'Entrada {nombre}', fontsize=10)
        axes[i].set_yticks([0, 1])
        axes[i].set_yticklabels(['BAJO', 'ALTO'])
        axes[i].grid(True, axis='y', linestyle='--', alpha=0.7)
        axes[i].set_ylim(-0.2, 1.2)
    
    # Graficar salida
    axes[-1].step(tiempo, salida, where='post', color='blue', linewidth=3)
    axes[-1].set_ylabel('Salida', fontsize=10)
    axes[-1].set_yticks([0, 1])
    axes[-1].set_yticklabels(['BAJO', 'ALTO'])
    axes[-1].grid(True, axis='y', linestyle='--', alpha=0.7)
    axes[-1].set_ylim(-0.2, 1.2)
    
    # Configuración final
    plt.xlabel('Tiempo', fontsize=12)
    
    # Crear título dinámico
    formula = crear_formula(nombres_entradas, operador)
    plt.suptitle(f'Compuerta {operador.upper()}: {formula}', fontsize=14, fontweight='bold')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def crear_formula(nombres_entradas, operador):
    """
    Crea la fórmula lógica para mostrar en el título.
    """
    if operador.lower() == 'and':
        simbolo = ' · '
    elif operador.lower() == 'or':
        simbolo = ' + '
    elif operador.lower() == 'nand':
        simbolo = ' · '
        return f"({simbolo.join(nombres_entradas)})'"
    elif operador.lower() == 'nor':
        simbolo = ' + '
        return f"({simbolo.join(nombres_entradas)})'"
    elif operador.lower() == 'xor':
        simbolo = ' ⊕ '
    elif operador.lower() == 'xnor':
        simbolo = ' ⊕ '
        return f"({simbolo.join(nombres_entradas)})'"
    else:
        simbolo = f' {operador.upper()} '
    
    return simbolo.join(nombres_entradas)

def main():
    """
    Función principal del programa.
    """
    try:
        # Configuración interactiva
        entradas, nombres_entradas, operador = crear_entradas_desde_input()
        
        # Calcular salida
        salida = operacion_logica(operador, *entradas)
        
        # Mostrar resultados
        print(f"\n=== RESULTADOS ===")
        for i, (entrada, nombre) in enumerate(zip(entradas, nombres_entradas)):
            print(f"Entrada {nombre}: {entrada}")
        print(f"Salida: {salida}")
        
        # Mostrar tabla de verdad
        mostrar_tabla_verdad(entradas, nombres_entradas, salida, operador)
        
        # Crear gráfica
        crear_grafica(entradas, nombres_entradas, salida, operador)
        
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo de uso rápido (descomenta para usar valores predefinidos)
def ejemplo_rapido():
    """
    Ejemplo rápido sin interacción del usuario.
    """
    # Configuración de ejemplo
    entrada_A = [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0]
    entrada_B = [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0]
    entrada_C = [1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0]
    
    entradas = [entrada_A, entrada_B, entrada_C]
    nombres_entradas = ['A', 'B', 'C']
    operador = 'OR'
    
    salida = operacion_logica(operador, *entradas)
    
    print("=== EJEMPLO RÁPIDO ===")
    mostrar_tabla_verdad(entradas, nombres_entradas, salida, operador)
    crear_grafica(entradas, nombres_entradas, salida, operador)

if __name__ == "__main__":
    print("1. Modo interactivo")
    print("2. Ejemplo rápido")
    
    modo = input("Selecciona el modo (1 o 2): ").strip()
    
    if modo == "2":
        ejemplo_rapido()
    else:
        main()
