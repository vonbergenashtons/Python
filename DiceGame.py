from random import randint
from time import sleep

def get_user_guess():
    guess = int(input("Please enter your guess: "))
    return guess

def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print('\nThe maximum value of the rolls is: %d' % (max_val))
    guess = get_user_guess()
    if (guess > max_val):
      print("Guess is larger than the maximum value of two dice.")
    else:
      print("Rolling...\n")
      sleep(2)
      print("First dice roll is... %d!" % (first_roll))
      sleep(1)
      print("Second dice roll is... %d!" % (second_roll))
      sleep(1)
      total_roll = first_roll + second_roll
      print("Total of both rolls is: %d" % (total_roll))
      print("Result...")
      sleep(1)
      if (total_roll == guess):
        print("You won!!!")
      else:
        print("You lost... play again!")
    
roll_dice(6)