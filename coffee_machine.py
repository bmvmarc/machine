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
        self.status = 'initial'

    def state(self):
        print('\nThe coffee machine has:\n'
              f'{self.available["water"]} of water\n'
              f'{self.available["milk"]} of milk\n'
              f'{self.available["coffee"]} of coffee beans\n'
              f'{self.available["cups"]} of disposable cups\n'
              f'{self.cash} of money\n')

    def buy(self, kind):

        if kind == 'back':
            self.status = 'initial'
            return

        kind = 'espresso' if kind == '1' else 'latte' if kind == '2' else 'cappuccino' if kind == '3' else ''

        if not kind:
            return
        else:
            self.status = 'initial'

        lack = [k for k, v in self.ingredients[kind].items() if v > self.available[k]]

        if lack:
            print('Sorry, not enough {0}!\n'.format(', '.join(lack)))
        else:
            print('I have enough resources, making you a coffee!\n')
            for k, v in self.ingredients[kind].items():
                self.available[k] -= v

            self.cash += self.prices[kind]

    def take(self):
        print(f'I gave you ${self.cash}\n')
        self.cash = 0

    def process(self, entry):
        if self.status == 'initial':
            if entry == 'buy':
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
                self.status = 'choose_coffee'

            elif entry == 'fill':
                print('\nWrite how many ml of water you want to add:')
                self.status = 'enter_water'

            elif entry == 'take':
                self.take()

            elif entry == 'remaining':
                self.state()

        elif self.status == 'choose_coffee':
            self.buy(entry)

        elif self.status == 'enter_water':
            try:
                self.available['water'] += int(entry)
                print('Write how many ml of milk you want to add:')
                self.status = 'enter_milk'
            except ValueError:
                print('Failed to add the ingredient. Try again')

        elif self.status == 'enter_milk':
            try:
                self.available['milk'] += int(entry)
                print('Write how many grams of coffee beans you want to add:')
                self.status = 'enter_coffee'
            except ValueError:
                print('Failed to add the ingredient. Try again')

        elif self.status == 'enter_coffee':
            try:
                self.available['coffee'] += int(entry)
                print('Write how many disposable coffee cups you want to add:')
                self.status = 'enter_cups'
            except ValueError:
                print('Failed to add the ingredient. Try again')

        elif self.status == 'enter_cups':
            try:
                self.available['cups'] += int(entry)
                self.status = 'initial'
            except ValueError:
                print('Failed to add the ingredient. Try again')

        if self.status == 'initial':
            print('Write action (buy, fill, take, remaining, exit):')


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

ent = ''
while ent != 'exit':
    coffee_machine.process(ent)
    ent = input()
