#Import random library
import random

#Define main fxn
def main():
    rng()

#Define rng fxn
def rng():
    task = str(input('What is the task at hand? '))
    prob = (random.random() * 100)
    print('The likelihood of ' + task + ' is ' + format(prob, '.2f') + '%.')

main()