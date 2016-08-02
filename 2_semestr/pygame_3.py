class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self):
        return (self.x, self.y)

class Collider:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def __call__(self):
        return (x, y, dx, dy)
        

class GameObject:

    def __init__(self, x, y):
        self.position = Position(x, y)

        self.collider = Collider(x, y, 0, 0)


class Box:
    def __init__(self, x, y, width, height):
        GameObject.__init__(self, x, y, width, height)

box1 = Box(10, 20)
