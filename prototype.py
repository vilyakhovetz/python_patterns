# Prototype is a creational design pattern which allows you to copy objects without going into details of their
# implementation.

# Basic prototype
class Shape:
    # Copying of all fields of the object occurs in the constructor.
    def __init__(self, source=None):
        if source is not None:
            self.x = source.x
            self.y = source.y
            self.color = source.color

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    # The result of a clone operation will always be an object from the Shape class hierarchy.
    def clone(self):
        raise NotImplementedError("Method is not implemented!")


# Specific prototype. The clone method creates a new object and passes its own object to its constructor for copying.
# By this we are trying to get the atomicity of the clone operation. In this implementation, until the constructor is
# executed, the new object does not yet exist. But as soon as the constructor is completed, we get a completely
# finished clone object, and not an empty object that needs to be filled.
class Rectangle(Shape):
    def __init__(self, source=None):
        super().__init__(source=source)
        if source is not None:
            self.width = source.width
            self.height = source.height

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def clone(self):
        return Rectangle(source=self)


class Circle(Shape):
    def __init__(self, source=None):
        # The call to the parent constructor is needed to copy potential private fields declared in the parent class.
        super().__init__(source=source)
        if source is not None:
            self.radius = source.radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def clone(self):
        return Circle(source=self)


if __name__ == '__main__':
    shapes = []

    rectangle1 = Rectangle()
    rectangle1.set_x(5)
    rectangle1.set_y(3)
    rectangle1.set_color('yellow')
    rectangle1.set_width(20)
    rectangle1.set_height(30)
    shapes.append(rectangle1)

    rectangle2 = rectangle1.clone()
    shapes.append(rectangle2)

    circle1 = Circle()
    circle1.set_x(1)
    circle1.set_y(5)
    circle1.set_color('red')
    circle1.set_radius(7)
    shapes.append(circle1)

    circle2 = circle1.clone()
    shapes.append(circle2)

    # An unobvious advantage of the Prototype is that you can clone a set of objects without knowing their concrete
    # classes.
    shapes_copy = []
    for shape in shapes:
        shapes_copy.append(shape.clone())

    # For example, we don't know what specific objects are inside the shapes array. But thanks to polymorphism,
    # we can blindly clone all objects. The "clone" method of the class that this object is will be executed.
    print(shapes_copy)
    print(rectangle1.get_height() == rectangle2.get_height())
    print(circle1.get_color() == circle2.get_color())

    # The shapes_copy variable will contain exact copies of the elements of the shapes array.
