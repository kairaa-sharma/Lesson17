
def calculate_change(total_bill, amount_paid):
    if amount_paid >= total_bill:
        change = amount_paid - total_bill
        print("Change to return : ", change, "$")
    else:
        print("Not enough money paid. ")


bill = float(input("Enter total bill amount: "))
paid = float(input("Enter amount paid: "))


calculate_change(bill, paid)