"""
Trivia de Fórmula 1 

Este es un programa que crea un juego de preguntas tipo trivia sobre la Fórmula 1.
El jugador/usuario debe responder preguntas de opción múltiple.
Al final se calcula su puntaje y se muestra un mensaje según su desempeño.

"""
# Importamos el módulo random para generar aleatoriedad
import random 
 
"""
================== funcion para las preguntas  ====================
"""
def las_preguntas(pregunta, opciones, respuesta_correcta):
    print(pregunta)
    
    """
    Muestra una pregunta con sus opciones, pide respuesta al usuario
    y devuelve internamente 1 si es correcta o 0 si es incorrecta.
    """
    
    # Ciclo for para mostrar opcines de respuesta
    for opcion in opciones:
        print(opcion)
    # Pide respuesta al usuario
    respuesta = input(" \n Tu respuesta: ")
    

    # Ciclos while: verifica si la respuesta sea valida
    while respuesta.lower() not in ["a","b","c","d"]:
        print("Respuesta no valida, intenta de nuevo")
        respuesta = input("Tu respuesta: ")
        
    # Estructura de decisión (if-else), compara las respuesta       
    if respuesta.lower() == respuesta_correcta:
        return 1    
    else:
        return 0
   
"""
================= funcion principal de la trivia ====================
"""

def jugar():
    """
    Función principal:
    - Muestra las preguntas en orden aleatoreo
    - Calcula la calificaón final
    - Muestra un mensaje según el resultado
    
    dato, proceso, salida y que se usa para hacerlo 
    """
    # Acumulador de puntos 
    score = 0 
    print("Bienvenido a la F1 TRIVIA \n")

    # Lista anidada para las preguntas, sub-listas para opcion y respuesta
    preguntas = [
        ["\n¿Quién tiene más campeonatos mundiales de Fórmula 1?",
         ["a) Lewis Hamilton", "b) Michael Schumacher", "c) Max Verstappen", 
          "d) Ayrton Senna"],
         "b"],
        
        ["\n¿En qué año se celebró el primer campeonato oficial de Fórmula 1?",
         ["a) 1946", "b) 1950", "c) 1955", "d) 1960"], "b"],
        
        ["\n¿Qué escudería es conocida como 'La Scuderia'?",
         ["a) Mercedes", "b) Ferrari", "c) Red Bull", "d) McLaren"], "b"],
        
        ["\n¿Qué piloto español ganó el Mundial en 2005 y 2006?",
         ["a) Fernando Alonso", "b) Carlos Sainz", "c) Pedro de la Rosa", 
          "d) Marc Gené"], "a"],
        
        ["\n¿En qué circuito se corre el Gran Premio de Mónaco?",
         ["a) Silverstone", "b) Monza", "c) Monte Carlo", 
          "d) Spa-Francorchamps"],"c"],
        
        ["\n¿Cuál es el color principal del equipo Red Bull Racing?",
         ["a) Azul", "b) Rojo", "c) Negro", "d) Amarillo"], "a"],
        
        ["\n¿Qué país alberga el circuito de Suzuka?",
         ["a) China", "b) Japón", "c) Corea del Sur", "d) Tailandia"], "b"],
        
        ["\n¿Cuál es el apodo del piloto Charles Leclerc?",
         ["a) The Prince of Monaco", "b) The Ice Man", "c) Mad Max", 
          "d) The Honey Badger"], "a"],
        
        ["\n¿Qué neumáticos fabrica la Fórmula 1 actualmente?",
         ["a) Bridgestone", "b) Michelin", "c) Goodyear", "d) Pirelli"], "d"],
        
        ["\n¿Cuál de estos circuitos es el más rápido del calendario?",
         ["a) Spa-Francorchamps", "b) Monza", "c) Silverstone", "d) Baku"],"b"]
    ]
    
    """
    Uso del módulo random y de la función shuffle():
    random.shuffle(lista) mezcla  elementos de una lista de manera aleatoria.
    En este caso las preguntas se mostrarán en un orden distinto
    cada vez que el jugador desida jugar,
    """
    
    random.shuffle(preguntas)

    # Ciclo for para recorrer la lista anidada de preguntas y sus sub-listas
    for pregunta, opciones, respuesta_correcta in preguntas:
        score += las_preguntas(pregunta, opciones, respuesta_correcta)
    
    # Operador aritmético (/ y *) con listas, calcula la calificación final 
    total_preguntas = len(preguntas)
    calificacion = (score / total_preguntas) * 100
    print("\nSacaste: ", calificacion, "/100")

    # Operadores relacionales (==, >=)
    # Estructura de decisión (if - elif - else)
    if calificacion == 100:
        print("Eres un experto en F1!")
    elif calificacion >= 50:
        print("Sigue la pista, vas en buen camino!")
    else:
        print("Necesitas más practicas, pero no te preocupes, cada gp hay 3!")

"""
=============== Ciclo principal para repetir la trivia  =================
"""
 # Estructura de decisión/repaticion de listas
jugar_again = "si"

# Ciclo while permite al usuario volver a jugae
while jugar_again == "si":
    jugar()
    jugar_again = input("\nQuieres jugar de nuevo? (si/no): ")

print("Gracias por participar ")
