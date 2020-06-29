# attmp_len() func returns the no. of incorrect attempts user wants
def attmp_len():
    in_attmp = int(input('How many incorrect attempts do you want ? [1-25]: '))
    while True:
        try:
            if in_attmp > 25 or in_attmp <= 0:
                print('Not an integer between [1-25]')
            else:
                break
        except Exception as e:
            print('Incorrect input,Please Enter integer value between [1-25]')

    return in_attmp


# word() func returns the choosen random word and the guess word pattern
def word():
    import random
    words = ['rainbow', 'computer', 'science', 'programming', 
		'python', 'mathematics', 'player', 'condition', 
		'reverse', 'water', 'board', 'geeks'] 
    word = random.choice(words)
    guess = '*' * len(word)
    print(f'Your word: {guess}')

    return word, guess


# game() func returns win or lose
def game(attempts, word, guess):
    while attempts != 0:
        char = input('Guess a letter : ')
        if char in word:
            indices = []
            for i in range(len(word)):
                if word[i] == char:
                    indices.append(i)
            for i in indices:
                guess = list(guess)
                guess[i] = char
            guess = ''.join(guess)
            print(f"Correct guess : {guess}")
            if guess == word:
                won = True
                break
        else:
            attempts -= 1
            print(f'Wrong guess, attempts reamained are {attempts}')
            if attempts == 0:
                won = False
    return won


#input name and start the game
name = input('Enter your name: ')
print(f'Welcome {name} !!')
print('Starting a game of Hangman!!')

attempts = attmp_len()
word, guess = word()
game = game(attempts, word, guess)

if game:
    print('Congratulations !! You Won')
    print('Thank you for playing')
else:
    print('You lost game, Out of attemps')
    print('Thank you for playing')