import random



x = random.randint(1, 100)
while True:
    n = int(input('Number:'))
    if n == x:
        print("Congrats u get it")
        break
    elif n < x:
        print("It's bigger")
    elif n > x:
        print("It's smaller")