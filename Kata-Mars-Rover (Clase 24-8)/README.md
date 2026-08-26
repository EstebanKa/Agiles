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
