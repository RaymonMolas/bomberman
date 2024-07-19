# Bomberman en Python con Pygame

## ¿Qué es Python?

Python es un lenguaje de programación de alto nivel, ampliamente utilizado en diversas áreas debido a su simplicidad y legibilidad. Algunos aspectos clave de Python son:

- **Propósito General**: Python es un lenguaje de propósito general, lo que significa que se puede aplicar en una variedad de contextos, desde desarrollo web hasta análisis de datos y automatización.
- **Popularidad**: Python es uno de los lenguajes más populares en todo el mundo. Su comunidad activa y su amplia gama de bibliotecas hacen que sea una elección atractiva para desarrolladores de todos los niveles.
- **Sintaxis Legible**: La sintaxis de Python es clara y fácil de entender, lo que facilita la escritura y el mantenimiento del código.

### Ventajas de Python

- **Facilidad de Aprendizaje**:
  - Python es ideal para principiantes. Su sintaxis simple y su enfoque en la legibilidad permiten a los nuevos programadores aprender rápidamente.
  - La curva de aprendizaje es suave, lo que fomenta la adopción y la creatividad.
- **Multiplataforma**:
  - Python es compatible con múltiples sistemas operativos (Windows, macOS, Linux). Esto significa que puedes escribir código en una plataforma y ejecutarlo en otra sin problemas.
- **Amplia Comunidad y Bibliotecas**:
  - La comunidad de Python es activa y solidaria. Puedes encontrar respuestas a tus preguntas en foros, blogs y tutoriales.

## Pygame: Creando Juegos en Python

### ¿Qué es Pygame?

Pygame es una biblioteca específica para la creación de videojuegos en 2D utilizando Python. Está basada en SDL (Simple DirectMedia Layer), lo que proporciona acceso a bajo nivel al hardware gráfico, sonido y eventos del usuario.

### Características de Pygame

- **Desarrollo 2D**: Pygame está diseñado para crear juegos en 2D.
- **Multiplataforma**: Funciona en Mac OS, Windows y Linux.
- **Gráficos y Sonido**: Permite cargar imágenes, reproducir sonidos y crear efectos visuales.
- **Interacción del Usuario**: Detecta eventos como teclas y clics del mouse.

### ¿Por qué utilizar Pygame?

Pygame es una excelente elección para crear juegos en Python por varias razones:

- **Facilidad de Uso**:
  - Pygame está diseñado para simplificar el desarrollo de juegos en 2D.
  - Su sintaxis es clara y fácil de entender, lo que facilita la creación de juegos incluso para principiantes.
- **Multiplataforma**:
  - Los juegos creados con Pygame pueden ejecutarse en diferentes sistemas operativos, como Windows, macOS, Linux e incluso Android.
  - Esto significa que puedes desarrollar un juego en una plataforma y luego distribuirlo en otras sin problemas.
- **Amplia Comunidad y Documentación**:
  - Pygame tiene una comunidad activa de desarrolladores y entusiastas.
  - Hay una gran cantidad de tutoriales, ejemplos y recursos disponibles en línea para aprender y resolver problemas.
- **Manejo de Gráficos y Sonido**:
  - Pygame proporciona herramientas para cargar imágenes, crear animaciones, reproducir sonidos y música.
  - Puedes crear mundos visuales atractivos y efectos de sonido envolventes para tus juegos.
- **Interacción del Usuario**:
  - Detecta eventos del teclado, clics del mouse y otros dispositivos de entrada.
  - Puedes crear controles interactivos y mecánicas de juego personalizadas.

## Juego a Realizar: Bomberman

Bomberman es una franquicia de videojuegos estratégico-laberínticos que se originó en la década de 1980. El juego original, desarrollado por Hudson Soft, fue lanzado en 1983 para varias plataformas, incluyendo MSX, NEC PC-8801, NEC PC-6001, Sharp MZ-700 y FM-7 en Japón. Desde entonces, se han lanzado numerosos juegos de la serie.

### Características Clave de Bomberman

- **Jugabilidad Estratégica**:
  - Bomberman se juega en laberintos donde el jugador controla al personaje principal, Bomberman.
  - El objetivo es colocar bombas estratégicamente para abrir caminos, destruir obstáculos y eliminar enemigos.
- **Elementos Clásicos**:
  - Bomberman debe evitar las explosiones de sus propias bombas mientras se mueve por el laberinto.
  - Los enemigos también colocan bombas y persiguen a Bomberman.
