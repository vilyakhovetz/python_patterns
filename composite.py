# Composite is a structural design pattern which allows you to group objects into a tree structure, and then work
# with them as if it were single object.

# Common Component interface.
class Graphic:
    def move(self, x, y):
        raise NotImplementedError("Method is not implemented!")

    def draw(self):
        raise NotImplementedError("Method is not implemented!")


# Simple Component.
class Dot(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print(f'Drawn dot with coordinates x = {self.x}, y = {self.y}')


# Components can extend other Components.
class Circle(Dot):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        print(f'Drawn circle with coordinates x = {self.x}, y = {self.y} and radius = {self.radius}')


# Composite contains operations for adding/removing child components. It delegates all standard operations of the
# component interface to each of the child components.
class CompoundGraphic(Graphic):
    def __init__(self):
        self.children = []

    def add(self, graphic):
        self.children.append(graphic)

    def remove(self, graphic):
        self.children.remove(graphic)

    def move(self, x, y):
        for child in self.children:
            child.move(x, y)

    def draw(self):
        for child in self.children:
            child.draw()


if __name__ == '__main__':
    # Adding simple components to Composite
    cg = CompoundGraphic()
    cg.add(Dot(1, 2))
    cg.add(Circle(4, 6, 10))

    # Adding other Composite to Composite
    cg2 = CompoundGraphic()
    cg2.add(Dot(5, 9))
    cg2.add(Circle(3, 8, 7))
    cg.add(cg2)

    # Drawing all Graphics at once.
    cg.draw()
