from abc import ABCMeta, abstractmethod


class Duck(metaclass=ABCMeta):
    flyBehavior = None
    quackBehavior = None

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self.flyBehavior.fly()

    def perform_quack(self):
        self.quackBehavior.quack()

    def set_fly_behavior(self, fb):
        self.flyBehavior = fb

    def set_quack_behavior(self, qb):
        self.quackBehavior = qb


class FlyBehavior:
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I'm cant fly")


class QuackBehavior:
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print('Quack')


class MuteQuack(QuackBehavior):
    def quack(self):
        print('<<Silence>>')


class MallardDuck(Duck):
    flyBehavior = FlyWithWings()
    quackBehavior = Quack()

    def display(self):
        print("I'm a Mallard duck")