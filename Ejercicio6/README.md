# Ejercicio6

Complejidad temporal: O(n + m)O(n+m)<br>
Complejidad Espacial: O(n + m)O(n+m)<br>

Solución Gráfica.<br>
<img src="img\1.jpg" style="float: right">
<img src="img\2.jpg" style="float: left">

Si no está muy familiarizado con el cruce de BFS, le sugerimos que lea nuestra Tarjeta de exploración de Leetcode y tenga algunos conocimientos de antemano.

En BFS, exploramos los nodos en el orden de su profundidad. Suponiendo que el nodo inicial tiene una profundidad de 0, exploraremos todos los nodos en la profundidad actual (d) antes de pasar a todos los nodos en la siguiente profundidad (d + 1).

Aquí hay un ejemplo del orden en el que visitamos los nodos usando BFS, el nodo inicial está coloreado en rojo y tiene una profundidad de 0. Los números representan la profundidad de cada nodo. Independientemente de la estructura específica, siempre visitamos el nodo de profundidad = 0, luego todos los nodos de profundidad = 1, todos los nodos de profundidad = 2 y así sucesivamente.
<img src="img\3.jpg" style="float: center"><br>

Volviendo a este problema, comenzamos con el origen del nodo con profundidad = 0, luego marcamos todos sus nodos vecinos no visitados con profundidad = 1 para ser visitados pronto, una vez que visitamos un nodo con profundidad = 1, marcamos todos sus nodos vecinos no visitados con profundidad = 2 también.

Podemos usar una cola cola como contenedor para almacenar todos los nodos a visitar sin mezclar el orden. Dado que la operación en la cola se realiza en el orden Primero en entrar, Primero en salir (FIFO), nos permite explorar todos los nodos con la profundidad actual, antes de pasar a los nodos con mayor profundidad.

Una vez que agregamos un nodo a la cola, lo marcamos inmediatamente como visitado para evitar que otros nodos lo agreguen nuevamente a la cola más adelante.

Si encontramos el destino del nodo durante el proceso, significa que existe una ruta desde el origen hasta el destino. De lo contrario, indica que no podemos encontrar ese camino.
<img src="img\4.jpg" style="float: center"><br>

Como se muestra en la figura anterior, el nodo 0 se visita mientras que el nodo 5 no se visita. Por lo tanto, no hay un camino de 0 a 5.<br>
Link de GitHub: https://github.com/Data-Structures-AYDA/Ejercicio6
