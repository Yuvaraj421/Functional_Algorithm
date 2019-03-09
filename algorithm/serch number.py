
from utilities.utility import search_number
import math
try:
    number = int(input("How much time you want me to ask the question:"))
    low = 0
    high = int(math.pow(2, number))
    print("Think a number between(", low, ")to(", high, ")in range")
    result = search_number(low, high)
    print("The number is = ", result)
except Exception as e:
    print(e)


if __name__ == '__main__':
    search_number(low, high)


