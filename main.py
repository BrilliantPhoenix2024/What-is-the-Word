def get_input():
    while True:
        user_input = input('Enter your guess: ')
        if user_input.isalpha():
            return user_input
        print('Your input is not corect please enter again.')
    
        
def get_input_from_list(words):
    user_input = get_input()
        
    while user_input.lower() not in words:
        print('Please enter a word from the given list.')
        user_input = get_input()
    
    return user_input.lower()    
        
def game_help():
    print('-'*10)
    print('Wellcome to the Gussing Game.')
    print("All words: ", list_of_words)
    print('Please start to guess.')
    print('-'*10)


def run_game(number_of_rounds, words):
    print(game_help())
    print(f'Number of guess: {number_of_rounds}')
    corect_word = words[8]
    
    for i in range(number_of_rounds):
        user_input = get_input_from_list(words)
       
        if user_input == corect_word:
            print('You Won!')
            return
        else:
            print('Your guess is Wrong.')
            print(f'Please try again.number of rounds left: {number_of_rounds-1 - i}')
    print('You Lost!')   
   
    
list_of_words = ['moon', 'star', 'sun', 'earth', 'mars', 'hello', 'hi', 'red', 'yellow', 'computer']        

run_game(5, list_of_words)
       