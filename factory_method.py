# The Factory Method pattern is applicable when there is a hierarchy of Product classes.

# Basic product
class Button:
    def render(self):
        raise NotImplementedError("Method is not implemented!")

    def on_click(self):
        raise NotImplementedError("Method is not implemented!")


# Product A
class WindowsButton(Button):
    def render(self):
        print('Rendered Windows button')

    def on_click(self):
        print('Pressed Windows button')


# Product B
class LinuxButton(Button):
    def render(self):
        print('Rendered Linux button')

    def on_click(self):
        print('Pressed Linux button')


# The base class of the factory. Note that "factory" is just an additional role for the class. It already has some
# kind of business logic that requires the creation of a variety of products.
class Menu:
    def render_menu(self):
        ok_button = self.create_button()
        ok_button.render()
        ok_button.on_click()

    # Factory method
    def create_button(self):
        raise NotImplementedError("Method is not implemented!")


# Concrete factories override the factory method and return their own products from it.
class WindowsMenu(Menu):
    def create_button(self):
        return WindowsButton()


class LinuxMenu(Menu):
    def create_button(self):
        return LinuxButton()


# Depending on the configuration (or other conditions), select the desired factory.
if __name__ == '__main__':
    from sys import platform
    if platform == 'win32':
        menu = WindowsMenu()
    if platform == 'linux':
        menu = LinuxMenu()

    menu.render_menu()
