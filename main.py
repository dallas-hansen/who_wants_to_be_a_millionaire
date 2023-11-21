def line_break(key='*'):
    print()
    print(key * 50)
    print()

class Contestant:
    def __init__(self, name, level):
        self.name = name
        self.money = 0
        self.lifeline = {'50/50': level.fifty_fifty,
                         'Ask the audience': level.ask_the_audience,
                         'Phone Call': level.phone_call
                         }
        self.guess = ''

    def add_money(self, amount):
        self.money += amount


    def get_guess(self):
        # Asks for input, sends to lifeline if selected
        # Otherwise saves guess

        response = input().upper()
        if response == 'Y':
            self.use_a_lifeline()
        elif response in Level.choices:
            self.guess = response
        else:
            return None
        
    
    def print_lifelines(self):
        # Prints available lifelines
        # Returns available lifelines

        line_break()
        print('Lifelines available:\n')
        available_lifelines = {}
        for num, i in enumerate(self.lifeline):
            available_lifelines[num] = i
            print(f'{num + 1}: {i}')
        return available_lifelines


    def use_a_lifeline(self):
        # Executes selected lifeline
        # Deletes lifeline from options
        
        available_lifelines = self.print_lifelines()
        choice = available_lifelines[int(input('Enter number of lifeline:\n')) - 1]
        self.lifeline[choice]()
        del self.lifeline[choice]


    def check_guess(self, answer):
        if self.guess == answer:
            print('Correct!')
            return True
        else:
            print('Nope!')
            return False

class Level:
    choices = ['A', 'B', 'C', 'D']
    money_tree = {
        1 : 100,
        2 : 200,
        3 : 300,
        4 : 500,
        5 : 1_000,
        6 : 2_000,
        7 : 4_000,
        8 : 8_000,
        9 : 16_000,
        10 : 32_000,
        11 : 64_000,
        12 : 125_000,
        13 : 250_000,
        14 : 500_000,
        15 : 1_000_000
    }

    def __init__(self):
        self.round_number = 1
        self.level_amount = 100
        self.question = ''
        self.answer = ''
        self.options = ''


    def get_question(self):
        # TODO: parse CSV
        self.question = 'What is my name?'
        self.answer = 'A'
        self.options = {'A': 'Dallas',
                'B': 'Troy',
                'C': 'Bob',
                'D': 'Kevin'
                }


    def display_question(self):
        # Simply prints out the question
        line_break()
        print(f'\nQuestion {self.round_number}: {self.question}\n')
        print('Options:\n')
        for k, v in self.options.items():
            print(f'{k}: {v}')
        print('\n Or: Press Y to use a lifeline\n')


    def increase_round_and_amount(self):
        self.round_number += 1
        self.level_amount = self.money_tree[self.round_number]

    
    def fifty_fifty(self):
        print('You used 50/50')
        # TODO: Finish function


    def ask_the_audience(self):
        print('You used Ask the Audience')
        # TODO: Finish function


    def phone_call(self):
        print('You used Phone Call')
        # TODO: Finish function


def main():
    # TODO: create main loop
    level = Level()
    contestant = Contestant(input('What is your name?\n'), level)
    level.get_question()
    level.display_question()
    contestant.get_guess()
    contestant.print_lifelines()


if __name__ == '__main__':
    main()