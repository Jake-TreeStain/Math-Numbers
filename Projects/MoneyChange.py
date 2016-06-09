total = float(input("Total Price: "))
paid = float(input("Amount Paid: "))

if paid < total:
    print("Customer still owes ${x}".format(x=total-paid))
else:
    print("Change of ${x}".format(x=paid-total))
