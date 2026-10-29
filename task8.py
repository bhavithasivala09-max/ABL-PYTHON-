units = int(input("Units produced: "))
material_unit = float(input("Material cost per unit: "))
wastage_rate = float(input("Wastage percentage: "))
labour = float(input("Total labour cost: "))
machine = float(input("Machine cost: "))
selling_price = float(input("Selling price per unit: "))
target = float(input("Target profit percentage on cost: "))
values = [material_unit, wastage_rate, labour, machine, selling_price, target]
if units <= 0 or any(v < 0 for v in values):
    print("Enter valid non-negative values and positive units")
else:
    material = units * material_unit 
    wastage = material * wastage_rate / 100
    total_cost = material + wastage + labour + machine
    revenue = units * selling_price
    profit = revenue - total_cost
    margin = profit / total_cost * 100 if total_cost else 0
    print("Material cost: ", round(material, 2))
    print("Wastage cost: ", round(wastage, 2))
    print("Total production cost: ", round(total_cost, 2))
    print("Revenue: ", round(revenue, 2))
    print("Profit/Loss: ", round(profit, 2))
    print("Profit on cost: ", round(margin, 2), "%")
    print("Target achieved" if margin >= target else "Target not achieved")