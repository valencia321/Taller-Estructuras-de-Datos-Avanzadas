# Ejercicio2

<img src= 'img\1.png'>

En el problema, se menciona claramente que tenemos que hacer el recorrido a través de la forma Inorder.

Primero entendamos qué es Inorder.

Atraviesa el subárbol izquierdo,
Visita la raíz.
Atraviesa el subárbol derecho,

→ Por ejemplo, cuando la entrada es [1,2,3,4,5] (como el gráfico a continuación)
La salida debe ser [4,2,5,1,3]


Vamos a entender cómo se calculará.

<img src= 'img\2.png'>

Primero, intentaremos atravesar el nodo izquierdo del árbol y agregar esos valores a la pila hasta que nos quedemos vacíos (NULL).

<img src= 'img\3.png'>

El último es.

<img src= 'img\4.png'>

Ahora, aquí en 4, si vamos a su lado izquierdo, nos quedaremos vacíos (NULL) ya que no hay ningún nodo a la izquierda de 4.

<img src= 'img\5.png'>

Ahora, como el nodo actual (4) no tiene ningún nodo izquierdo, pondremos el valor del nodo actual en la lista, eliminaremos los valores de la pila y agregaremos ese valor a la lista.

<img src= 'img\6.png'>

Ahora, verifique el lado derecho del nodo actual (que es 4), que también es nulo.

<img src= 'img\7.png'>

Ahora, extraemos el valor de la pila y lo agregamos a la lista.

<img src= 'img\8.png'>

Entonces, el resultado sería.

<img src= 'img\9.png'>

Ahora, verificaremos el lado derecho de 2, que es 5, colocaremos todos los nodos izquierdos del nodo actual (que es 5) en la pila, pero 5 no tiene nodos izquierdos. Ponemos el valor del nodo superior (es decir, 5) en la lista.

<img src= 'img\10.png'>

Compruebe el nodo derecho del nodo actual, que también es nulo.

<img src= 'img\11.png'>

Ahora, extraemos el valor de la pila y lo agregamos a la lista.

<img src= 'img\12.png'>

Ahora, verifique el lado derecho del nodo actual (1), que es 3.

<img src= 'img\13.png'>

Ahora, coloque todos los nodos izquierdos del nodo actual (que es 3) en la pila, pero 3 no tiene nodos izquierdos.

<img src= 'img\14.png'>

Ahora, el siguiente paso, agregaremos el valor del nodo actual a la lista.

<img src= 'img\15.png'>

Luego verifique todo el lado derecho del nodo actual, que también es nulo.

<img src= 'img\16.png'>

Después.

<img src= 'img\17.png'>

Aquí, tanto el nodo como la pila son nulos y están vacíos. No queda ningún nodo para agregar a la lista.

Complejidad del tiempo.
Aquí, estamos atravesando todos los nodos del árbol una vez, por lo que la complejidad del tiempo total es O(n).

Complejidad espacial.
Dado que hemos usado dos matrices adicionales como res y stack, la complejidad del espacio será O(2n) => O(n).
