
# SmartSpeaker: diseñar y proteger un objeto

## Parte 1. Análisis del problema

### 1.2. Problemas de la primera versión

1. **¿Qué ocurre cuando el nombre está vacío?** Se permite permite y el altavoz queda sin un nombre válido.
2. **¿Qué ocurre cuando el volumen es negativo?** Se guarda sin comprobaciones. No tiene sentido.
3. **¿Podemos asignar un texto al atributo `encendido`?** Sí, no se controla ese atributo
4. **¿Quién debe evitar estos valores?** La clase `Altavoz`, para que las reglas se cumplan siempre.
5. **¿Qué problemas causa modificar el estado directamente?** Almacenar valores incoherente, funcionamiento erroneo del objeto.

### 1.3. Reglas de negocio

| Elemento | Regla que debe cumplir | Ejemplo inválido |
| --- | --- | --- |
| Nombre | Ser una cadena de texto no vacía ni formada solo por espacios; eliminar espacios exteriores. | `"   "`, `""`, `27`     |
| Volumen | Ser un entero entre 0 y 100, ambos incluidos. | `-5`, `101`, `13.5` |
| Estado | Representar únicamente si el altavoz está encendido o apagado. | `"quizá"` |
| Encendido y apagado | El estado debe cambiarse a través de`encender()` y `apagar()`. | `altavoz.estado = "encendido"` |

## Parte 2. Diseño de la interfaz pública

### 2.1. Tabla de diseño

| Elemento | ¿Público o interno? | ¿Cómo debería utilizarse? |
| --- | --- | --- |
| Nombre del altavoz | Propiedad pública `nombre` y atributo interno `_nombre` | Consultarlo y modificarlo mediante una propiedad. |
| Volumen | Propiedad pública `volumen` y atributo interno `_volumen` | Consultarlo y modificarlo mediante una propiedad. |
| Estado de encendido | Propiedad pública de solo lectura `estado` y atributo interno `_encendido` | Consultarlo con `estado`, pero no asignarle valores directamente. |
| Operación para encender | Método público `encender()` | Llamar para cambiar el estado a encendido |
| Operación para apagar | Método público `apagar()` | Llamar para cambiar el estado a apagado. |

### 2.2. Justificación

- **Validación del volumen:** es necesaria para impedir valores que no son enteros o que están no están el 0 y el 100.
- **Control del estado:** no queremos que se cambie por una asignación directa porque debe modificarse mediante los métodos previstos para ello, para evitar estados erroneos.
- **Diferencia entre `_volumen` y `volumen`:** `_volumen` es el atributo interno donde se guarda el dato; `volumen` es la propiedad pública por la que se consulta o modifica aplicando las comprobaciones del setter.

## Parte 3. Implementación de la clase

La clase está implementada en `altavoz.py`.

- En el constructor `__init__`, `self.nombre = nombre` y `self.volumen = volumen` utilizan los setters y aplican la validación desde la creación del objeto.
- La propiedad `nombre` comprueba que el valor sea una cadena, elimina los espacios exteriores con `strip()` y rechaza cadenas vacías.
- La propiedad `volumen` rechaza valores que no sean exactamente de tipo `int` y números fuera del intervalo de 0 a 100.
- El atributo interno `_encendido` comienza con `False`. La propiedad `estado` devuelve `"apagado"` o `"encendido"` y no tiene setter público.
- Los métodos `encender()` y `apagar()` cambian el atributo `_encendido` a `True` y `False`, respectivamente.

El programa podrá consultar `altavoz.nombre`, `altavoz.volumen` y `altavoz.estado`, cambiar el volumen y utilizar los métodos para encender o apagar el altavoz, sin acceder normalmente a los atributos internos.

## Parte 4. Comprobación del comportamiento

Las pruebas se encuentran en el fichero`pruebas_manuales.py`. 

### 4.1. Resultados de las pruebas válidas

| ID | Resultado obtenido | ¿Coincide con el esperado? |
| --- | --- | --- |
| V01 | Se crea correctamente `Altavoz("Salón", 30)`. | Sí |
| V02 | El nombre es `"Salón"`. | Sí |
| V03 | El volumen es `30`. | Sí |
| V04 | El estado inicial es `"apagado"`. | Sí |
| V05 | Se acepta el volumen `50`. | Sí |
| V06 | Se acepta el volumen `0`. | Sí |
| V07 | Se acepta el volumen `100`. | Sí |
| V08 | Después de `encender()`, el estado es `"encendido"`. | Sí |
| V09 | Después de `apagar()`, el estado es `"apagado"`. | Sí |
| V10 | El nombre `"  Cocina  "` se almacena como `"Cocina"`. | Sí |

### 4.2. Resultados de las pruebas inválidas

| ID | Resultado obtenido | ¿Coincide con el esperado? |
| --- | --- | --- |
| I01 | Nombre `""`: `ValueError`. | Sí |
| I02 | Nombre `"   "`: `ValueError`. | Sí |
| I03 | Nombre `25`: `ValueError`. | Sí |
| I04 | Volumen `-1`: `ValueError`. | Sí |
| I05 | Volumen `101`: `ValueError`. | Sí |
| I06 | Asignación `altavoz.volumen = 25.5`: `ValueError`. | Sí |
| I07 | Asignación `altavoz.volumen = "alto"`: `ValueError`. | Sí |
| I08 | Asignación `altavoz.estado = "encendido"`: `AttributeError`. | Sí |

## Parte 5. IA como revisora del diseño

### 5.1. Recomendaciones analizadas

| Recomendación de la IA | ¿La acepto? | Justificación | ¿Cómo la he verificado? |
| --- | --- | --- | --- |
| Comprobar que los setters no provocan recursión. | Sí | Dentro de los setters se asigna a `_nombre` o `_volumen`, no a la misma propiedad pública; de este modo no se llama al setter repetidamente. | He revisado las asignaciones de los setters y ejecuté las pruebas de creación y modificación de volumen sin que se produzcan errores de recursión. |
| Comprobar que `True` y `False` no se aceptan como volúmenes. | Sí | La comprobación `type(volumen) is not int` del setter los rechaza. | Revisé la condición del setter y probé a crear altavoces con volumen `True` y `False`: ambos casos provocaron `ValueError`. |

### 5.2. Valoración

La IA me ha servido para revisar aspectos que pueden pasar desapercibidos, pero no he dado por válidas sus sugerencias sin contrastarlas.

## Parte 6. Una reflexión final: ¿qué ventajas tiene que la clase controle sus propias reglas?

Considero que es una ventaja que la propia clase controle sus reglas porque así se evitan datos incorrectos desde el principio. Las propiedades permiten consultar los valores y modificarlos de manera controlada, mientras que los métodos `encender()` y `apagar()` evitan cambiar directamente el estado. El código que utiliza la clase es más claro, más seguro y más fácil de mantener. También he comprobado que las pruebas nos muestran que el programa se comporta como se espera, tanto con valores válidos como inválidos.
