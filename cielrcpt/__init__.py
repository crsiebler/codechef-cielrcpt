import sys
import math

input = sys.stdin.readlines()
t = int(input[0])
for i in range(t):
    count = 0
    value = int(input[i + 1])

    while value > 0:
        count += 1
        baseTwoPower = int(math.floor(math.log(value, 2)))

        if baseTwoPower > 11:
            baseTwoPower = 11

        value = value - 2 ** (baseTwoPower)

    print(str(count))