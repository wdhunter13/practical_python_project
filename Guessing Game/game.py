import random

greet = input("Hello, what is your name?"" ")

random_number = random.randint(1,100)

greet2 = 'Hello'' '+ greet +' ''I am thinking of a number 1-100. Now...'
print(greet2)


run = True
while run:


    guess = int(input("Guess a number"))


    if guess < random_number:
        print("Your number is too low. Try again")
        
        
    
    elif guess > random_number:
        print("Your number is too high. Try again")
        

    else:
        print("Winner Winner Chicken Dinner!")
        run = False







