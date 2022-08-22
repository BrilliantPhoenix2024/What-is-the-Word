list_of_words = ['moon', 'star', 'sun', 'earth', 'mars', 'hello', 'hi', 'red', 'yellow', 'computer']

def get_input():
    while True:
        user_input = input('Enter your guess: ')
        if user_input.isalpha():
            return user_input
        else:
            print('Your input is not corect please enter again.')
        
def game_help():
    print('-'*10)
    print('Wellcome to the Gussing Game.')
    print("All words: ", list_of_words)
    print('Please start to guess.')
    print('-'*10)

def run_game(number_of_rounds):
    print(game_help())
    print(f'You can guess {number_of_rounds} times.')
    corect_word = list_of_words[8]
    
    for i in range(number_of_rounds):
        user_input = get_input()
        
        if user_input == corect_word:
            print('You Won!')
            break
        else:
            print('Your guess is Wrong.')
            print(f'Please try again.number of rounds left: {number_of_rounds-1 - i}')
            
run_game(5)
       