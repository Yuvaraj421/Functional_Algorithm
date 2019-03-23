from datetime import date
import re


def regular_expression():
    today = date.today()
    try:
        name = input("Enter your name: ").capitalize()
        if not name.isalpha():
            raise ValueError
        fullName = input("Enter your full name: ").capitalize()
        if fullName.isspace() and fullName.isalpha():
            raise ValueError
        phoneNumber = input("Enter your phone number: ")
        if not phoneNumber.isnumeric():
            raise ValueError
        if len(phoneNumber) > 10 or len(phoneNumber) < 10:
            raise ValueError
        currentDate = today.strftime("%d/%m/%Y")
        string = "Hello <<name>>, We have your full name as <<full name>> in our system.Your contact number is " \
                 "91-xxxxxxxxxx." \
                 "Please,let us know in case of any clarification Thank you bridge labs xx/xx/xxxx."
        patternName = re.sub(r"<+....>+", name, string)
        pattern_fullName = re.sub(r"<+....\s....>+", fullName, patternName)
        patternPhoneNumber = re.sub(r"x{10}", phoneNumber, pattern_fullName)
        patternDate = re.sub(r"xx\Sxx\Sx{4}", currentDate, patternPhoneNumber)
        print(patternDate)
    except Exception as e:
        print("Please Enter Proper Values")


class RegularExpression:
    pass


if __name__ == "__main__":
    myClass = RegularExpression()
    regular_expression()
