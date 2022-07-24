import random

low = 1
high = 0
print("Welcome to the number guessing game!")
while True:
    try:
        low = int(input("Please input your lower bound: "))
        break
    except ValueError:
        print("Invalid input.")

while not low < high:
    try:
        high = int(input("Please input your higher bound: "))
        if low > high or low == high:
            print("You've input an invalid range")
    except ValueError:
        print("Invalid input.")

print("A random number between {} and {} will be generated".format(low,high))
x = random.randint(int(low),int(high))
guess = input("Please guess a number: ")
while guess != x:
    try:
        guess = int(guess)
        if guess == x:
            break
        elif guess > high or guess < low:
            temp = "Your guess is invalid. "
        elif guess < x:
            if guess > low:
                low = guess
            temp = "The number is higher than your guess. "
        elif guess > x:
            if guess < high:
                high = guess
            temp = "The number is lower than your guess. "
    except ValueError:
        temp = "Your guess is invalid. "
    guess = input(temp + "Please guess a new number between {} and {}: ".format(low, high))
print("Congraduations! You've successfully guessed the number!")