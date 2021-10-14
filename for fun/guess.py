import random


n = random.randint(1, 99)
guess = int(input("Devine le nombre entre 1 et 99 : "))
while n != guess:
    print()
    if guess < n:
        print("Trop bas...")
        guess = int(input("Écris un nombre entre 1 et 99 : "))
    elif guess > n:
        print("Trop haut...")
        guess = int(input("Écris un nombre entre 1 et 99 : "))
    else:
        print("Trouver !")
        break
    print()
