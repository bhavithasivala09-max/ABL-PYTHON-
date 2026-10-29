from typing import final


budget = float(input("Travel budget in home currency: "))
fee_rate = float(input("Conversion fee percentage: "))
expenses = []
n = int(input("Number of expense categories: "))
if budget < 0 or fee_rate < 0 or n <= 0:
    print("Enter valid values")
else:
    total = 0
    for i in range(n):
        category = input("Expense category: ")
        foreign_amount = float(input("Amount in foreign currency: "))
        rate = float(input("Exchange rate (home currency per 1 foreign):"))
        if foreign_amount < 0 or rate <= 0:
            print("Invalid amount or exchange rate; skipped")
            continue
        converted = foreign_amount * rate
        final = converted * (1 + fee_rate / 100)
        expenses.append((category, final))
        total += final
    if expenses:
        largest = max(expenses, key=lambda x: x[1])
        print("Total spending: ", round(total, 2))
        print("Largest expense category:", largest[0],"(amount:", round(largest[1], 2), ")")
        if total <= budget:
            print("Budget remaining:", round(budget - total, 2))
        else:
            print("Over budget by:", round(total - budget, 2))
    else:
        print("No valid expenses entered")