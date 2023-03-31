#-------------------------------------------------------------------------------
# Name:        guess number
# Purpose:
#
# Author:      lalit
#
# Created:     31/03/2023
# Copyright:   (c) lalit 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def guess_number(a):
    num = random.randint(1,a)
    total_lives = 5
    lives = 5
    while True:
        user_input = int(input(f"What's your guess number?[1-{a}]: "))
        lives -=1

        if user_input > num:
            print(f"It's high!, Try again!\n you have {lives} lives")

        elif user_input < num:
            print(f"It's low!, Try again!\n you have {lives} lives")

        elif user_input == num:
            print(f"You have guessed it! {num} \nwith {lives} lives left!")
            break
        if lives == 0:
            print("___________________________________________________")
            print("\n\tSoory!\n")
            print(f"You are out of lives! {lives} out of {total_lives}")
            print(f"\nCorrect number is {num}")
            print("___________________________________________________")

            break

a = int(input("Enter the range you wanna guess: "))

guess_number(a)
