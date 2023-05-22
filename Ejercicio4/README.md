# Ejercicio4

Solución Gráfica.
<img src= 'img\1.png'>
<img src= 'img\2.png'>
Tenga en cuenta que normalmente podría haber varias rutas para conectar los nodos en un gráfico. Sin embargo, en nuestro caso, dado que el gráfico de entrada puede formar un árbol desde cualquier nodo, como se especifica en el problema, sólo podría haber una ruta entre dos nodos cualesquiera. Además, no habría ningún ciclo en el gráfico. Como resultado, no habría ambigüedad en la definición anterior de distancia.

La altura de un árbol se puede definir como la distancia máxima entre la raíz y todos los nudos de sus hojas.
Con las definiciones anteriores, podemos reformular el problema cómo encontrar los nodos que en general están cerca de todos los demás nodos, especialmente los nodos hoja.
<img src= 'img\3.png'>
Por ejemplo, en el gráfico anterior, está claro que el nodo con el valor 1 es el centroide del gráfico. Si elegimos el nodo 1 como raíz para formar un árbol, obtendríamos un árbol con la altura mínima, en comparación con otros árboles que se forman con cualquier otro nodo.
Antes de continuar, aquí hacemos una afirmación que es esencial para el algoritmo.
Para el gráfico similar a un árbol, el número de centroides no es más de 2.
Si los nodos forman una cadena, es intuitivo ver que se cumple la declaración anterior, que se puede dividir en los siguientes dos casos:
Si el número de nodos es par, entonces habría dos centroides.
Si el número de nodos es impar, entonces solo habría un centroide.
<img src= 'img\4.png'>
Para el resto de los casos, podríamos probar por contradicción. Supongamos que tenemos 3 centroides en el gráfico, si eliminamos todos los nodos que no son centroides en el gráfico, entonces los 3 nodos centroides deben formar un triángulo, de la siguiente manera:
<img src= 'img\5.png'>
Debido a que estos centroides son igualmente importantes entre sí, y también deberían estar igualmente cerca entre sí. Si falta alguno de los bordes del triángulo, los 3 centroides se reducirían a un solo centroide.
Sin embargo, la forma del triángulo forma un ciclo que se contradice con la condición de que no hay ciclo en nuestro gráfico de árbol. De manera similar, para cualquiera de los casos que tengan más de 2 centroides, estos deben formar un ciclo entre los centroides, lo cual se contradice con nuestra condición.
