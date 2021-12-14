import random
# library that we use in order to choose
# on random words from a list of words
def juego():
    b=print('HEY!')
name = input("What is your name? ")
# Here the user is asked to enter the name first
 
print("Good Luck ! ", name)
 
sports = ['basketball','football','baseball','volleyball','hockey','tennis']
colours=['yellow','black','red','blue','green','grey']
fruit=['apple','banana','orange','melon','watermelon','pear'] 

word = random.choice(sports)
word = random.choice(fruit)
word = random.choice(colours)
 
 
print("Guess the characters")
print(f'The next category is :Sports  ') 
print(f'The next category is colours')
print(f'The next category is: fruit')
guesses = ''
 

turns = 12
 
 
while turns > 0:
     
    failed = 0
     

    for char in word:
        if char in guesses:
            print(char)
             
        else:
            print("_",)
             
            failed += 1
    if failed == 0:
        print("You Win")
         

        print("The word is: ", word)
        break
     
    guess = input("guess a character:")
     
    guesses += guess
     
    if guess not in word:
         
        turns -= 1
         
        print("Wrong")
         
        print("You have", + turns, 'more guesses')
         
         
        if turns == 0:
            print("You Loose")



a=input('Would you like to play again?y/n')
if a=='y':
    a=name
else:
    a=='n'
    print('Thanks for playing our game!!!!')