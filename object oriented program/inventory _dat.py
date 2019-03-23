import json


class Inventory:

    def inventory(self):

        try:
            # read the JSON file and store in the detail variable
            with open('inventory.json', 'r') as myfile:
                detail = json.load(myfile)

            choice = int(input("Choice \n 1.Rice \n 2.Pulse \n 3.Wheat \n Select your Choice :"))

            while True:
                if int(choice) == 1:
                    print("rice")
                    # it will calculate the rice price = weight * price_per kg  and display the calculate amount
                    for element in range(len(detail['rice'])):
                        print(detail['rice'][element], detail['rice'][element]['name'],
                              " Total amount:",
                              int(detail['rice'][element]['weight']) * int(detail['rice'][element]['price']))
                    break
                elif int(choice) == 2:
                    print("pulse")
                    # it will calculate the pulse price = weight * price_per kg  and display the calculate amount
                    for element in range(len(detail['pulse'])):
                        print(detail['pulse'][element], detail['pulse'][element]['name'],
                              " Total amount:",
                              int(detail['pulse'][element]['weight']) * int(detail['pulse'][element]['price']))
                    break
                elif int(choice) == 3:
                    print("wheat")
                    # it will calculate the wheat price = weight * price_per kg  and display the calculate amount
                    for element in range(len(detail['wheat'])):
                        print(detail['wheat'][element], detail['wheat'][element]['name'],
                              " Total amount:",
                              int(detail['wheat'][element]['weight']) * int(detail['wheat'][element]['price']))
                    break
                else:
                    print("Wrong Input")
                    break
        except ValueError as e:
            print("Input value isn't proper type")
            print(e)
        except IOError as e:
            print("File Not Found ")
            print(e)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    myInventory = Inventory()
    # this line invoked inventory method
    myInventory.inventory()
