import json


class Node:
    try:

        def __init__(self, value):

            # param data elements inserted into node using data attribute

            self.data = value
            self.next = None

        def getData(self):
            return self.data

        def getNext(self):
            return self.next

        def setData(self, new_value):
            new_value = []
            self.data = new_value

        def setNext(self, new_next):
            self.next = new_next

    except ValueError as e:
        print(e)


# this class shows implementation of the ordered linked list


class LinkedList:

    def __init__(self):
        # it's constructor of linked
        self.head = None

    def is_empty(self):

        # this block check the linked list

        return self.head is None

    def get_by_index(self, index):

        # this block take index of the data in the linked list

        temp = self.head
        for i in range(index):
            temp = temp.getNext()
        return temp.getData()

    def add(self, data):

        # this block add the element of the company in the linked list

        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):

        # this block check the size of the linked list

        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.getNext()
        return count

    def search_node(self, value):

        # this block search for company name

        temp = self.head
        while temp:
            if temp.getData()['company_name'] == value:
                return True
            temp = temp.getNext()
        return False

    def get_first(self):

        # this block track the first element from the linked list

        temp = self.head
        if temp is not None:
            self.head = temp.getNext()
            return temp.getData()
        return None

    def remove_node(self, value):

        # it will remove searched company name

        prev = None
        temp = self.head
        while temp:
            if temp.getData()['company_name'] == value:
                if prev:
                    prev.setNext(temp.getNext())
                else:
                    self.head = temp.getNext()
                return True

            prev = temp
            temp = temp.getNext()

        return False

    def print_node(self):

        # this block print the company detail

        current = self.head
        print("Display Element :")
        while current != None:
            print(current.data)
            current = current.getNext()


    def new_company_add(self):

        # this block add the company details into
        # the JSON file
        # company details like company_name,number_of share and per_share_cost

        try:
            with open('ListCompanyShare_Linked_List.json', 'r') as myfile:
                customer_details = json.load(myfile)
            company_name = input("Enter comapny name : ").capitalize()
            if not company_name.isalpha():
                raise ValueError
            number_of_share = input("Enter Number of Share you want to add: ")
            if not number_of_share.isnumeric():
                raise ValueError
            per_share_cost = input("Enter Cost of share price:")
            if not per_share_cost.isnumeric():
                raise ValueError

            details = {'company_name': company_name, 'number_of_share': number_of_share,
                       'per_share_cost': per_share_cost}
            customer_details.append(details)

            with open('ListCompanyShare_Linked_List.json', 'w') as myfile:
                json.dump(customer_details, myfile)
            print("Company Details Added in the file")

        except ValueError:
            print("Entered Input Improper type")
        except IOError:
            print("File Not Found")

    def remove_company(self):

        try:
            with open('ListCompanyShare_Linked_List.json', 'r') as my_file:
                company_details = json.load(my_file)

            print("Company Details")
            for element in company_details:
                print(element)
            company_name = input("Enter Company name to remove :").capitalize()
            if not company_name.isalpha():
                raise ValueError
            flag1 = True
            company_index = 0

            for element in range(len(company_details)):

                if company_details[element]['company_name'] == company_name:
                    company_index = element
                    print("Conform Your Details ", company_details[company_index]['company_name'])
                    print("Company Name :", company_details[company_index]['number_of_share'])
                    print("Company Name :", company_details[company_index]['per_share_cost'])
                    flag1 = False
            if flag1:
                print("this name of company isn't present in the file ! Plz enter correct company of the  name !!")
                exit()
            search_company_name = my_linked_list.searchNode(company_name)
            print("Successfully Company removed from the file :", search_company_name)
            my_linked_list.remove_node(company_name)
            my_linked_list.print_node()

            temp = []
            size = my_linked_list.size()
            for i in range(size):
                temp.append(my_linked_list.getFirst())
            with open('ListCompanyShare_Linked_List.json', 'w') as my_file:
                json.dump(temp, my_file)

        except ValueError:
            print("Entered input is Improper type")
        except IOError:
            print("File Not Found")


if __name__ == '__main__':
    # main method
    try:
        my_linked_list = LinkedList()

        with open('ListCompanyShare_Linked_List.json', 'r') as myfile:
            company_details = json.load(myfile)

        for element in company_details:
            my_linked_list.add(element)
        #  my_linked_list.printNode()
        choice = int(input("Choice  \n 1.Add_new_Company \n 2.Remove_Company \n"
                           " 3.Print Company Details Reports \n 4.Quit \n Select your Choice :"))

        while True:
            if choice == 1:
                my_linked_list.new_company_add()
                break
            elif choice == 2:
                my_linked_list.remove_company()
                break
            elif choice == 3:
                my_linked_list.print_node()
                break
            elif choice == 4:
                exit()
                break
            else:
                print("Wrong Input")
                break

    except IOError as e:
        print("File not found")
        print(e)
    except Exception as e:
        print(e)
