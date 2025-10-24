# Trivia de Fórmula 1
# Contexto
La Fórmula 1 es de los deportes más populares a nivel mundial. 
Muchos aficionados disfrutan no solo de verlas carreras sino también poner a prueba 
sus conocimientos sobre el deporte. (pilotos, escuderías, historia).

Este proyecto será un juego de preguntas tipo trivial sobre Fórmula 1 que permite que 
el jugador/usuario responda dichas preguntas. El programa de Python, tendrá preguntas de opción múltiple, 
validará las respuestas del jugador/usuario, calculará su puntaje final y le dirá si es 
un verdadero aficionado dependiendo del puntaje final.


# ¿Por qué es interesante?
Este proyecto combina mi gusto por la Fórmula 1 con la programación.
Me permite aplicar de manera práctica los conocimientos vistos en clase, 
tales como: estructuras condicionales, ciclos, funciones, listas, listas anidadas,
operadores aritméticos y manejo del módulo random. 
Y el 26 de Octubre, justo se llevará a cabo el Gran Premio de la Ciudad de México.

# Algoritmo
      Inicio:
      
      Mostrar mensaje de bienvenida (print())
      
      Definir datos:
      
      Crear una lista anidada con las preguntas, opciones y la respuesta correcta
      
      Inicializar la variable score = 0
      
      Ciclo principal (for):
      
      Mostrar cada pregunta y sus opciones
      
      Pedir respuesta al usuario (input())
      
      Validar si la respuesta es correcta o no con if y else
      
      Sumar 1 punto al score si acierta
      
      Calcular calificación:
      
      Usar operadores aritméticos (/ y *) para obtener el porcentaje total
      
      Mostrar resultado:
      
      Usar estructuras condicionales (if, elif, else) para mostrar un mensaje personalizado según el puntaje
      
      Repetición del juego:
      
      Con un ciclo while, preguntar si el usuario desea volver a jugar
      
      Si responde “sí”, el juego se reinicia con las preguntas en orden aleatorio usando random.shuffle()
      
      Fin del programa:
      
      Mostrar un mensaje de despedida
      
# Biblioteca random y referencias al API de Python
random.shuffle()

Utilizada para cambiar el orden de las preguntas en cada partida.

Referencia oficial: https://docs.python.org/3/library/random.html#random.shuffle

# Instrucciones 
Descargar el archivo y correrlo en terminal o Thony
      F1TRIVA.py
Responder a las preguntas que aparecen.
Y recibe las noticias sobre tu afición de la F1.

Gracias!


