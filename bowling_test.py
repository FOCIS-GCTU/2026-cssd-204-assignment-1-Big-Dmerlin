# File: bowling.py
# Description: This program calculates a bowler's average score and handicap
#              after three games using floor division and the standard handicap
#              formula: handicap = (200 - average) * 80%
# Assignment Number: 4
#
# Name: APPIAH-KUBI BERNARD OLOGO DMERLIN
# SID:  2425400482
# Email: 2425400482@live.gctu.edu.gh
# Grader:  Carolyn
# Slip days used in this assignment: 0
#
# On my honor, APPIAH-KUBI BERNARD OOGO DMERLIM, this programming assignment is my own work
# and I have not provided this code to any other student.

name = input("Enter your name: ")

print()

game1 = int(input("Enter Game 1: "))
game2 = int(input("Enter Game 2: "))
game3 = int(input("Enter Game 3: "))

print()

average = (game1 + game2 + game3) // 3

handicap = (200 - average) * 80 // 100

print(name + "'s average is: " + str(average))
print(name + "'s handicap is: " + str(handicap))
