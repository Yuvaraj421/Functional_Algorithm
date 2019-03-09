from utilities.utility import merge_sort, merge_sort1

if __name__ == '__main__':
    m = int(input("Enter the number of Elements"))
    print("Enter the elements")
    arr = [(input()) for i in range(m)]
    merge_sort(arr)

