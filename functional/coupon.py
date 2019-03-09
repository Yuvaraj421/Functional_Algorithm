from utilities.utility import coupon

if __name__ == '__main__':
    try:
        coupon_number = int(input("Enter the Coupon number\n"))
        coupon(coupon_number)
    except Exception as e:
        print(e)
        print("enter integer data ")
