def check_guess(guess, answer):
    if str(guess).upper() == answer.upper():
        print('Correct!')
        return True
    else:
        print('Nope!')
        return False


def next_question():
    pass


class Contestant:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.lifeline = ['50/50',
                         'Ask the audience',
                         'Phone Call']
        self.guess = ''

    def add_money(self, amount):
        self.money += amount


    def get_guess(self):
        # Asks for input, sends to lifeline if selected
        # Otherwise saves guess

        options = ['A', 'B', 'C', 'D']
        response = input().upper()
        if response == 'Y':
            self.use_a_lifeline()
        elif response in options:
            self.guess = response
        else:
            return None


    def use_a_lifeline(contestant):
        pass


    def fifty_fifty(contestant):
        pass


    def ask_the_audience(contestant):
        pass


    def phone_call(contestant):
        pass


class Level:
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
        self.level_amount = 0
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
        print(f'\nQuestion {self.round_number}: {self.question}\n')
        print('Options:\n')
        for k, v in self.options.items():
            print(f'{k}: {v}')
        print('\nPress Y to use a lifeline\n')


def main():
    # TODO: create main loop
    contestant = Contestant(input('What is your name?\n'))
    level = Level()
    level.get_question()
    level.display_question()


if __name__ == '__main__':
    main()