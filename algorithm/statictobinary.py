from utilities.utility import to_binary

if __name__ == '__main__':

    try:
        number = int(input("enter the number\n"))
        to_binary(number)
    except Exception as e:
        print(e)
