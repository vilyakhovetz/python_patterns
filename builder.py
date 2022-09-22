# A builder can create different products using the same building process.
class Car:
    pass


class Manual:
    pass


# The builder interface declares all possible product configuration steps.
class Builder:
    def reset(self):
        raise NotImplementedError("Method is not implemented!")

    def set_seats(self, seats):
        raise NotImplementedError("Method is not implemented!")

    def set_engine(self, engine):
        raise NotImplementedError("Method is not implemented!")

    def set_gps(self, gps):
        raise NotImplementedError("Method is not implemented!")


# All concrete builders implement the common interface in their own way.
class CarBuilder(Builder):
    def __init__(self):
        self.__car = Car()

    def reset(self):
        self.__car = Car()

    def set_seats(self, seats):
        self.__car.__seats = seats

    def set_engine(self, engine):
        self.__car.__engine = engine

    def set_gps(self, gps):
        self.__car.__gps = gps

    def get_result(self):
        print(f'Car: seats = {self.__car.__seats}, engine = {self.__car.__engine}, gps = {self.__car.__gps}')
        return self.__car


class ManualBuilder(Builder):
    def __init__(self):
        self.__manual = Manual()

    def reset(self):
        self.__manual = Manual()

    def set_seats(self, seats):
        self.__manual.__seats = seats

    def set_engine(self, engine):
        self.__manual.__engine = engine

    def set_gps(self, gps):
        self.__manual.__gps = gps

    def get_result(self):
        print(f'Manual for car: seats = {self.__manual.__seats}, engine = {self.__manual.__engine}, gps = {self.__manual.__gps}')
        return self.__manual


# The director knows in what sequence to make the builder work. It works with it through a common builder interface.
# Because of this, he may not know what specific product is being built.
class Director:
    def build_sports_car(self, builder):
        builder.reset()
        builder.set_seats(2)
        builder.set_engine('V8')
        builder.set_gps(True)


# The director receives a specific builder object from the client (application). The application itself knows which
# builder to use in order to get the desired product.

# The finished product is returned by the builder, since the director most often does not know and does not depend on
# specific classes of builders and products.
if __name__ == '__main__':
    director = Director()

    builder1 = CarBuilder()
    director.build_sports_car(builder1)
    car = builder1.get_result()

    builder2 = ManualBuilder()
    director.build_sports_car(builder2)
    manual = builder2.get_result()