- **Power-ups y Objetos**:
  - A lo largo del juego, Bomberman puede recoger power-ups que mejoran sus habilidades, como aumentar la cantidad de bombas que puede colocar o su alcance de explosión.
  - También hay objetos especiales, como patadas para mover las bombas o guantes para recogerlas.

## `menu.py`

Este código configura y gestiona la interfaz de usuario del menú para el juego. Incluye la inicialización de Pygame, la configuración de la ventana del juego y la creación de menús utilizando `pygame_menu`.

### Importaciones

- `pygame`: Biblioteca principal para el desarrollo del juego.
- `pygame_menu`: Biblioteca para la creación de menús en Pygame.
- `game`: Módulo principal del juego, que contiene la lógica del juego.
- `Algorithm`: Enumeración que define diferentes algoritmos para los personajes del juego.

### Constantes y Variables Globales

- `COLOR_BACKGROUND`: Color del fondo de la ventana del juego.
- `COLOR_BLACK`: Color negro.
- `COLOR_WHITE`: Color blanco.
- `FPS`: Frames por segundo para el juego.
- `MENU_BACKGROUND_COLOR`: Color de fondo del menú.
- `MENU_TITLE_COLOR`: Color del título del menú.
- `WINDOW_SCALE`: Escala de la ventana del juego.

### Inicialización

- Se inicializa Pygame y se configura la ventana del juego con un tamaño basado en el tamaño de los azulejos (`TILE_SIZE`).
- Se definen los algoritmos para los personajes y si se debe mostrar el camino.

### Funciones Principales

- `change_path(value, c)`: Cambia la configuración para mostrar o no el camino.
- `change_player(value, c)`: Cambia el algoritmo para el jugador.
- `change_enemy1(value, c)`, `change_enemy2(value, c)`, `change_enemy3(value, c)`: Cambian los algoritmos para los enemigos 1, 2 y 3, respectivamente.
- `run_game()`: Inicializa y ejecuta el juego con las configuraciones actuales.
- `main_background()`: Configura el fondo principal de la ventana del juego.
- `menu_loop()`: Maneja el bucle principal del menú, incluyendo la creación de menús y el manejo de eventos.

### Menús

- `play_menu`: Menú principal del juego con opciones para comenzar el juego o acceder a las opciones.
- `play_options`: Menú de opciones para configurar los algoritmos de los personajes y si se debe mostrar el camino.
- `main_menu`: Menú principal con opciones para jugar o salir del juego.

### Bucle Principal

- Controla el FPS del juego y actualiza la pantalla.
- Maneja los eventos de Pygame, como el cierre de la ventana del juego.
- Ejecuta el bucle del menú principal y actualiza la pantalla.

### Punto de Entrada Principal

- Si el script es ejecutado directamente, se llama a la función `menu_loop()` para iniciar el bucle principal del menú.

## `game.py`

Este código configura y gestiona la lógica del juego tipo Bomberman utilizando Pygame. Incluye la inicialización del juego, la gestión de elementos del juego, y la actualización y dibujo en pantalla.

### Importaciones

- `pygame`: Biblioteca principal para el desarrollo del juego.
- `sys`: Módulo para gestionar argumentos y salida del sistema.
- `random`: Módulo para generar números aleatorios.
- `PowerUpType`: Enumeración que define diferentes tipos de power-ups.
- `Player`, `Explosion`, `Enemy`, `PowerUp`: Clases que representan al jugador, explosiones, enemigos y power-ups.

### Constantes y Variables Globales

- `BACKGROUND_COLOR`: Color de fondo de la ventana del juego.
- `font`: Fuente para los textos en pantalla.
- `player`: Instancia del jugador.
- `enemy_list`: Lista de enemigos en el juego.
- `ene_blocks`: Lista de bloques que pueden interactuar con los enemigos.
- `bombs`: Lista de bombas activas.
- `explosions`: Lista de explosiones activas.
- `power_ups`: Lista de power-ups activos.
- `GRID_BASE`: Mapa base del juego representado como una matriz.

### Funciones Principales

