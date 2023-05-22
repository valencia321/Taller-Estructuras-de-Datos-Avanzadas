# Ejercicio3

Complejidad temporal: O(n)<br>
Complejidad Espacial: O(n)<br>

Solución Gráfica.<br>
<img src="img\1.jpg"><br>
<img src="img\2.jpg"><br>

A primera vista, el problema es trivial. Recorrimos el árbol y verificamos en cada paso si node.right.val > node.val y node.left.val < node.val. Este enfoque incluso funciona para algunos árboles.

<img src="img\3.jpg"><br>

El problema es que este enfoque no funcionará para todos los casos. No solo el hijo derecho debe ser más grande que el nodo, sino todos los elementos en el subárbol derecho. Aquí hay un ejemplo :
<img src="img\4.jpg"><br>

Eso significa que uno debe mantener los límites superior e inferior para cada nodo al atravesar el árbol, y comparar el valor del nodo no con los valores de los hijos sino con estos límites.
Link de GitHub: https://github.com/Data-Structures-AYDA/Ejercicio3
