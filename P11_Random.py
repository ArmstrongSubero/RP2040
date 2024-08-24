import random

strt = 'a'

while True:
    strt = input("Press ENTER to start, X to exit ")
    if strt.upper() != 'X':
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        print("%d  %d" % (first, second))
    else:
        break