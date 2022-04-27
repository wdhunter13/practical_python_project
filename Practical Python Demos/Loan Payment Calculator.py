money_owed = float(input("How much money do you owe?"))
apr = float(input("What is the annual percentage rate?"))
payment = float(input("What will your monthly payment be?"))
months = int(input("How many months?"))

monthly_rate = apr/100/12

for i in range(months):

    interest_paid = money_owed * monthly_rate
    money_owed = money_owed * interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break



    money_owed = money_owed - payment

    print("Paid", payment, "of which", interest_paid, "was interest", end=' ')
    print("Now i owe", money_owed)