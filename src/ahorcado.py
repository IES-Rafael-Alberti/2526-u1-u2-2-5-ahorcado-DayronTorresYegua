"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: [Dayron Torres Yegua]
Fecha: [6/11/2025]
"""
import requests

def limpiar_pantalla():
    """
    Imprime varias líneas en blanco para 'limpiar' la consola
    y que el jugador 2 no vea la palabra introducida
    """
    print("\n" * 50)


def solicitar_palabra():
    """
    Solicita una palabra al jugador 1
    La palabra debe tener mínimo 5 caracteres y solo contener letras
    
    Returns:
        str: La palabra a adivinar en mayúsculas
    """
    # - Usar un bucle while para repetir hasta que la palabra sea válida
    # - Verificar que tenga al menos 5 caracteres (len())
    # - Verificar que solo contenga letras (isalpha())
    # - Convertir a mayúsculas (upper())
    url = "https://random-words-api.vercel.app/word/spanish"

    palabra = ""

    while len(palabra) < 5:
        # Hacer la solicitud GET dentro del ciclo para obtener una nueva palabra cada vez
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            palabra = data[0]["word"]
            if len(palabra) < 5:
                palabra = ""  # Vaciar para forzar otra iteración si palabra tiene menos de 5 letras
        else:
            print("Error al obtener la palabra aleatoria")

    return palabra.upper()

def aniadir_letras_usadas(letra:str) -> list:
    
    letras_usadas = []
    letras_usadas.append(letra)
    return letras_usadas

def solicitar_letra(letras_usadas):
    """
    Solicita una letra al jugador 2
    La letra debe ser válida (solo una letra) y no estar ya usada
    
    Args:
        letras_usadas (list): Lista de letras ya introducidas
        
    Returns:
        str: La letra introducida en mayúsculas
    """
    # - Usar un bucle while para repetir hasta que la letra sea válida
    # - Verificar que sea solo un carácter (len() == 1)
    # - Verificar que sea una letra (isalpha())
    # - Verificar que no esté en letras_usadas (operador 'in')
    # - Convertir a mayúsculas (upper())
    letra = None
    
    while not letra:
        letra = input("Introduce una letra: ")
        if len(letra) == 1 and letra.isalpha() and not letra in letras_usadas:
            return letra.upper()
        else:
            letra = None

def mostrar_estado(palabra_oculta, intentos, letras_usadas):
    """
    Muestra el estado actual del juego
    
    Args:
        palabra_oculta (str): La palabra con _ y letras adivinadas
        intentos (int): Número de intentos restantes
        letras_usadas (list): Lista de letras ya usadas
    """
    # TODO: Implementar la función
    # - Imprimir intentos restantes
    # - Imprimir la palabra con espacios entre caracteres
    # - Imprimir las letras usadas
    print(intentos)


def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    """
    Actualiza la palabra oculta revelando las apariciones de la letra
    
    Args:
        palabra (str): La palabra completa a adivinar
        palabra_oculta (str): La palabra actual con _ y letras adivinadas
        letra (str): La letra que se ha adivinado
        
    Returns:
        str: La palabra oculta actualizada
    """
    # TODO: Implementar la función
    # - Recorrer la palabra original con un bucle for
    # - Usar enumerate() para obtener índice y carácter
    # - Si el carácter coincide con la letra, reemplazar en palabra_oculta
    # - Puedes convertir palabra_oculta a lista, modificar y volver a string
    for letras in enumerate(palabra)


def jugar():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    print("=== JUEGO DEL AHORCADO ===\n")
    
    # Configuración inicial
    INTENTOS_MAXIMOS = 5
    
    # TODO: Solicitar la palabra al jugador 1
    palabra = solicitar_palabra()
    
    # TODO: Limpiar la pantalla para que el jugador 2 no vea la palabra
    limpiar_pantalla()
    
    # TODO: Inicializar variables del juego
    # - palabra_oculta: string con guiones bajos (ej: "_ _ _ _ _")
    # - intentos: número de intentos restantes
    # - letras_usadas: lista vacía
    # - juego_terminado: False
    
    print("Jugador 2: ¡Adivina la palabra!\n")
    
    # TODO: Bucle principal del juego
    # - Mientras haya intentos y el juego no haya terminado:
    #   1. Mostrar el estado actual
    #   2. Solicitar una letra
    #   3. Añadir la letra a letras_usadas
    #   4. Si la letra está en la palabra:
    #      - Actualizar palabra_oculta
    #      - Mostrar mensaje de acierto
    #      - Si ya no hay '_' en palabra_oculta, el jugador ha ganado
    #   5. Si la letra NO está en la palabra:
    #      - Restar un intento
    #      - Mostrar mensaje de fallo
    
    # TODO: Mostrar mensaje final
    # - Si ganó: mostrar felicitación y la palabra
    # - Si perdió: mostrar mensaje de derrota y la palabra correcta
    pass


def main():
    """
    Punto de entrada del programa
    """
    jugar()
    
    # TODO (Opcional): Preguntar si quiere jugar otra vez
    # jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    # if jugar_otra_vez.lower() == 's':
    #     main()


if __name__ == "__main__":
    main()
