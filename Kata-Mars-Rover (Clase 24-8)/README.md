# Kata Mars Rover — TDD en mob programming

**<u>Grupo 12:</u>**

- Esteban Karlen Aguirre
- Gabriel Perlin
- Mateo Spertino
- Tomas Sanchez Machado

**<u>Cambio que nos tocó:</u>**

**Salto**. Aparece el comando X: avanza dos celdas de una, salteando lo que haya en el medio. Si el destino está ocupado por un obstáculo, no salta y se comporta como si hubiera chocado.

**<u>Cómo lo absorberíamos:</u>**

Tocaríamos rover.py, agregando 2 funciones nuevas una que detecte si hay un obstáculo en una posición dada. Una función saltar() que calcule la celda dos lugares adelante y si está ocupada, se comporte como un choque si no, mueve al rover ahí directo.

**<u>Implementación real (post-clase):</u>**

La consigna pedía no implementarlo por falta de tiempo, pero terminamos de refactorizar el paso 3 antes de que terminara la clase, así que lo hicimos igual, siguiendo el ciclo RED → GREEN → REFACTOR completo.

En vez de dos funciones independientes como planteamos arriba, terminamos unificando `mover_adelante()` y `saltar()` en un solo método privado `_mover(pasos)`, que calcula el desplazamiento según la orientación (reusando la misma lógica de índices que ya usábamos en `girar_izquierda`/`girar_derecha`) y lo multiplica por la cantidad de pasos (1 para avanzar, 2 para saltar). Antes de mover al rover, chequea si la celda destino está en `self.obstaculos`; si lo está, no lo mueve, simulando el choque.
