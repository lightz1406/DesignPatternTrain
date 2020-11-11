# interface
from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class Light:
    def on(self):
        print('Light on')

    def off(self):
        print('Light off')


class GarageDoor:
    def open(self):
        print('Garage door is open')

    def close(self):
        print('Garage door is close')


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class GarageDoorOpenCommand:
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.open()


class SimpleRemoterControl:
    slot = None

    def set_command(self, command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()


class RemoteControlTest:
    def __init__(self):
        remote = SimpleRemoterControl()
        light = Light()
        light_on = LightOnCommand(light)
        remote.set_command(light_on)
        remote.button_was_pressed()

        garage_door = GarageDoor()
        garage_door_open = GarageDoorOpenCommand(garage_door)
        remote.set_command(garage_door_open)
        remote.button_was_pressed()
