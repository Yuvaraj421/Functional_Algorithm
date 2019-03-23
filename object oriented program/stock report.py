class Stock:

    def __init__(self):
        # This creates constructor and initialise the variables
        self.number_of_shares = 0
        self.share_price = 0
        self.stock_total_value = 0

    def stock_data(self):
        # This contains the details of stock data
        try:
            number_of_stocks = int(input("enter the number of stocks details you want to enter\n"))
            number = 1
            # This loop takes the data till the range of stock number
            for stock_details in range(number_of_stocks):
                print("stock number = ", number)
                stock_name = input("enter the stock name\n")
                self.number_of_shares = int(input("enter the number of shares\n"))
                self.share_price = int(input("enter the share price\n"))
                print("stock", number, "details are as follows")
                # print(" ", " ", " ", "|", "|")
                # print(" ", " ", " ", "V", "V")
                print("'stock name' = ", stock_name, " 'number of shares' = ", self.number_of_shares,
                      " 'share price' = ", self.share_price)
                number += 1
                stock_value = self.number_of_shares * self.share_price
                self.stock_total_value += stock_value
                print("\n")
                print("stock value of", stock_name, "=", stock_value)
                print("-------------------------------------------------")
        except ValueError:
            print("enter valid number")
        print("=>", "The total value of stock =", self.stock_total_value)


# super class stock data is inherited
class StockValues(Stock):
    # This class is created to hold the stock values
    def __init__(self):
        # method is override
        Stock.__init__(self)
        self.stock_data_object = Stock()
        # Stock data objected is created

    def stock_values(self):
        self.stock_data_object.stock_data()
        # Stock data method is called


stock_value_object = StockValues()
# Stock value object is created

if __name__ == '__main__':
    try:
        stock_value_object.stock_values()
        # Stock value method is called
    except UnboundLocalError:
        print("enter valid data")
