import random


def hangman():
    Words = ["apple", "car", "cat", "python", "house", "yellow", "computer", "bus", "park", "grass"]
    word_choice = random.choice(Words)
    lives = 10
    print("Welcome To Hangman!\nYou Have 10 Lives!\n")
    guessed = ''
    while lives > 0:

        missed = 0
        for letter in word_choice:
            if letter in guessed:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                missed = missed + 1
        if missed == 0:
            print('\n\nYou win!')
            quit()
            break
        guess = input("please guess a letter:")

        guessed = guessed + guess
        if guess not in word_choice:
            print('\nthat letter is not in this word, your lives have been decreased by 1.')
            print('please try another letter.')
            lives = lives - 1
            missed = missed + 1
            print('your new lives value is')

            print(lives)


print(hangman())