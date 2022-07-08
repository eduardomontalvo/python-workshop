# Python Workshop
## Introducción
El objetivo del taller es conocer el lenguaje python para desarrollar aplicaciones web. Si bien es cierto, el proyecto final contiene tecnologías fronted, nuestro enfásis será en las buenas prácticas del desarrollo del lado del servidor, también llamado **desarrolo backend**.

Los temas a abordar en el taller son los siguientes:
* Python como lenguaje de programación
* Sintáxis Básica de Python
* Módulos y paquetes
* Conocimientos de la Biblioteca Estándar
* Programación Orientada a Objetos
* APIs REST (http, verbos, json, seguridad, etc)
* Bases de datos y ORMs
* Algunos patrones de diseño y de arquitectura

![Python](https://www.python.org/static/img/python-logo.png)

**Python** es un lenguaje de programación de alto nivel (esto significa que es más cercano a nosotros: usando lenguaje humano, que a las máquinas que usan ceros y unos) que sirve para desarrollar muchos tipos de aplicaciones: desde aplicaciones web, hasta bots inteligentes de whatsapp. Sumamente poderoso y escalable, fue creado a finales de los años 80's por [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum). A pesar de que podamos pensar que al buen Guido le gustan los reptiles, no lo nombra así por las serpientes, lo nombra así pues es fanático de los humoristas británicos [Monty Python](https://es.wikipedia.org/wiki/Monty_Python).

Para conocer más de sus características y de su historia da click en el siguiente enlace: [¿Qué es python y porque debo aprenderlo?](https://www.miramar.dev/que-es-python-y-porque-debo-aprenderlo/)

Algunas de las características más importantes son:
* Sintaxis Legible.
* Fácil de aprender y de enseñar.
* Multiplataforma.
* Multiparadigma.

## Sintáxis Básica
```python
# Comentarios de una línea

"""
Cadenas de texto de varias lineas que pueden 
ser ocupados como comentarios en el 
código
"""

####################################################
## 1. Tipos de datos y operadores.
####################################################

# Para iniciar puedes escribir python en tu terminal y escribir
print("hola mundo") # Ese hola mundo, es un texto

# También puedes usarlo como una calculadora, pues soporta números y sus matemáticas:
1231 + 1231
824 - 341
103 * 32

# Valores 'boolean' => Los que contestan preguntas con si o no
True
False

# Igual a es ==
1 == 1  # => True
2 == 1  # => False

####################################################
## 2. Variables y Colecciones
####################################################

# La convención es usar guiones_bajos_con_minúsculas
coffee_price = 5    

# Listas almacena items en su interior
lista = []

# También existen diccionarios
diccionario = {}

# Y tuplas
tupla = (,)

####################################################
## 3. Control de Flujo
####################################################

# if: Para preguntar si algo es verdadero o falso"
if person > 18:
    print("Mayor de Edad")
else:
    print("No es mayor de edad")

# For: Para recorrer items dentro de alguna lista, diccionario, tupla, etc
for animal in ["perro", "gato", "raton"]:
    print("{} es un mamifero".format(animal))

# While: para recorrer mientras una condición se cumple.
x = 0
while x < 4:
    print(x)
    x += 1

####################################################
## 4. Funciones
####################################################

# Usa 'def' para crear nuevas funcionalidas en tu código y no repetir el mismo
def greetings(name):
    print("Hola {}".format(name))

# Usa return para devolver el resultado de tu función:
def add(a, b):
    return a + b
```
Para conocer más sintáxis del lenguaje visita: 
* Como check rápido: [Python Learn X in Y Minutes](https://learnxinyminutes.com/docs/es-es/python-es/)
* Para cuando tengas más tiempo: [Referencia a la sintáxis de Python](https://docs.python.org/3/reference/)

## Primer Ejercicio
> Escribir un programa que muestre en pantalla los números del 1 al 100, sustituyendo los múltiplos de 3 por la palabra “fizz”, los múltiplos de 5 por “buzz” y los múltiplos de ambos, es decir, los múltiplos de 3 y 5 (o de 15), por la palabra “fizzbuzz”.

1. En la primera iteración del código: usar range para que nos de los números del 1 al 100 e imprimir los resultados en consola.
2. Convertir el código en una función y mandarla llamar
3. Permitir que el código itere sobre cualquier lista que se envíada como parámetro a la función

Ver respuesta [aqui](src/fizzbuzz.py)

