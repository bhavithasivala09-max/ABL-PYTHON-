#continues loops are running
items = []
n = int(input("Number of products: "))
if n <= 0:
    print("Enter at least one product")
else:
    subtotal = 0
    tax_total = 0
    for i in range(n):
        name = input("Product name: ")
        category = input("Category (electronics/grocery/other): ").lower()
        qty = int(input("Quantity: "))
        price = float(input("Unit price: "))
        if qty <= 0 or price < 0 or category not in ("electronics", "grocery", "other"):
            print("Invalid item; skipped")
            continue
        line = qty * price
        rate = 0.18 if category == "electronics" else 0.05 if category == "grocery" else 0.12
        items.append((name, qty, line, rate))
        subtotal += line
        discount = min(subtotal * 0.10, 500)
        discount = discount if subtotal >= 2000 else 0
        # Allocate discount proportionally across items before tax
        for name, qty, line, rate in items:
            share = (line / subtotal) * discount if subtotal else 0
            tax_total += (line - share) * rate
        total = subtotal - discount + tax_total
        print("\n--- ITEMIZED INVOICE ---")
        for name, qty, line, rate in items:
            print(name, "Qty:", qty, "Amount: ", round(line, 2),
                  "Tax rate:", int(rate * 100), "%")
        print("Subtotal: ", round(subtotal, 2))
        print("Discount: ", round(discount, 2))
        print("Tax: ", round(tax_total, 2))
        print("Final total: ", round(total, 2))