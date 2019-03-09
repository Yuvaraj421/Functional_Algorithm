from utilities.utility import anagram

if __name__ == '__main__':

    try:
        string1 = input("enter the string1 data \n")
        string2 = input("enter the string2 data \n")

        anagram(string1, string2)
    except Exception as e:
        print(e)
