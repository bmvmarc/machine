class CoffeeMachine:
    """ Simulates a coffee machine. """

    def __init__(self, water, milk, coffee, cups, cash):
        self.ingredients = {'espresso': {'water': 250, 'coffee': 16, 'cups': 1},
                            'latte': {'water': 350, 'milk': 75, 'coffee': 20, 'cups': 1},
                            'cappuccino': {'water': 200, 'milk': 100, 'coffee': 12, 'cups': 1}
                            }

        self.prices = {'espresso': 4,
                       'latte': 7,
                       'cappuccino': 6
                       }

        self.available = {'water': water, 'milk': milk, 'coffee': coffee, 'cups': cups}
        self.cash = cash

    def state(self):
        print('The coffee machine has:\n'
              f'{self.available["water"]} of water\n'
              f'{self.available["milk"]} of milk\n'
              f'{self.available["coffee"]} of coffee beans\n'
              f'{self.available["cups"]} of disposable cups\n'
              f'{self.cash} of money\n')

    def buy(self):
        kind = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu::\n')
        kind = 'espresso' if kind == '1' else 'latte' if kind == '2' else 'cappuccino' if kind == '3' else ''

        if not kind:
            return

        lack = [k for k, v in self.ingredients[kind].items() if v > self.available[k]]

        if lack:
            print('Sorry, not enough {0}!\n'.format(', '.join(lack)))
        else:
            print('I have enough resources, making you a coffee!\n')
            for k, v in self.ingredients[kind].items():
                self.available[k] -= v

            self.cash += self.prices[kind]

    def fill(self):
        try:
            self.available['water'] += int(input('Write how many ml of water you want to add:\n'))
            self.available['milk'] += int(input('Write how many ml of milk you want to add:\n'))
            self.available['coffee'] += int(input('Write how many grams of coffee beans you want to add:\n'))
            self.available['cups'] += int(input('Write how many disposable coffee cups you want to add:\n'))
        except ValueError:
            print('Failed to add ingredients. Try again')

    def take(self):
        print('I gave you ${self.cash}')
        self.cash = 0

    def start(self):
        action = ''
        while action != 'exit':
            action = input('Write action (buy, fill, take, remaining, exit):\n')
            if action in ('buy', 'fill', 'take'):
                getattr(self, action)()
            elif action == 'remaining':
                self.state()


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.start()
