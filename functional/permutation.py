from utilities.utility import permut

if __name__ == '__main__':
    try:
        var1 = "ABC"
        var2 = list(var1)
        print(var2)
        j = 0
        permut(var2, j)
    except Exception as e:
        print(e)
