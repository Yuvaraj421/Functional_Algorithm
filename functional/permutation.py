from utilities.utility import function



def permut():
    flag = 0
    while flag == 0:
        try:
            word = list(input("enter the string\n"))
            type[word] = string1
            flag = 1
        except Exception as e:
            print("enter string only")
        for string1 in function.function(word):
            print(string1)

        function.function(word)


if __name__ == '__main__':
    try:
        permut()
    except Exception as e:
        print(e)
