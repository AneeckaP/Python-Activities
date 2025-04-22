def calculate_due_amount(bill_amount, amount_paid):
  return bill_amount - amount_paid

bill_amount = float(input("Enter the bill amount: "))
amount_paid = float(input("Enter the amount paid: "))

due_amount = calculate_due_amount(bill_amount, amount_paid)
print("Due amount:", due_amount)