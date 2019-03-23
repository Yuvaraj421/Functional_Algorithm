import json


class Stock_Account:
    def new_Account(self):

        print("Adding Account")
        data = []
        try:
            with open("customer.json", "r") as file:
                data = json.load(file)
        except Exception:
            print("File is Empty....Please add contents")
            print()
        try:
            id = input("Enter your ID:")
            if not id.isnumeric():
                raise ValueError
            else:
                for i in range(0, len(data)):
                    if data[i]['ID'] != id:
                        continue
                    else:
                        print("ID is present please enter another id")
                        exit()
            name = input("Enter your Name:")
            if not name.isalpha():
                raise ValueError
            amount = input("Enter Amount:")
            if not amount.isnumeric():
                raise ValueError
            values = {'ID': id, 'Name': name, 'Amount': amount}
            data.append(values)
            with open("customer.json", "w") as file:
                json.dump(data, file)
        except Exception:
            print("please enter proper values")

    def valueof(self):

        totalamount = 0
        print("Total Value of Account:")
        with open("customer.json", "r") as file:
            data = json.load(file)
        for i in range(len(data)):
            totalamount += int(data[i]['Amount'])
        print("Total Amount of customer Account :", totalamount)

    def buy(self):

        # this method will buy a shares of the companies which are there in company.json file

        print("Buy Company")
        data = []
        try:
            with open("customer.json", "r") as file:
                data = json.load(file)
        except Exception:
            print("File is Empty....Please add contents")
            print()
        customerdata = []
        companydata = []
        try:
            customerID = input("Enter customer ID:")
            if not customerID.isnumeric():
                raise ValueError
            else:
                flag = True
                for i in range(len(data)):
                    if customerID == data[i]['ID']:
                        print("Id is available.")
                        flag = False
                if flag:
                    print("Sorry ID is not present you can't buy.")
                    return
            companyname = input("Enter the company Name:").upper()
            if not companyname.isalpha():
                raise ValueError
            numberofshare = input("Enter number of shares to buy:")
            if not numberofshare.isnumeric():
                raise ValueError
        except Exception:
            print("Enter proper Values")
        with open("customer.json", "r") as customerfile:
            customerdata = json.load(customerfile)
        with open("company.json", "r") as companyfile:
            companydata = json.load(companyfile)
        calcutatedamount = int(companydata[companyname]['Price']) * int(numberofshare)
        for i in range(len(customerdata)):
            if customerID == customerdata[i]['ID']:
                cid_index = i
                customeramount = (customerdata[i]['Amount'])
        if int(customeramount) < int(calcutatedamount):
            print("Don't have enough amount to buy a share")
        else:
            print("total amount to be deducted from customer ID: ", customerID, " amount:",
                  int(companydata[companyname]['Price']) * int(numberofshare))
            updatedamount = int(customeramount) - int(calcutatedamount)
            customerdata[cid_index]['Amount'] = int(updatedamount)
            companydata[companyname]["Balance"] = str(int(companydata[companyname]["Balance"]) + updatedamount)
            companydata[companyname]["Share"] = str(int(companydata[companyname]["Share"]) - int(numberofshare))
            customerdata[cid_index][companyname] = numberofshare
        with open("customer.json", "w") as customerfile:
            json.dump(customerdata, customerfile)
        with open("company.json", "w") as companyfile:
            json.dump(companydata, companyfile)

    def sell(self):

        # this method will sells a customers brought company to another customer at the same  time amount will be

        print("Companies For Sale:")
        customerdata = []
        companydata = []
        with open("company.json", "r") as companyfile:
            companydata = json.load(companyfile)
        with open("customer.json", "r") as file:
            customerdata = json.load(file)
        for i in range(0, len(customerdata)):
            print(customerdata[i])
        print("Please Enter Selling Company ID for Buying that Company:")
        try:
            selling_companyID = input("Enter Selling Company ID:")
            if not selling_companyID.isnumeric():
                raise ValueError
            selling_companyName = input("Enter Company Name: ").upper()
            if not selling_companyName.isalpha():
                raise ValueError
            buyerID = input("Enter Buyers ID: ")
            if not buyerID.isnumeric():
                raise ValueError
            else:
                print("Number of Shares of Sellar ID is ",
                      customerdata[int(selling_companyID) - 1][selling_companyName])
                sharestobuy = input("Enter Number of shares to buy: ")
                if customerdata[int(selling_companyID) - 1][selling_companyName] < sharestobuy:
                    print("Sorry less number of shares available")
                else:
                    buyerAmount = int(companydata[selling_companyName]['Price']) * int(sharestobuy)
                    print("total amount to be deducted from customer ID: ", buyerID, " amount:", buyerAmount)
                    customerdata[int(buyerID) - 1]['Amount'] = customerdata[int(buyerID) - 1]['Amount'] - buyerAmount
                    customerdata[int(selling_companyID) - 1]['Amount'] = customerdata[int(selling_companyID) - 1][
                                                                             'Amount'] + buyerAmount
                    customerdata[int(buyerID) - 1][selling_companyName] = sharestobuy
                    customerdata[int(selling_companyID) - 1][selling_companyName] = str(
                        int(customerdata[int(selling_companyID) - 1][selling_companyName]) - int(sharestobuy))
                with open("customer.json", "w") as customerfile:
                    json.dump(customerdata, customerfile)
        except Exception:
            print("Enter Proper Values")

    def save(self):

        # this method will save all data to the file

        print("Your File Saved")
        # new_data = {}
        # new_data["share"] = 5
        # company_data.ap(new_data)

    def print_Report(self):

        # this method will print all the Details of each account

        with open("customer.json", "r") as file:
            data = json.load(file)
        print("Report")
        for i in range(len(data)):
            print(data[i])



if __name__ == "__main__":
    s = Stock_Account()
    try:
        while True:
            print("Enter your choice: ")
            print("1.New Account ")
            print("2.Buy Company Shares")
            print("3.Sell Company Shares")
            print("4.Value of Total Shares")
            print("5.Save")
            print("6.Print Report")
            print("7.Quit")
            choice = input()
            if not choice.isnumeric():
                raise ValueError
            if int(choice) == 1:
                s.new_Account()
                break
            elif int(choice) == 2:
                s.buy()
                break
            elif int(choice) == 3:
                s.sell()
                break
            elif int(choice) == 4:
                s.valueof()
                break
            elif int(choice) == 5:
                s.save()
                break
            elif int(choice) == 6:
                s.print_Report()
                break
            elif int(choice) == 7:
                break
            print("\n")
    except Exception as e:
        print("Enter Proper Values")
