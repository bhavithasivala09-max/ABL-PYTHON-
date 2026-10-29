venue = float(input("Enter venue cost: "))
food = float(input("Enter food cost: "))
transport = float(input("Enter transport cost: "))
equipment = float(input("Enter equipment cost: "))

total = venue + food + transport + equipment

print("Total event cost =", total)

if total <= 10000:
    print("Event is within budget")
else:
    print("Event budget exceeded")