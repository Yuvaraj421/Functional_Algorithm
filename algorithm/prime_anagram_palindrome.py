

def get_prime():
    list = []
    is_prime = True
    for i in range(1001):
        if i == 0 or i == 1:
            continue
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            list.append(i)
    return list


def PrimeCheck(no1, no2):  # Pass the No. from start till end
    count = 0
    l = []
    print("Prime No.s in a Range", no1, "And ", no2)
    for i in range(no1, no2 + 1):  # Iterate no1 to no2(i=no1;i<no2+1;i++)
        for j in range(2, i):  # Iterate (j=2;j<i;j++)
            if i % j == 0:  # No1 is divisible by 2, break
                count = 0
                break
            else:
                count = 1
        if count == 1:  # If its not divisible then append in the list
            l.append(i)

    print(l)


def get_anagram_prime():
    x = get_prime()

    x = [str(i) for i in x]
    anagram1 = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if sorted(x[i]) == sorted(x[j]):
                anagram1.append(x[i])
                anagram1.append(x[j])
    return anagram1



def isAnagram(s1, s2):
    # s1 = len(21)
    # s2 = len(31)
    s1 = len(str())
    s2 = len(str())
    if s1 != s2:
        return False
    ss1 = sorted(s1)
    ss2 = sorted(s2)
    for i in range(0, s1):
        if ss1[i] != ss2[i]:

            return False

    return True


def palin_fun():
    n = int(input("Enter number:"))
    temp = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if temp == rev:
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")


def final_out():
    # get_prime()
    # PrimeCheck(no1, no2)algorithm/prime_anagram_palindrome.py:52
    # print(get_anagram_prime())
    get_anagram_prime()
    isAnagram(12, 21)


if __name__ == '__main__':
    no1 = int(input("enter the no1"))
    no2 = int(input("enter the no2"))
    try:
        final_out()
    except Exception as e:
        # pass
        print(e)




