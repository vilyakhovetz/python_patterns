# Bridge is a structural design pattern that splits one or more classes into two separate hierarchies - abstraction
# and implementation, allowing you to change them independently of each other.

# Remote class has a reference to the device it controls. The methods of this class delegate work to the methods of
# the associated device.

class Remote:
    def __init__(self, device):
        self.__device = device

    def toggle_power(self):
        if self.__device.is_enabled():
            self.__device.disable()
        else:
            self.__device.enable()

    def volume_down(self):
        self.__device.set_volume(self.__device.get_volume() - 10)

    def volume_up(self):
        self.__device.set_volume(self.__device.get_volume() + 10)

    def channel_down(self):
        self.__device.set_channel(self.__device.get_channel() - 1)

    def channel_up(self):
        self.__device.set_channel(self.__device.get_channel() + 1)


# You can extend Remote class without touching Device code.
class AdvancedRemote(Remote):
    def __init__(self, device):
        super().__init__(device)
        self.__device = device

    def mute(self):
        self.__device.set_volume(0)


# All Devices share a common interface. Therefore, any Remote can work with them.
class Device:
    def is_enabled(self):
        raise NotImplementedError("Method is not implemented!")

    def enable(self):
        raise NotImplementedError("Method is not implemented!")

    def disable(self):
        raise NotImplementedError("Method is not implemented!")

    def set_volume(self, volume):
        raise NotImplementedError("Method is not implemented!")

    def get_volume(self):
        raise NotImplementedError("Method is not implemented!")

    def set_channel(self, channel):
        raise NotImplementedError("Method is not implemented!")

    def get_channel(self):
        raise NotImplementedError("Method is not implemented!")


# But each Device has a special implementation.
class TV(Device):
    def __init__(self):
        self.__is_enabled = False
        self.__volume = 0
        self.__channel = 0

    def is_enabled(self):
        return self.__is_enabled

    def enable(self):
        self.__is_enabled = True

    def disable(self):
        self.__is_enabled = False

    def set_volume(self, percent):
        self.__volume = percent

    def get_volume(self):
        return self.__volume

    def set_channel(self, channel):
        self.__channel = channel

    def get_channel(self):
        return self.__channel


class Radio(Device):
    def __init__(self):
        self.__is_enabled = False
        self.__volume = 0
        self.__channel = 0

    def is_enabled(self):
        return self.__is_enabled

    def enable(self):
        self.__is_enabled = True

    def disable(self):
        self.__is_enabled = False

    def set_volume(self, percent):
        self.__volume = percent

    def get_volume(self):
        return self.__volume

    def set_channel(self, channel):
        self.__channel = channel

    def get_channel(self):
        return self.__channel


if __name__ == '__main__':
    tv = TV()
    remote = Remote(tv)
    print(tv.get_volume())  # 0
    remote.volume_up()
    print(tv.get_volume())  # 10

    print()

    radio = Radio()
    remote = AdvancedRemote(radio)
    print(radio.get_volume())  # 0
    remote.volume_up()
    print(radio.get_volume())  # 10
    remote.mute()
    print(radio.get_volume())  # 0