- `game_init(surface, path, player_alg, en1_alg, en2_alg, en3_alg, scale)`: Inicializa el juego, configurando el jugador y los enemigos según los algoritmos proporcionados. Carga las imágenes para los diferentes tipos de terreno, bombas, explosiones y power-ups.
- `draw(s, grid, tile_size, show_path, game_ended, terrain_images, bomb_images, explosion_images, power_ups_images)`: Dibuja el mapa del juego, power-ups, bombas, explosiones, jugador y enemigos en la ventana del juego. Muestra el camino de los enemigos si `show_path` está activado. Muestra un mensaje de fin de juego si `game_ended` es `True`.
- `generate_map(grid)`: Modifica la matriz `grid` para generar un mapa aleatorio con bloques adicionales.
- `main(s, tile_size, show_path, terrain_images, bomb_images, explosion_images, power_ups_images)`: Ejecuta el bucle principal del juego. Maneja el movimiento y las acciones del jugador y los enemigos. Dibuja todos los elementos del juego en la ventana. Verifica si el juego ha terminado y maneja los eventos del usuario.
- `update_bombs(grid, dt)`: Actualiza el estado de las bombas y explosiones. Verifica si el jugador o los enemigos han muerto debido a explosiones. Elimina las explosiones que han terminado su ciclo.
- `check_end_game()`: Verifica si el juego ha terminado. Retorna `True` si el jugador ha muerto o todos los enemigos han muerto.

## `enemy.py`

Este módulo gestiona la lógica del enemigo en el juego. Configura el movimiento del enemigo, su ruta, y las interacciones con bombas y explosiones.

### Importaciones

- `pygame`: Biblioteca principal para el desarrollo del juego.
- `random`: Módulo para generar números aleatorios.
- `Bomb`: Clase que representa una bomba.
- `Node`: Clase que representa un nodo en la grilla para los algoritmos de búsqueda.
- `Algorithm`: Enumeración que define diferentes algoritmos de búsqueda (DFS y Dijkstra).

### Constantes y Variables de Clase

- `dire`: Lista de direcciones posibles para el movimiento del enemigo (abajo, derecha, arriba, izquierda).
- `TILE_SIZE`: Tamaño de un tile en el mapa.

### Métodos de la Clase `Enemy`

- `__init__(self, x, y, alg)`: Inicializa al enemigo con su posición, vida, ruta y algoritmo de movimiento.
- `move(self, map, bombs, explosions, enemy)`: Mueve al enemigo en la dirección actual y actualiza su ruta si es necesario.
- `make_move(self, map, bombs, explosions, enemy)`: Ejecuta el movimiento del enemigo, eligiendo un nuevo camino si no hay uno actual.
- `plant_bomb(self, map)`: Planta una bomba en la posición actual del enemigo.
- `check_death(self, exp)`: Verifica si el enemigo está en una posición de explosión y debe morir.
- `dfs(self, grid)`: Calcula la ruta del enemigo usando el algoritmo de búsqueda en profundidad (DFS).
- `dfs_rec(self, grid, end, path, depth)`: Función recursiva para realizar la búsqueda en profundidad.
- `dijkstra(self, grid)`: Calcula la ruta del enemigo usando el algoritmo de Dijkstra.
- `create_grid(self, map, bombs, explosions, enemys)`: Crea una grilla de navegación para el algoritmo DFS.
- `create_grid_dijkstra(self, map, bombs, explosions, enemys)`: Crea una grilla de navegación para el algoritmo de Dijkstra.
- `load_animations(self, en, scale)`: Carga las animaciones del enemigo en diferentes direcciones y tamaños.

## `explosion.py`

Este módulo define la lógica para manejar las explosiones en el juego.

### Importaciones

- `PowerUpType`: Enumeración para diferentes tipos de power-ups.
- `PowerUp`: Clase que representa los power-ups en el juego.

### Clase `Explosion`

#### Variables

- `bomber`: Variable estática para almacenar el jugador que colocó la bomba.
- `sourceX, sourceY, range, time, frame, sectors`: Atributos que definen la posición, rango, tiempo de vida, estado actual y sectores afectados por la explosión.

#### Métodos

- `__init__(x, y, r)`: Inicializa una explosión en una posición específica con un rango dado.
- `explode(map, bombs, b, power_ups)`: Maneja la explosión en el mapa, elimina la bomba de la lista y gestiona la reacción en cadena de explosiones.
- `bomb_chain(bombs, map, power_ups)`: Realiza una reacción en cadena de explosiones, elimina power-ups y bombas en los sectores afectados, y realiza nuevas explosiones si es necesario.
- `clear_sectors(map, random, power_ups)`: Limpia los sectores afectados en el mapa y genera posibles power-ups aleatorios.
- `update(dt)`: Actualiza el tiempo de vida de la explosión y ajusta el frame de la animación en función del tiempo restante.

## `player.py`

La clase `Player` gestiona la lógica del jugador en el juego.

