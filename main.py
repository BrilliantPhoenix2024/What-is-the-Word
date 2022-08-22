list_of_words = ['moon', 'star', 'sun', 'earth', 'mars', 'hello', 'hi', 'red', 'yellow', 'computer']

def get_input():
    while True:
        user_input = input('Enter your guess: ')
        if user_input.isalpha():
            return user_input
        print('Your input is not corect plz enter again.')
        
def game_help():
    print('-'*10)
    print('Wellcome to the Gussing Game.')
    print("All words: ", list_of_words)
    print('Please start to guess.')
    print('-'*10)
    
print(game_help())    
print(get_input())
       