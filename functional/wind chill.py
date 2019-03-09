from utilities.utility import windchill

if __name__ == '__main__':
    try:
        temperature = float(input("enter the temperature \n"))
        wind_speed = float(input("enter the speed of the wind \n"))
        windchill(temperature, wind_speed)

    except Exception as e:
        print(e)
        print("do not enter character value")
