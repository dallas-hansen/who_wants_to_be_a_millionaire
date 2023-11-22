import json
import random


def line_break(key='*'):
    print()
    print(key * 50)
    print()


class Player:
    def __init__(self, name, game):
        self.name = name
        self.money = 0
        self.lifeline = {'50/50': game.fifty_fifty,
                         'Ask the audience': game.ask_the_audience,
                         'Phone Call': game.phone_call
                         }
        self.guess = ''
        self.game = game


    def add_money(self, amount):
        self.money = amount

    def back_out_chance(self):
        print(f'\nYou currently have ${self.money}.\n')
        choice = ''
        y_n = ['Y', 'N']
        while choice not in y_n:
            choice = input("Would you like to continue? (Y/N): ").upper()
        if choice == 'Y':
            return False
        else:
            print(f"\nCongratulations, {self.name}! You've won ${self.money}!\n")
            return True

    def get_guess(self):
        # Asks for input, sends to lifeline if selected
        # Otherwise saves guess
        response = ''
        while response not in Game.choices:
            if len(self.lifeline) > 0:
                self.game.display_question()
                response = input('Choose an option, or press Y to use a lifeline:\n').upper()
                if response == 'Y':
                    self.use_a_lifeline()
                elif response in Game.choices:
                    self.guess = response
                else:
                    print('\n*****Option not available, try again*****\n')
            else:
                self.game.display_question()
                response = input('Choose an option:\n').upper()
                self.guess = response
        

    def print_lifelines_with_numbers(self, add_numbers=True):
        # Prints available lifelines
        # Returns available lifelines

        line_break()
        print('Lifelines available:\n')
        available_lifelines = {}
        for num, i in enumerate(self.lifeline):
            available_lifelines[num] = i
            if not add_numbers:
                print(f'{i}')
            else:
                print(f'{num + 1}: {i}')
        return available_lifelines


    def use_a_lifeline(self):
        # Executes selected lifeline
        # Deletes lifeline from options

        available_lifelines = self.print_lifelines_with_numbers()
        choice = -1 # Initializing choice - shouldn't be an option in available_lifelines
        while choice not in available_lifelines:
            choice = int(input('\nEnter number of a lifeline: ')) - 1
        print()
        self.lifeline[available_lifelines[choice]]()
        print()
        del self.lifeline[available_lifelines[choice]]


    def check_guess(self):
        positive_exclamations = ['Bravo', 'Amazing', 'Correct', 'Ay, caramba', 'Wow', 'Congrats']
        if self.guess == self.game.answer:
            print(f'\n{random.choice(positive_exclamations)}, {self.name}!\n')
            self.add_money(self.game.level_amount)
            self.game.increase_round_and_amount()
            return False
        else:
            self.money = 0
            print(f'\nNope! Sorry! You are leaving with ${self.money}\n')
            return True

class Game:
    
    f = open('question_list.json')
    question_list = json.load(f)
    
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
        self.players = []
        self.random_numbers_used = []

    
    def add_player(self, player):
        self.players.append(player)


    def get_question(self):
        # TODO: parse JSON file
        random_number = -1
        while random_number in self.random_numbers_used or random_number == -1:
            random_number = random.randint(0, 546)
        self.random_numbers_used.append(random_number)
        data = self.question_list[random_number]        

        self.question = data['question']
        self.answer = data['answer']
        self.options = {'A': data['A'],
                'B': data['B'],
                'C': data['C'],
                'D': data['D']
                }


    def display_question(self):
        # Simply prints out the question
        self.players[0].print_lifelines_with_numbers(False)
        print(f'\nQuestion {self.round_number}: {self.question}\n')
        for k, v in self.options.items():
            print(f'{k}: {v}')
        print()


    def increase_round_and_amount(self):
        self.round_number += 1
        self.level_amount = self.money_tree[self.round_number]

    
    def fifty_fifty(self):
        print('You used 50/50')
        coupled_options = {0: 'A',
                           1: 'B',
                           2: 'C',
                           3: 'D'
                           }
        random_num = random.randint(0, 3)
        selected = []
        while coupled_options[random_num] == self.answer or len(selected) < 2:
            random_num = random.randint(0, 3)
            if coupled_options[random_num] != self.answer:
                print(selected)
                selected.append(coupled_options[random_num])
        for i in selected:
            del self.options[i]


    def ask_the_audience(self):
        print('You used Ask the Audience')
        # TODO: Finish function


    def phone_call(self):
        print('You used Phone Call')
        # TODO: Finish function


def main():
    # TODO: create main loop
    line_break('$')
    intro = ('Welcome to Who Wants to be a Millionaire!\n'
             'All the questions are taken randomly from a pool of 547.\n'
             'Get 15 questions correct, in a row, to become a Millionaire!')
    print(intro)                          
    line_break('$')

    game = Game()
    player1 = Player(input('What is your name?\n\n'), game)
    game.add_player(player1)

############################################################
    end_condition_met = False
    while end_condition_met is False and player1.money < 1_000_000:
        game.get_question()
        player1.get_guess()
        end_condition_met = player1.check_guess()
        end_condition_met = player1.back_out_chance()


if __name__ == '__main__':
    main()