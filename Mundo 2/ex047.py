from time import sleep

for c in range(1, 51):
    print('.', end=' ')
    if c % 2 == 0:
        print(c, end=' ')
        sleep(0.1)
