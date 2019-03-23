import json
from utilities.utility import Queue

q1 = Queue()
# creating object of Queue class to access all the method present in that class
company_tran = json.load(open("transaction.json", "r"))
# opening and reading the 'company' JSON file and


# converting it to the python Dictionary storing in a variable


# this method add element to the Queue
def queue_transaction():
    for val in range(len(company_tran['transaction'])):
        time = company_tran['transaction'][val]['time']  # converting timestamp to string type
        tran_type = str(company_tran['transaction'][val]["buy_sell"])  # converting the type of transaction to string
        q1.enqueue(
            company_tran['transaction'][val]["company_symbol"] + " - " + time + " - " + tran_type)
        # concatenating
        # company symbol and the type of transaction done and queuing to the Queue
    print("\nCompanies transaction details added to the Queue")


# this function delete(de_queue) element from the Queue
def de_queue_transaction():
    de_queue = q1.dequeue()  # deleting element from the Queue
    print("\n'", de_queue, "' de_queued from the Queue\n")


# 'Transaction' as Main class
class Transaction:
    while True:
        print("enter 1.To add company transaction details to Queue")
        print("enter 2.To delete company transaction details from Queue")
        print("enter 3.To display companies transaction details from Queue")
        print("enter 4.For Exit")

        global choice
        try:
            choice = int(input("\nEnter your choice: "))
        except Exception as e:
            # handling the exception for user-input
            print(e, "add company details")
            try:
                if choice == 1:
                    queue_transaction()
                    # calling 'queue_transaction' function
                elif choice == 2:
                    de_queue_transaction()
                    # calling 'de_queue_transaction' function
                elif choice == 3:
                    print()
                    q1.show()
                    # calling 'display' function to print all the element of the Queue
                elif choice == 4:
                    print("exited")
                    exit(0)  # terminating the program
                else:
                    print("Invalid choice !!! Please Try again")
            except Exception as e:
                print(e, "\n!!! Invalid Input !!!\n")


    # from this python file only program will compile not from the imported file(s)
if __name__ == '__main__':
    s1 = Transaction()
    # creating object of 'Transaction'
