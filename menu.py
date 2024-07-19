import pygame
import pygame_menu

import game  # Importa el módulo principal del juego
from enums.algorithm import Algorithm  # Importa la enumeración Algorithm desde un archivo específico

# Definición de constantes y variables globales
COLOR_BACKGROUND = (153, 153, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (102, 102, 153)
MENU_TITLE_COLOR = (51, 51, 255)
WINDOW_SCALE = 0.75

# Inicialización de pygame y configuración de la ventana del juego
pygame.display.init()
INFO = pygame.display.Info()
TILE_SIZE = int(INFO.current_h * 0.035)
WINDOW_SIZE = (13 * TILE_SIZE, 13 * TILE_SIZE)

clock = None
player_alg = Algorithm.PLAYER  # Algoritmo seleccionado para el jugador
en1_alg = Algorithm.DIJKSTRA  # Algoritmo seleccionado para el enemigo 1
en2_alg = Algorithm.DFS  # Algoritmo seleccionado para el enemigo 2
en3_alg = Algorithm.DIJKSTRA  # Algoritmo seleccionado para el enemigo 3
show_path = True  # Mostrar camino (para el juego)
surface = pygame.display.set_mode(WINDOW_SIZE)  # Superficie de la ventana del juego

# Función para cambiar la configuración de mostrar o no el camino
def change_path(value, c):
    global show_path
    show_path = c

# Funciones para cambiar los algoritmos de los personajes
def change_player(value, c):
    global player_alg
    player_alg = c

def change_enemy1(value, c):
    global en1_alg
    en1_alg = c

def change_enemy2(value, c):
    global en2_alg
    en2_alg = c

def change_enemy3(value, c):
    global en3_alg
    en3_alg = c

# Función para inicializar y ejecutar el juego
def run_game():
    game.game_init(surface, show_path, player_alg, en1_alg, en2_alg, en3_alg, TILE_SIZE)

# Función para configurar el fondo principal
def main_background():
    global surface
    surface.fill(COLOR_BACKGROUND)

# Función principal para el bucle del menú
def menu_loop():
    pygame.init()  # Inicializa pygame

    pygame.display.set_caption('Bomberman')  # Título de la ventana del juego
    clock = pygame.time.Clock()  # Reloj para controlar el FPS del juego

    # Tema para los menús principales y de opciones
    menu_theme = pygame_menu.Theme(
        selection_color=COLOR_WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=TILE_SIZE,
        title_font_color=COLOR_BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.7),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR,
    )

    # Menú principal de juego
    play_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        title='Menu de Juego'
    )

    # Menú de opciones de configuración
    play_options = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        title='Opciones'
    )
    
    # Agrega selectores para elegir algoritmos para los personajes
    play_options.add.selector("Personaje 1", [("Jugador", Algorithm.PLAYER), ("DFS", Algorithm.DFS),
                                              ("DIJKSTRA", Algorithm.DIJKSTRA), ("Ninguno", Algorithm.NONE)], onchange=change_player)
    play_options.add.selector("Personaje 2", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("Ninguno", Algorithm.NONE)], onchange=change_enemy1)
    play_options.add.selector("Personaje 3", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("Ninguno", Algorithm.NONE)], onchange=change_enemy2,  default=1)
    play_options.add.selector("Personaje 4", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("Ninguno", Algorithm.NONE)], onchange=change_enemy3)
    
    # Selector para mostrar o no el camino
    play_options.add.selector("Mostrar Camino", [("Sí", True), ("No", False)], onchange=change_path)

    # Botón para volver al menú principal desde las opciones
    play_options.add.button('Volver', pygame_menu.events.BACK)
    
    # Botón para comenzar el juego desde el menú principal
    play_menu.add.button('Comenzar', run_game)

    # Botón para acceder a las opciones desde el menú principal
    play_menu.add.button('Opciones', play_options)

    # Botón para volver al menú principal desde los menús secundarios
    play_menu.add.button('Volver al Menu  Principal', pygame_menu.events.BACK)

    # Tema para el menú "Acerca de"
    about_menu_theme = pygame_menu.themes.Theme(
        selection_color=COLOR_WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=TILE_SIZE,
        title_font_color=COLOR_BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.5),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR
    )

    # Menú principal
    main_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        onclose=pygame_menu.events.EXIT,
        title='Menu Principal'
    )

    # Botones principales del menú principal
    main_menu.add.button('Jugar', play_menu)
    main_menu.add.button('Salir', pygame_menu.events.EXIT)

    running = True
    while running:
        clock.tick(FPS)  # Controla el FPS del juego

        main_background()  # Configura el fondo principal

        events = pygame.event.get()  # Obtiene los eventos del juego
        for event in events:
            if event.type == pygame.QUIT:
                running = False  # Termina el bucle si se cierra la ventana del juego

        if main_menu.is_enabled():
            main_menu.mainloop(surface, main_background)  # Ejecuta el bucle principal del menú

        pygame.display.flip()  # Actualiza la pantalla

    exit()  # Sale del programa

# Punto de entrada principal del programa
if __name__ == "__main__":
    menu_loop()  # Ejecuta el bucle principal del menú
