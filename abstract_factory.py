# This pattern assumes that you have multiple product families in separate class hierarchies (Button/Checkbox).
# Products of the same family must have a common interface.

# All product families have the same variations (Windows/Linux).

class Button:
    def render(self):
        raise NotImplementedError("Method is not implemented!")


class WindowsButton(Button):
    def render(self):
        print(f'Rendered Windows button')


class LinuxButton(Button):
    def render(self):
        print(f'Rendered Linux button')


class Checkbox:
    def render(self):
        raise NotImplementedError("Method is not implemented!")


class WindowsCheckbox(Checkbox):
    def render(self):
        print(f'Rendered Windows checkbox')


class LinuxCheckbox(Checkbox):
    def render(self):
        print(f'Rendered Linux checkbox')


# The abstract factory knows about all (abstract) product types.
class GUI:
    def render_gui(self):
        button = self.create_button()
        checkbox = self.create_checkbox()
        button.render()
        checkbox.render()

    def create_button(self):
        raise NotImplementedError("Method is not implemented!")

    def create_checkbox(self):
        raise NotImplementedError("Method is not implemented!")


# Each specific factory knows and creates only products of its variation.
class WindowsGUI(GUI):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class LinuxGUI(GUI):
    def create_button(self):
        return LinuxButton()

    def create_checkbox(self):
        return LinuxCheckbox()


# Depending on the configuration (or other conditions), select the desired factory.
if __name__ == '__main__':
    from sys import platform

    if platform == 'win32':
        gui = WindowsGUI()
        gui.render_gui()

    if platform == 'linux':
        gui = LinuxGUI()
        gui.render_gui()
