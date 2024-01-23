import random

def prime():
    number =[]
    #for num in range(50):
    num = random.randint(0, 50)
    # num = input()
    primenum = False
    if num == 1:
        print(f'{num} is not a prime number')
    elif num > 1:
        for i in range(2,num):
            if num % i == 0:
                primenum = True
                break
        if primenum:
            print(f'{num} is a not a prime number')
        else:
            print(f'{num} is a prime number')
prime()        