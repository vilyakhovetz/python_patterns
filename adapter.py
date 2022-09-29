# Adapter transforms the interface or data of one object in such a way that it becomes understandable to another object.

# Classes with compatible interfaces: RoundHole and RoundPeg.
class RoundHole:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def fits(self, peg):
        return self.radius >= peg.get_radius()


class RoundPeg:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


# Old incompatible class SquarePeg
class SquarePeg:
    def __init__(self, width):
        self.width = width

    def get_width(self):
        return self.width


# The adapter allows you to use square pegs and round holes together.
class SquarePegAdapter(RoundPeg):
    def __init__(self, peg):
        self.__peg = peg

    # Calculate half the diagonal of a square peg using the Pythagorean theorem.
    def get_radius(self):
        return ((2 * (self.__peg.get_width() ** 2)) ** 0.5) / 2


if __name__ == '__main__':
    hole = RoundHole(5)

    round_peg = RoundPeg(5)
    print(hole.fits(round_peg))  # true

    small_square_peg = SquarePeg(2)
    big_square_peg = SquarePeg(10)
    small_square_peg_adapter = SquarePegAdapter(small_square_peg)
    big_square_peg_adapter = SquarePegAdapter(big_square_peg)
    print(hole.fits(small_square_peg_adapter))  # true
    print(hole.fits(big_square_peg_adapter))  # false
