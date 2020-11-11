from abc import ABCMeta, abstractmethod


class Pizza(metaclass=ABCMeta):
    name = None
    dough = None
    sauce = None
    topping = []

    def prepare(self):
        print('Prepare ' + self.name)
        print('Tossing dough..,')
        print('Adding sauce...')
        print('Adding topping: ')
        print(' '.join(self.topping))

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza')

    def box(self):
        print('Place pizza in official')


class PizzaStore(metaclass=ABCMeta):
    @abstractmethod
    def _create_pizza(self, _type):
        pass

    def order_pizza(self, _type):
        pizza = self._create_pizza(_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYStylePizzaCheese(Pizza):
    name = 'NY Style Sauce and Cheese Pizza'
    dough = 'Thin Crust Dough'
    sauce = 'Mariana Sauce'
    topping = ['Grated Reggiano Cheese']


class NYStylePizzaPepperoni(object):
    pass


class NYStylePizza(PizzaStore):
    def _create_pizza(self, _type):
        pizza = None
        if _type == 'cheese':
            pizza = NYStylePizzaCheese()
        if _type == 'pepperoni':
            pizza = NYStylePizzaPepperoni()
        return pizza
