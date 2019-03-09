from utilities.utility import triplets

try:
    size = int(input("enter the size of elements\n"))
    list1 = []
    print("enter the values")
    for i in range(0, size):
        val = int(input())
        list1.append(val)
    triplets(size, list1)
except Execption as e:
    print(e)
