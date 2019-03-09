from utilities.utility import gambler_method

try:
    stake = int(input("enter the stake value  "))
    goals = int(input("enter the goal value "))
    trails = int(input("enter the number of trails"))
    gambler_method(stake, goals, trails)

except Exception as e:
    print(e)
    print("enter integer number")
