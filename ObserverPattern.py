from abc import ABCMeta, abstractmethod


# interface
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def register_observer(self, obs):
        pass

    @abstractmethod
    def remover_observer(self, obs):
        pass

    @abstractmethod
    def notify_observer(self):
        pass


# interface
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, temp, humidity, pressure):
        pass


# interface
class DisplayElement(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass


class WeatherData(Subject):
    temperature = None
    humidity = None
    pressure = None

    def __init__(self):
        self.observers = []

    def register_observer(self, obs):
        self.observers.append(obs)

    def remover_observer(self, obs):
        try:
            self.observers.remove(obs)
        except Exception as e:
            print(e)

    def notify_observer(self):
        for o in self.observers:
            o.update(self.temperature, self.humidity, self.pressure)

    def measurement_changed(self):
        self.notify_observer()

    def set_measurement(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurement_changed()


class CurrentDisplay(Observer, DisplayElement):
    temperature = None
    humidity = None

    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print('Current conditions:' + self.temperature + "C degrees and " + self.humidity + "% humidity")


class WeatherStation:
    def __init__(self):
        weather_data = WeatherData()
        current_display = CurrentDisplay(weather_data)
        weather_data.set_measurement('35', '65', '30.4f')
