# Tree Algorithms Compression Correction Huffman and Hamming
# Algoritmos de Árboles: Compresión y Corrección usando Huffman y Hamming

## Universidad Autónoma de Yucatán

### Maestría en Ciencias de la Computación

Matemáticas Discretas Proyecto Final

### Autores

* Dayan Bravo
* Mario Herrera

## Descripción general del sistema

### Objetivo

El objetivo de este sistema es leer archivos de texto y conviertir su contenido en un archivo binario comprimido utilizando el método de Huffman.
Luego tomar este archivo binario y codificarlo utilizando el método de Hamming lo que permite transmitir la información de un lugar a otro y corregir aquellos errores que puedan surgir por el camino. 
Para introducir errores en el archivo binario creado por el algoritmo de Hamming se utiliza una función que aleatoriamente modifica un bit en algunos conjuntos de 8 bits. 
De esta forma se puede probar que el algoritmo funciona correctamente.
El proceso paso a paso sería como se describe a continuación:

1. Leer un archivo de texto.
2. Construir una tabla de frecuencias para los caracteres existentes en el texto leído.
3. Construir un árbol binario que permita convertir cadenas binarias en caracteres.
4. Generar cadenas binarias de 8 bits que representen el contenido del texto leído.
5. Codificar estas cadenas en grupos de 4 bits de información y añadiendo 3 bits de pariedad.
6. Añadir errores aleatorios al archivo binario que contiene el texto codificado.
7. Enviar el archivo con errores de una lugar a otro.
8. Recibir el archivo con errores.
9. Corregir los errores existentes archivando la ubicación en que se encontró cada error.
10. Decodificar el archivo para obtener nuevamente su forma comprimida.
11. Descomprimir el archivo para obtener el texto original.

### Documentación Técnica

#### Clase Tree ####

La clase Tree contiene la estructura básica de un árbol binario, el cual tiene su propio _data_ que permite almacenar
información en el nodo, contiene además un nodo izquierdo y un nodo derecho que representan a los hijos izquierdo y 
derecho del nodo respectivamenten.

#### Clase TreeObject ####

La clase TreeObject representa la _data_ dentro de un nodo Tree.

#### Clase FileManager ####

La clase FileManager gestiona todas las funcionalidades relacionadas con leer o escribir ficheros. Los métodos que 
contiene son los siguientes:

* **write_txt:** Permite almacenar en un archivo el texto deseado.
* **read_txt:** Permite leer un archivo de texto y almacenarlo en una variable para ser procesado posteriormente.
* **write_bin:** Genera un archivo binario a partir del código en forma de texto.
* **read_bin:** Lee un archivo binario y lo traduce a texto.

#### Clase FrequencyCalculator ####

La clase FrequencyCalculator contiene los métodos que permiten gestionar la frecuencia con que aparecen cada uno de
los caracteres en el archivo de texto que sirve como entrada para todo el proceso que realiza este sistema. Los métodos 
que contiene son los siguientes:

* **count_symbols:** Permite contar la cantidad de veces que aparece cada símbolo en el archivo de texto leído.
* **frequency_symbols:** Crea un diccionario que contiene cada caracter perteneciente al archivo leído con su frecuencia asociada.
* **export_json_frequency:** Exporta el diccionario que contiene los caracteres con su frecuencia a un archivo de tipo json.
* **import_json_frequency:** Importa el diccionario que contiene los caracteres con su frecuencia desde un archivo de tipo json.

#### Clase SymbolMapper ####

Esta es una clase auxiliar para gestionar algunos símbolos utilizados en los archivos json.

#### Clase Code ####

Esta clase gestiona todo lo  relacionado con las operaciones que se pueden realizar sobre un código o fregmento de 
código. Los métodos que contiene son:

* **extract:** Extrae una cantidad determinada de bits menos significativos de un código.
* **concat_zero:** 
* **concat_one:** 
* **concat_zero_init:** 
* **concat_one_init:** 
* **concat_init:** 
* **complete_byte:** Añade bits hasta alcanzar una longitud de 8 bits en unacadena cuando no hay suficientes bits para completarla con bits de información.
* **get_code_from_string:** Permite obtener el código de un texto.

#### Clase Huffman ####

Esta es la clase principal para la parte de convertir un archivo de texto a un archivo binario comprimido. Los métodos 
que contiene son los siguientes: 

* **generate_tree:** Genera el árbol que permite convertir un símbolo de texto a una cadena de ceros y unos o viceversa. 
* **generate_code:** Genera el diccionario que contiene todas las representaciones en binario de los caracteres extraídos del texto.
* **__generate_code_recursive:** Este método recorre el árbol generado por _generate_tree_ de manera recursiva sirviendo como apoyo al método _generate_code_.
* **encode:** Convierte una cadena de símbolos en formato de texto a una cadena en formato binario.
* **decode:** Convierte una cadena en formato binario a una cadena de símbolos en formato de texto.
* **export_json_codes:** Exporta el diccionario que contiene la representación de cada símbolo en formato binario a un archivo de tipo json.
* **export_json_tree:** Exporta el árbol a un archivo de tipo json.
* **__export_json_tree_recursive:** Método auxiliar que apoya al método _export_json_tree_ para exportar el árbol a un archivo de tipo json.

## Un ejemplo sencillo

