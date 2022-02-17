# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants


Test task
"""
# TODO Import the necessary libraries


# TODO Write here is_palindrome function 

def Game():
    word = input("Please write a word or a sentence to check for palindrome\n")
    def isPalindrome(word):
        word = word.replace(" ", "")
        return word == word[::-1]
    if isPalindrome(word):
        print("This word is Palindrome")
    else:
        print("No, it's not")

start_game = input("Do you want to start the game? \n").lower()
while True:
    if start_game == 'yes':
        Game()
        restart = input('do you want to restart \n').lower()
        if restart == 'yes':
            pass
        else:
            print("Goodbye !")
            break
    else:
            print("Goodbye !")
            break

