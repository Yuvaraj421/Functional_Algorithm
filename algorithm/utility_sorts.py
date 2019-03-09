
from utilities.utility import string_binary, int_binary, insertion_sort, string_insertion_sort, bubble_sort, string_bubble_sort

number = int(input("enter the number to perform operations\n"))
if number == 1:
    string_insertion_sort()
elif number == 2:
    insertion_sort()
elif number == 3:
    string_binary()
elif number == 4:
    int_binary()
elif number == 5:
    bubble_sort()
elif number == 6:
    string_bubble_sort()
else:
    print("invalid data ")
