class BoardOutException(Exception):
    """
    Класс исключения, который  используется чтобы отлавливать ошибки,
     когда игрок пытается выстрелить в клетку за пределами игрового поля.
    """

    def __init__(self, dot):
        self.dot = dot

    def __str__(self):
        return f"Точка с координатами ({self.dot[0]},{self.dot[1]})\
         находится за пределами  игрового поля."