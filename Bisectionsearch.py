'''
Game to illustrate concept of bisection search.
@edx Introduction to Computer Science and Programming Using Python
'''
x = 100
guessed = False
low = 0
high = x


print('Think of a number between 0 and 100.')
while not guessed:
    ans = (low + high)//2
    print('Is your secret number ' + str(ans) + '?')
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if guess == 'l':
        low = ans
    elif guess == 'h':
        high = ans
    elif guess == 'c':
        guessed = True
    else:
        print('Sorry, I did not understand your input')
print('Game over. Your secret number was: ' + str(ans))