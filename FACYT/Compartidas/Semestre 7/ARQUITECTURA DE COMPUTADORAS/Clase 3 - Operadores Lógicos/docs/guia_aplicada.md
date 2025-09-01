## Guía de Aplicación de Conceptos

### 1. Análisis de Tablas de Verdad

Para analizar una compuerta, lo primero es construir o leer su tabla de verdad. Por ejemplo, para una **compuerta AND** de dos entradas (A y B), la tabla de verdad es:

|A|B|X|
|---|---|---|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

Exportar a Hojas de cálculo

Si necesitas entender el comportamiento de un circuito, puedes crear una tabla de verdad para cada compuerta y luego combinar los resultados para obtener la salida final.

### 2. Funcionamiento con Trenes de Impulsos

Los **trenes de impulsos** son señales que varían entre ALTO y BAJO con el tiempo. Para determinar la forma de onda de salida de una compuerta, debes analizar el estado de sus entradas en cada momento.

Por ejemplo, con una compuerta OR de dos entradas (A y B):

- Si A = BAJO y B = BAJO, la salida X es BAJA.
    
- En cualquier otro caso (A=ALTO o B=ALTO o ambas en ALTO), la salida X es ALTA.
    

Puedes trazar la forma de onda de la salida superponiendo las entradas en un diagrama de tiempo y aplicando la regla de la compuerta en cada instante.

### 3. Estados Activos y Polaridad

El pequeño círculo en los símbolos lógicos es crucial.

- **Círculo en la entrada:** La entrada es **activa a nivel BAJO**. Esto significa que la compuerta se activa cuando la señal en esa entrada es 0.
    
- **Círculo en la salida:** La salida es **activa a nivel BAJO**. La salida es 0 cuando la compuerta está en su estado "verdadero" o activado.
    
- **Sin círculo:** El terminal es **activo a nivel ALTO**. Se activa con un 1.
    

Este concepto es importante para entender cómo funcionan los circuitos, ya que un mismo símbolo puede tener diferentes "estados activos" dependiendo de la presencia del círculo.