# Flyweight is a structural design pattern which allows you to fit more objects into the allocated RAM due to
# economical sharing the general state of objects among themselves, instead of storing the same data in every object.

# Flyweight TreeType class contains some of the fields that describe Trees. These fields are not unique for each Tree,
# unlike, for example, coordinates - several Trees can have the same texture.
# Therefore, we transfer repeated data into one single object and refer to it from many Trees.
class TreeType:
    def __init__(self, name, color, texture):
        self.__name = name
        self.__color = color
        self.__texture = texture

    def draw(self, x, y):
        print(f'{self.__color} {self.__texture} {self.__name} tree is painted at coordinates ({x},{y})')


# Flyweight factory decides when to create a new Flyweight and when to make do with an existing one.
class TreeFactory:
    tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        if (name, color, texture) in cls.tree_types:
            tree_type = cls.tree_types[(name, color, texture)]
        else:
            tree_type = TreeType(name, color, texture)
            cls.tree_types[(name, color, texture)] = tree_type
        return tree_type


# The context object from which we extracted Flyweight TreeType. There can be thousands of Tree objects in a
# program, since the overhead of storing them is very small - on the order of three integers (two coordinates and a
# reference).
class Tree:
    def __init__(self, tree_type):
        self.tree_type = tree_type

    def draw(self, x, y):
        return self.tree_type.draw(x, y)


if __name__ == '__main__':
    type1 = TreeFactory.get_tree_type('african', 'red', 'smooth')

    tree1 = Tree(type1)
    tree1.draw(5, 4)

    tree2 = Tree(type1)
    tree2.draw(7, 9)

    tree3 = Tree(type1)
    tree3.draw(2, 1)

    print(f'3 trees were painted but, there is only {len(TreeFactory.tree_types)} object of Tree types')
