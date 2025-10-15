# Importa el módulo para mezclar las preguntas 
import random  
 
"""
================== funcion para las preguntas  ====================
"""
def las_preguntas(pregunta, opciones, respuesta_correcta):
    print(pregunta)
    
    """
Muestra una pregunta y sus opciones, al igual que pide una respuesta al usuario,
e internamente devuekve un 1 si la respuesta es correcta o 0 si no
    """
    
    # Ciclo para mostrar opcines 
    for opcion in opciones:
        print(opcion)
    # Pide respuesta al usuario
    respuesta = input(" \n Tu respuesta: ")
    

    # Estructura de ciclos while: si el usuario pone algo no válido, se repite
    while respuesta.lower() not in ["a","b","c","d"]:
        print("Respuesta no valida, intenta de nuevo")
        respuesta = input("Tu respuesta: ")
        
    # Estructura de decisión (if-else), compara las respuesta       
    if respuesta.lower() == respuesta_correcta:
        return 1   # operador aritmético (+): suma puntos 
    else:
        return 0
   
"""
================== funcion principal de la trivia ====================
"""

def jugar():
    """
- Muestra las preguntas en orden aleatoreo
- Calcula la calificaón final
- Muestra un mensaje según el resultado
"""
    # Acumulador de puntos 
    score = 0 

    print("Bienvenido a la F1 TRIVIA \n")

    # Lista anidada para las preguntas 
    # lista simple para las opciones 
    preguntas = [
        
         
     #1
    ["\n¿Quién tiene más campeonatos mundiales de Fórmula 1?",
     ["a) Lewis Hamilton", "b) Michael Schumacher", "c) Max Verstappen", "d) Ayrton Senna"], "b"],
    
     #2
    ["\n¿En qué año se celebró el primer campeonato oficial de Fórmula 1?",
     ["a) 1946", "b) 1950", "c) 1955", "d) 1960"], "b"],
    
     #3
    ["\n¿Qué escudería es conocida como 'La Scuderia'?",
     ["a) Mercedes", "b) Ferrari", "c) Red Bull", "d) McLaren"], "b"],
    
     #4
    ["\n¿Qué piloto español ganó el Mundial en 2005 y 2006?",
     ["a) Fernando Alonso", "b) Carlos Sainz", "c) Pedro de la Rosa", "d) Marc Gené"], "a"],
    
     #5
    ["\n¿En qué circuito se corre el Gran Premio de Mónaco?",
     ["a) Silverstone", "b) Monza", "c) Monte Carlo", "d) Spa-Francorchamps"],"c"],
    
     #6
    ["\n¿Cuál es el color principal del equipo Red Bull Racing?",
     ["a) Azul", "b) Rojo", "c) Negro", "d) Amarillo"], "a"],
    
     #7
    ["\n¿Qué país alberga el circuito de Suzuka?",
     ["a) China", "b) Japón", "c) Corea del Sur", "d) Tailandia"], "b"],
    
     #8
    ["\n¿Cuál es el apodo del piloto Charles Leclerc?",
     ["a) The Prince of Monaco", "b) The Ice Man", "c) Mad Max", "d) The Honey Badger"], "a"],
    
     #9
    ["\n¿Qué neumáticos fabrica la Fórmula 1 actualmente?",
     ["a) Bridgestone", "b) Michelin", "c) Goodyear", "d) Pirelli"], "d"],
   
     #10
    ["\n¿Cuál de estos circuitos es el más rápido del calendario?",
     ["a) Spa-Francorchamps", "b) Monza", "c) Silverstone", "d) Baku"],"b"]
        ]
    
    #Mexcla aleatoriamente el orden de la lista de preguntas 
    random.shuffle(preguntas)

    # Ciclo para recorrer a lista de las preguntas y su sub-lista
    for pregunta, opciones, respuesta_correcta in preguntas:
        score += las_preguntas(pregunta, opciones, respuesta_correcta)
    
     # Operador aritmético (/ y *) con listas, calcula la calificación final 
    total_preguntas = len(preguntas)
    calificacion = (score / total_preguntas) * 100
    print("\nSacaste: ", calificacion, "/100")

    # operadores relacionales (==, >=)
    # estructura de decisión (if - elif - else)
    if calificacion == 100:
        print("Eres un experto en F1!")
    elif calificacion >= 50:
        print("Sigue la pista, vas en buen camino!")
    else:
        print("Necesitas más practicas, pero no te preocupes, cada gp hay 3!")

"""
================== Ciclo principal para repetir la trivia  ====================
"""
 # estructura de decisión/repaticion de listas
jugar_again = "si"
while jugar_again == "si":
    jugar()
    jugar_again = input("\nQuieres jugar de nuevo? (si/no): ")

print("Gracias por participar ")
