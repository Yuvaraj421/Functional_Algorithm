from utilities.utility import Stacklinked
import datetime
import json

stack1 = Stacklinked()
# object is created for stack


class Per_son:
    # this class is created to add the stock by admin and
    # insertion and deletion of users are implemented by stack

    try:
        def __init__(self):
            with open("stock.json", "r") as stock_jf:
                stock_jf = json.load(stock_jf)
                # load() convert file into python from json

            self.stock_jf = stock_jf
            with open("customers.json", "r") as person_json_value:
                person_json_value = json.load(person_json_value)
            self.person_json_value = person_json_value

        def show_shares(self):
            for number_of_shares in range(len(
                    self.stock_jf['Stock Report'])):
                # Iterating through Stock Report by means of checking the length
                print(number_of_shares, self.stock_jf['Stock Report'][number_of_shares])

        def check_validity(self):
            try:
                number = 0
                name = input("Enter Username\n")

            # while number < len(self.person_json_value["Person"]):  # Creating the user for buying or selling a shares
            # if self.person_json_value["Person"][number]["Name"] == name.title():  # Verifying the user
                index = number
                print(self.person_json_value[number])
                print("....Login successful....")
                read_input = int(input("1:Buy shares\n2:Sell shares:\n"))
                if read_input == 1:
                    person_object.buy_share(index, name)
                elif read_input == 2:
                    person_object.sell_share(index, name)
                else:
                    print("wrong Input")
                number += 1
            except Exception as e:
                print(e)


        def add_new_company(self):
            # Add a new company by adding a new through dictionary
            name = input("Enter company name\n")
            number = int(input("Enter Your Number of share\n"))
            price = int(input('Enter Your Price per share\n'))
            new_stock_dict = {"Stock Name": name,
                              # created the dictionary for a new values

                              "Number of Share": number,

                              "Share Price": price}

            with open('stock.json', 'w') as stock_jf:
                # Add a new file in a json through a key
                self.stock_jf['Stock Report'].append(new_stock_dict)

                stock_jf.write(json.dumps(self.stock_jf, indent=2))
                # Writing a file through python to json

        def buy_share(self, index, name):
            # this method is used to buy shares
            for stock_report in range(len(self.stock_jf['Stock Report'])):
                print(stock_report, self.stock_jf['Stock Report'][stock_report])

            print('Enter Which Company Share you want to buy\n')
            choice = int(input("Enter choice\n"))
            buy_share = int(input("Enter Number of Share You want to buy\n"))
            each_share_price = self.stock_jf['Stock Report'][choice]['Share Price']
            # Asking for a user to sell shares among indexing
            amount_pay = buy_share * each_share_price
            # Calculating the share that are purchasing

            if self.person_json_value['Person'][index]["Total Balance"] > amount_pay:
                # Balance should be there while purchasing
                print("Total amount you have to pay for ", buy_share, " stocks : ", amount_pay, "\n")
                updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] - buy_share
                # Updating the stock
                with open("stock.json", "w") as jf:  # Changing the updated stock in a file
                    self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                    jf.write(json.dumps(self.stock_jf, indent=2))

                person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] - amount_pay
                # Subtracting the new share amount from a balance
                print('Now Your Updated Balance is ', person_updated_balance, "\n")
                person_updated_share = self.person_json_value['Person'][index]['Number of Share'] + buy_share
                # Adding the new shares in a stock
                print('Now Your Updated Number of share is ', person_updated_share, "\n")
                dt = datetime.datetime.now()
                stack1.push(
                    ("Buy", self.stock_jf["Stock Report"][choice]["Stock Name"], "Number of shares : ", buy_share))

                with open("stack_transaction.txt", "a")as txt:
                    # to append the data to the file
                    txt.write(name + str(stack1.show()) + str(dt) + "\n")
                print("stack show\n")
                stack1.show()
                stack1.push("Brought")
                stack1.show()
                with open("customers.json", "w") as jf:
                    self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                    self.person_json_value['Person'][index]['Number of Share'] = person_updated_share
                    jf.write(json.dumps(self.person_json_value))
            else:
                print("You Don't have enough money \n")

        def sell_share(self, index, name):
            # this method is used to show the share
            print('Enter choice to sell your share to particular company\n')
            for share in range(len(self.stock_jf['Stock Report'])):
                print(share, self.stock_jf['Stock Report'][share])

            choice = int(input("Enter choice in Int\n"))

            print('Enter Number of share you want to sell to', self.stock_jf['Stock Report'][choice]['Stock Name'],
                  'company\n')
            sell_share = int(input("Number of shares to sell \n"))
            updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] + sell_share

            with open("stock.json", "w") as jf:
                # open file to write and dump
                self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                jf.write(json.dumps(self.stock_jf, indent=2))

            updated_person_share = self.person_json_value['Person'][index]["Number of Share"] - sell_share
            # person share price is updated
            person_share_price = int(input("price for per share you want from company\n"))
            person_updated_balance = self.person_json_value['Person'][index][
                                         "Total Balance"] + person_share_price * sell_share

            print(' --> ', person_share_price * sell_share, '<--will be Added to your total balance\n')
            print('Now Your Updated Balance is ', person_updated_balance, "\n")

            print('Now Your Updated Number of share is ', updated_person_share, "\n")
            st = datetime.datetime.now()
            # to show the user date for entering details

            stack1.push(("Sold", self.stock_jf["Stock Report"][choice]["Stock Name"], "Number of shares :", sell_share))

            with open("stack_transaction.txt", "a")as txt:
                txt.write(name + str(stack1.show()) + str(st) + "\n")
            print("stack show")
            stack1.show()
            stack1.push("Sold")
            stack1.show()

            with open("customers.json", "w") as jf:
                # open file to write the details
                self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                self.person_json_value['Person'][index]['Number of Share'] = updated_person_share
                jf.write(json.dumps(self.person_json_value, indent=2))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    person_object = Per_son()
    # person object is created
    person_object.show_shares()
    print("\n")
    try:
        read_input_1 = int(input("1: Admin Login or 2: User \n"))
        if read_input_1 == 1:
            # If user selects as Admin
            print("welcome Admin")
            read_input_2 = int(input("press 1 to add Company :\n"))
            if read_input_2 == 1:
                person_object.add_new_company()
        elif read_input_1 == 2:
            # if user selects as User
            print("fill your details\n")
            person_object.check_validity()

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid Value")
