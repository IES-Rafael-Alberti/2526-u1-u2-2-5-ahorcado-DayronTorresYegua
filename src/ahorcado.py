"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: [Dayron Torres Yegua]
Fecha: [7/11/2025]
"""

# Importacion de modulos necesarios

import requests

def limpiar_pantalla():
    """
    Imprime varias líneas en blanco para 'limpiar' la consola
    y que el jugador 2 no vea la palabra introducida
    """
    print("\n" * 50)


def solicitar_palabra() -> str:
    """
    Solicita una palabra al jugador 1
    La palabra debe tener mínimo 5 caracteres y solo contener letras
    
    Returns
    -------
    str
        Una cadena que contiene una palabra a adivinar al azar con al menos 5 letras y en mayúsculas
    """
    url = "https://random-words-api.vercel.app/word/spanish"

    palabra = ""

    while len(palabra) < 5:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            palabra = data[0]["word"]
            if len(palabra) < 5:
                palabra = ""
        else:
            print("Error al obtener la palabra aleatoria")

    return palabra.upper()

def ocultar_palabra(palabra:str) -> str:
    """ 
    Recibe la palabra a adivinar y la oculta sustituyendo las letras por "_"
    
    Parameters
    ----------
        palabra : str
            String que contiene la palabra original a adivinar
    
    Returns
    -------
    str
        Una cadena que contiene una palabra a adivinar al azar con al menos 5 letras y en mayúsculas
    """
    
    palabra_oculta = " ".join(["_"] * len(palabra))
    
    return palabra_oculta
    
def aniadir_letras_usadas(letras_usadas:list, letra:str) -> list:
    """ 
    Recibe una lista de las letras usadas y la letra a comprobar añadir y devuelve la lista con las letras usadas
    
    Parameters
    ----------
        letras_usadas : list
            Lista que contien las letras usadas
        letra : str
            String que contiene la letra a adivinar
    Returns
    -------
        list
            Lista que contien las letras usadas actualizada con la nueva letra
    """
    
    letras_usadas.append(letra)
    
    return letras_usadas

def solicitar_letra(letras_usadas) -> str:
    """ 
    Solicita al jugador 2 una letra para adivinar la palabra, comprueba que 
    la letra sea valida y no usada y devuelve la letra introducida
    
    Parameters
    ----------
        letras_usadas : list
            Lista que contiene las letras usadas
    Returns
        str
            String que contiene la letra a adivinar en mayúscula
    -------
    """
    
    letra = None
    
    while not letra:
        letra = input("Introduce una letra: ").upper()
        
        if len(letra) == 1 and letra.isalpha() and not letra in letras_usadas:
            return letra.upper()
        else:
            print("Debe introducir una letra valida y que no este en letras usadas.")
            letra = None

def mostrar_estado(palabra_oculta, intentos, letras_usadas):
    """ 
    Muestra el estado actual del juego (La palabra oculta, los intentos restantes y las letras usadas)
    
    Parameters
    ----------
        palabra_oculta : str
            String que contiene la palabra oculta (la palabra actual pero con "_")
        intentos : int
            Numero entero que representa el numero de intentos restantes
        letras_usadas : list
            Lista que contiene las letras ya usadas
    """
    
    print(f'La palabra oculta es: {palabra_oculta}\nNumero de intentos: {intentos}\nLetras usadas: {letras_usadas}')
    
def actualizar_palabra_oculta(palabra, palabra_oculta, letra) -> str:
    """ 
    Actualiza la palabra oculta sustituyendo las "_" por las letras ya adivinadas
    Parameters
    ----------
        palabra : str
            String que contiene la palabra original a adivinar
        palabra_oculta : str
            String que contiene la palabra oculta (la palabra actual pero con "_")
        letra : str
            String que contiene la letra a adivinar
    Returns
    -------
        str
            String que contiene la palabra oculta pero actualizada
    """
    
    palabra_oculta_lista = palabra_oculta.split(" ")
    
    for indice, caracter in enumerate(palabra):
        if caracter == letra:
            palabra_oculta_lista[indice] = letra
    palabra_oculta = " ".join(palabra_oculta_lista)
    
    return palabra_oculta
    
def jugar():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    
    print("=== JUEGO DEL AHORCADO ===\n")
    
    # Configuración inicial
    INTENTOS_MAXIMOS = 5
    palabra = solicitar_palabra()
    limpiar_pantalla()
        
    palabra_oculta = ocultar_palabra(palabra) # - palabra_oculta: string con guiones bajos (ej: "_ _ _ _ _")
    intentos = INTENTOS_MAXIMOS# - intentos: número de intentos restantes
    letras_usadas = [] # - letras_usadas: lista vacía
    juego_terminado = False
    
    print("Jugador 2: ¡Adivina la palabra!\n")
        
    while intentos > 0 and not juego_terminado:
        mostrar_estado(palabra_oculta, intentos, letras_usadas)
        letra = solicitar_letra(letras_usadas)
        letras_usadas = aniadir_letras_usadas(letras_usadas, letra)
        
        if letra in palabra:
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
            print(f"La letra {letra} esta en la palabra")
            
            if not "_" in palabra_oculta:
                juego_terminado = True
        else:
            intentos -= 1
            print(f"Error, la letra {letra} no esta en la palabra.")
            
            
    if not juego_terminado:
        print(f"¡Has perdido! Se te acabaron los intentos.")
        print(f"La palabra era: {palabra}")
    
    if juego_terminado:
        print(f"Enhorabuena ganaste\nLa palabra era {palabra}")
    else:
        print(f"Perdiste\nLa palabra era {palabra}")

def main():
    """
    Punto de entrada del programa
    """
    jugar()
    
    """ 
    Bucle que pregunta si quieres volver a jugar despues de acabar el juego
    """
    
    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ").lower()

    if jugar_otra_vez == 's':
        main()
            
if __name__ == "__main__":
    main()
