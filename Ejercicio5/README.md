# Ejercicio5

Análisis de Complejidad
Complejidad del tiempo:O(N). Ya que uno tiene que visitar cada nodo, donde NN es un número de nodos.

Complejidad espacial: O(N). En el caso del árbol degenerativo (donde el árbol tiene la forma de una lista enlazada), todos los nodos estarán en la pila de tiempo de ejecución mientras se procesa el nodo más profundo. Si el árbol está equilibrado, la complejidad del espacio estará más cerca de O(logN), pero recuerda que para los propósitos del análisis de complejidad, consideramos principalmente el peor de los casos.

Solución Gráfica.

<img src =  'img\1.png' style = 'center'><br>

<img src =  'img\2.png' style = 'center'><br>

<img src =  'img\3.png' style = 'center'><br>

Recorramos ambos árboles en paralelo y, una vez que se identifique el nodo de destino en el primer árbol, devolvamos el nodo correspondiente del segundo árbol.
Hay dos formas de atravesar el árbol: búsqueda primero en profundidad DFS y búsqueda primero en amplitud BFS.

Ambos comienzan desde la raíz y bajan, ambos usan estructuras adicionales, ¿cuál es la diferencia? Así es como se ve a gran escala: BFS atraviesa nivel por nivel, y DFS primero va a las hojas.

<img src =  'img\4.png' style = 'center'><br>