### Importaciones
- `pygame`: Biblioteca principal para el desarrollo del juego.
- `math`: Módulo para funciones matemáticas.
- `Bomb`: Clase que representa una bomba.
- `PowerUpType`: Enumeración que define los tipos de power-ups.

### Constantes y Variables
- `pos_x` y `pos_y`: Posición inicial del jugador en el eje x e y.
- `direction`: Dirección inicial del jugador.
- `frame`: Frame actual de la animación.
- `animation`: Lista de animaciones del jugador.
- `rango`: Alcance inicial de las bombas del jugador.
- `bomb_limit`: Límite inicial de bombas que el jugador puede plantar.
- `TILE_SIZE`: Tamaño de cada tile en el mapa.

### Métodos
- `__init__()`: Inicializa el estado de vida del jugador.
- `move(dx, dy, grid, enemigos, power_ups)`: Mueve al jugador en la dirección especificada y verifica si consume un power-up.
- `plant_bomb(mapa)`: Crea una bomba en la posición del jugador.
- `check_death(explosiones)`: Verifica si el jugador muere al estar en una posición de explosión.
- `consumir_power_up(power_up, power_ups)`: Aplica los efectos del power-up consumido y lo elimina de la lista de power-ups.
- `load_animations(escala)`: Carga y escala las animaciones del jugador según el tamaño especificado.

## `bomb.py`

La clase `Bomb` gestiona la lógica y el comportamiento de una bomba en el juego.

### Importaciones
- `pygame`: Biblioteca principal para el desarrollo del juego.
- `sys`: Módulo para manejar argumentos del sistema y la salida.

### Atributos
- `frame`: Controla el marco actual de la animación de la bomba.
- `range`: Alcance de la explosión de la bomba.
- `pos_x` y `pos_y`: Coordenadas de la bomba en el mapa.
- `time`: Tiempo restante hasta que la bomba explote (en milisegundos).
- `bomber`: Jugador que colocó la bomba.
- `sectors`: Lista de sectores que serán afectados por la explosión.

#### Métodos
- `__init__(self, r, x, y, map, bomber)`: Inicializa una nueva bomba con el alcance, posición, mapa y el jugador que la colocó. Calcula los sectores afectados por la explosión llamando a `get_range`.
- `update(self, dt)`: Actualiza el estado de la bomba según el tiempo transcurrido (`dt`). Cambia el marco de la animación basado en el tiempo restante.
- `get_range(self, map)`: Determina los sectores del mapa afectados por la explosión. Recorre el mapa en las direcciones horizontal y vertical desde la posición de la bomba, añadiendo sectores afectados a la lista `sectors`.

## `node.py`

La clase `Node` se utiliza en algoritmos de búsqueda para representar un nodo en un grafo o estructura similar.

### Atributos
- `parent`: Nodo padre en el camino hacia el nodo actual.
- `weight`: Peso acumulado desde el inicio hasta el nodo actual.
- `direction`: Dirección asociada al nodo (opcional).

### Método `__init__`
- `px (int)`: Posición x del nodo en una matriz o grid.
- `py (int)`: Posición y del nodo en una matriz o grid.
- `reach (int)`: Alcance o distancia desde el nodo inicial.
- `base_weight (float)`: Peso base asociado al nodo para algoritmos de búsqueda.
- `value (int)`: Valor asociado al nodo, que puede representar diferentes cosas según el contexto.

## `power_up.py`

Este archivo define una clase llamada `PowerUp` que representa un objeto de tipo "power-up" en el juego. La clase gestiona la posición y el tipo del power-up.

### Métodos

- `__init__(self, x: int, y: int, power_type: str) -> None`:
  - **x (int)**: Coordenada x de la posición del power-up.
  - **y (int)**: Coordenada y de la posición del power-up.
  - **power_type (str)**: Tipo de power-up, que define el efecto o característica del power-up en el juego.

## `algorithm.py`

Este archivo define una enumeración para representar diferentes algoritmos de búsqueda en la aplicación.

### Enumeración

- **DFS (0)**: Algoritmo de búsqueda en profundidad.
- **DIJKSTRA (1)**: Algoritmo de Dijkstra.
- **PLAYER (2)**: Algoritmo asociado al jugador.
- **NONE (3)**: Valor nulo o sin algoritmo específico.

## `power_up_type.py`

Este archivo define una enumeración para representar diferentes tipos de power-ups en el juego.

### Enumeración

- **PowerUpType**: Enum que define dos tipos de power-ups:
  - **BOMB (0)**: Incrementa el número de bombas disponibles.
  - **FIRE (1)**: Incrementa la potencia explosiva de las bombas.
