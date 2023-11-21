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

    
    def guess(self):
        options = ['A', 'B', 'C', 'D']
        response = input().upper()
        if self.guess == 'Y':
            use_a_lifeline()
        elif self.guess in options:
            self.guess = response
        else:
            return None
    

    def use_a_lifeline(contestant):
        print(f'You have {contestant.lifeline} left')


    def fifty_fifty(contestant):
        pass


    def ask_the_audience(contestant):
        pass


    def phone_call(contestant):
        pass


def get_question():
    # TODO: parse CSV
    question = 'What is my name?'
    answer = 'A'
    options = {'A': 'Dallas',
               'B': 'Troy',
               'C': 'Bob',
               'D': 'Kevin'
               }
    return question, options, answer


def display_question(question, options):
    # Simply prints out the question
    print(f'Question: {question}\n')
    print(f'Options:')
    for k, v in options.items():
        print(f'{k}: {v}')
    print('Press Y to use a lifeline')
    print()


def check_guess(guess, answer):
    if str(guess).upper() == answer.upper():
        print('Correct!')
        return True
    else:
        print('Nope!')
        return False

     
def main():
    # TODO: create main loop
    contestant = Contestant(input('What is your name?\n'))
    while True:
        question, options, answer = get_question()
        display_question(question, options)
        check_guess(guess(contestant), answer)
        break



if __name__ == '__main__':
    main()