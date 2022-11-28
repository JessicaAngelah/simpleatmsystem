import time as t

username = "Jessica"
pin = 1234
balance = 75293
custlist = []

while (True):
    print("\t\t1. Administrator")
    print("\t\t2. Customer")
    role = int(input("Please enter number to proceed your role > "))
    print("\n")

    if role == 1:
        print("Welcome admin. How can we help you?")
        print("\t\t1. add customer")
        print("\t\t2. delete customer")
        print("\t\t3. edit customer")
        print("\t\t4. search customer")
        admin = int(input("Enter number to proceed > "))
        print("\n")
        if admin == 1:
            fname = input("Please Enter First Name:")
            lname = input("Please Enter Last Name:")
            custlist.append(fname + lname)
            print(custlist)
            print("\n")
        elif admin == 2:
            delet = input("Please enter the customer's first and last name:")
            custlist.remove(delet)
            print(custlist)
            print("\n")
        elif admin == 3:
            print(custlist)
            edit = int(input("Please enter the index you want to edit in the list:"))
            newfname = input("Please Enter The New First Name:")
            newlname = input("Please Enter The New Last Name:")
            new = newfname + newlname
            custlist[edit] = new
            print(custlist)
            print("\n")
        elif admin == 4:
            search = input("Please enter the first and last name you want to search:")
            if search in custlist:
                print('Exist')
            else:
                print('Not exist')
            print("\n")
        else:
            print("Invalid input!")
            print("Please re-enter number")
        continue

    # ==============================================================================

    elif role == 2:
        print("Welcome", username, "How can we help you?")
        print("\t\t1. View Account Balance")
        print("\t\t2. Withdraw Cash")
        print("\t\t3. Deposit Cash")
        cust = int(input("Enter number to proceed > "))
        print("\n")

        if cust in (1, 2, 3):
            num_of_tries = 3
            while (num_of_tries != 0):
                inputpin = int(input("Please enter your 4-digit PIN > "))
                print("\n")

                if inputpin == pin:
                    print("Account auhtorized!")
                    print("\n")

                    if cust == 1:
                        print("Loading Account Balance...")
                        t.sleep(1.5)
                        print("Your current balance is $", balance)
                        print("\n")
                        break
                    elif cust == 2:
                        print("Opening Cash Withdrawal...")
                        t.sleep(1.5)

                        while (True):
                            withdraw = float(input("Enter the amount you wish to withdraw > "))

                            if withdraw > balance:
                                print("Can't withdraw $", withdraw)
                                print("Please enter a lower amount!")
                                continue

                            else:
                                print("Withdrawing $", withdraw)
                                confirm = input("Confirm? Y/N > ")
                                if confirm in ('Y', 'y'):
                                    balance -= withdraw
                                    print("Amount withdrawn - $", withdraw)
                                    print("Remaining balance - $", balance)
                                    break

                                else:
                                    print("Cancelling transaction...")
                                    t.sleep(1)
                                    print("Transaction Cancelled!")
                                    break
                        print("\n")
                        break

                    elif cust == 3:
                        print("Loading Cash Deposit...")
                        t.sleep(1.5)

                        deposit = float(input("Enter the amount you wish to deposit > "))
                        print("Depositing $", deposit)
                        confirm = input("Confirm? Y/N > ")
                        if confirm in ('Y', 'y'):
                            balance += deposit
                            print("Amount deposited - $", deposit)
                            print("Updated balance - $", balance)
                        else:
                            print("Cancelling transaction...")
                            t.sleep(1)
                            print("Transaction Cancelled!")
                        print("\n")
                        break
                    else:
                        print("Invalid input!")
                        print("Please re-enter number")
                        print("\n")
                    continue
    # ==============================================================================
    else:
        print("Invalid input!")
        print("Please re-enter number")
        print("\n")
    continue