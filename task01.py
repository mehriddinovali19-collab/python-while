from random import randint
 
random_number = randint(1, 20)

user_guess = None 

while True:
    user_guess = int(input(" Enter a number from 1 to 20: "))
    if user_guess < random_number:
        print("Kattarooq son!")
    elif user_guess > random_number:
        print(" kichikroq son kiriting! ")
    else:
        print("To'g'ri topdingiz!")
        break 