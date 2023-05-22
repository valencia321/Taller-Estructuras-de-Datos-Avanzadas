Análisis de Complejidad
Complejidad de tiempo: El preprocesamiento es O(N), donde N es el número de nodos en el árbol. Cada operación de inserción a partir de entonces es O(1)O(1).
Complejidad espacial: O(N) cuando el tamaño del árbol durante la operación de inserción actual.

Solución Gráfica.<br>
<img src="img\1.jpg"><br>

Considere todos los nodos numerados primero por nivel y luego de izquierda a derecha. Llame a esto el "orden numérico" de los nodos.

En cada paso de inserción, queremos insertar en el nodo con el número más bajo (que todavía tiene 0 o 1 hijos).

Al mantener una deque (cola de dos extremos) de estos nodos en orden numérico, podemos resolver el problema. Después de insertar un nodo, ese nodo ahora tiene el número más alto y no tiene hijos, por lo que va al final de la deque. Para obtener el nodo con el número más bajo, saltamos desde el principio del deque.

Link GitHub: https://github.com/valencia321/Taller-Estructuras-de-Datos-Avanzadas/tree/main/Ejercicio1

