def subtract():
    amount = int(input("Enter the due amount: "))
    paid = int(input("Enter the amount paid: "))
    
    bill_amount = amount - paid
    print("The bill remaining to be paid is", bill_amount)

subtract()