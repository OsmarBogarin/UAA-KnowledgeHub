## Conceptos Clave de Lógica Digital

### 1. Variables y Niveles Lógicos

En el álgebra booleana, las variables solo pueden tener dos valores:

- **0 lógico:** Representa un estado **BAJO** (Low), **Falso** (False) o **Apagado** (Off).
    
- **1 lógico:** Representa un estado **ALTO** (High), **Verdadero** (True) o **Encendido** (On).
    

Estos valores corresponden a rangos de voltaje específicos en un circuito electrónico. Por ejemplo, en algunos sistemas, 0-0.8V podría ser un 0 lógico y 2-5V un 1 lógico.

### 2. Tabla de Verdad

Una **tabla de verdad** es una herramienta fundamental que describe el comportamiento de una compuerta lógica. Enumera todas las posibles combinaciones de entradas y la salida correspondiente.

### 3. Compuertas Lógicas

Las compuertas lógicas son los bloques de construcción de los circuitos digitales.

- **Compuerta AND:** La salida **X** es **ALTA** (1) **solo si todas las entradas son ALTAS** (1).
    
- **Compuerta OR:** La salida **X** es **ALTA** (1) **si al menos una de sus entradas es ALTA** (1). La salida es BAJA (0) solo cuando todas sus entradas son BAJAS (0).
    
- **Compuerta NAND:** La salida **X** es **BAJA** (0) **solo si todas las entradas son ALTAS** (1). Es la negación de la compuerta AND.
    
- **Compuerta NOR:** La salida **X** es **ALTA** (1) **solo si todas las entradas son BAJAS** (0). Es la negación de la compuerta OR.
    
- **Compuerta XOR (OR Exclusiva):** La salida **X** es **ALTA** (1) **solo si las dos entradas están a niveles lógicos opuestos**. Si ambas entradas son iguales (0-0 o 1-1), la salida es BAJA (0).
    

### 4. Simbología Lógica

Los símbolos de las compuertas lógicas están estandarizados (por ejemplo, **ANSI/IEEE 91-1984**). Un círculo pequeño en una entrada o salida (llamado **indicador de polaridad**) significa que ese terminal es **activo a nivel BAJO**. Si no hay círculo, el terminal es **activo a nivel ALTO**.