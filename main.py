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

def run_game():
    print(game_help())
    print('You can guess 5 times.')
    corect_word = list_of_words[8]
    
    for i in range(5):
        user_input = get_input()
        
        if user_input == corect_word:
            print('You Won!')
            break
        else:
            print('Your guess is Wrong.')
            print(f'Please try again.You can guess {4 - i} times.')
            
run_game()
       