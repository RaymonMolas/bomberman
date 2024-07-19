class Node:
    """
    Clase que representa un nodo en un algoritmo de búsqueda.
    """

    parent = None  # Nodo padre en el camino hacia este nodo
    weight = None  # Peso acumulado desde el inicio hasta este nodo
    direction = 1  # Dirección asociada al nodo (opcional)

    def __init__(self, px, py, reach, base_weight, value):
        """
        Inicializa un nuevo nodo con las coordenadas, alcance, peso base y valor.

        Args:
            px (int): Posición x del nodo en la matriz o grid.
            py (int): Posición y del nodo en la matriz o grid.
            reach (int): Alcance o distancia desde el nodo inicial.
            base_weight (float): Peso base asociado al nodo para algoritmos de búsqueda.
            value (int): Valor asociado al nodo que puede representar diferentes cosas según el contexto.
        """
        self.x = px  # Posición x del nodo
        self.y = py  # Posición y del nodo
        self.reach = reach  # Alcance o distancia desde el nodo inicial
        self.base_weight = base_weight  # Peso base del nodo
        self.value = value  # Valor asociado al nodo
