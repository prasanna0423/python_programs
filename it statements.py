bill=float(input("enter bill: "))
print("pay: ",bill)
print("-------------------------------")

#2
bill=float(input("enter bill: "))
discount=0.15*bill
bill=bill-discount
print("pay: ",bill)

#3
bill=float(input("enter bill: "))
if bill>=5000:
    discount=0.15*bill
    bill=bill-discount
    print("pay: ",bill)

#4
emp_name=chr(input("enter name: "))
years_exp=int(input("enter: "))
salary=45000
if years_exp>=5:
    bonus=0.20*salary
    total=bonus+salary
    print(total)

#5
bill_amount=float(input("enter bill amount: "))
member = input("Are you a member (yes/no)? ").lower() == "yes"
if member and bill_amount> 1000:
    discount=0.10*bill_amount
    total=discount-bill_amount
    print("total: ",total)
else:
    final_amount = bill_amount

#6
bill=float(input("enter bill amount: "))
person=int(input("enter how many days: "))
if person>=7:
    discount=0.15*bill
    final_bill=bill-discount
    print("final_bill: ",final_bill)
else:
    print("bill: ",bill*person)

#7
bill=float(input("enter bill amount: "))
items=int("enter quantity of items: ")
if items>20:
    discount=0.10*bill
    final_bill=bill-discount
    print("final_bill: ",final_bill)
else:
    print("final_bill: ",bill)

#8
salary = float(input("Enter salary: "))
days = int(input("Enter working days: "))
if days == 30:
    bonus = 0.05 * salary
    final_salary = salary + bonus
    print("Bonus:", bonus)
    print("Final Salary:", final_salary)
else:
    print("Final Salary:", salary)

#9
amount = float(input("Enter gym fee: "))
years = int(input("Enter membership period (in years): "))

if years >= 1:
    discount = 0.20 * amount
    total_fee = amount - discount
    print("Discount:", discount)
    print("Total gym fee:", total_fee)
else:
    print("Total gym fee:", amount)

#10
bill_amount = float(input("Enter credit card bill amount: "))
paid_amount = float(input("Enter amount paid: "))

if paid_amount >= 0.5 * bill_amount:
    cashback = 200
    daily_limit = paid_amount + cashback
    print("Cashback:", cashback)
    print("Daily limit of credit card:", daily_limit)
else:
    print("No cashback")
    print("Daily limit of credit card:", paid_amount)
    
