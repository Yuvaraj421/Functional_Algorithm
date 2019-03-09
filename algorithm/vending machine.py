def vending_machine(rupees):
    # enter the rupee notes
    money = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    # initialize note as zero
    note = 0
    for i in range(len(money)):
        # // is used to generate integer value
        if rupees // money[i] > 0:
            print("number of notes in ", money[i], "is ", rupees // money[i])
            note = note + (rupees // money[i])
            rupees = rupees % money[i]
            # reminder is generated and assigned to rupee


    print("number of notes are ", note)


if __name__ == '__main__':

    try:
        rupees = int(input("enter the rupees\n"))
        vending_machine(rupees)
    except Exception as e:
        print(e)
