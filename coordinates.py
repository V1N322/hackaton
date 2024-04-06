class Coordinates:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y
    
    def get(self):
        return {
            'x': self.x,
            'y': self.y}
    
    def change_x(self, x):
        self.x = x

    def change_y(self, y):
        self.y = y

    def change(self, x, y):
        self.change_x(x)
        self.change_y(y)


class Letlong(Coordinates):
    def __init__(self, x: float = 0.0, y: float = 0.0):
        super().__init__(x, y)