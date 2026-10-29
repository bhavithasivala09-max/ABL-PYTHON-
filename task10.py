stock = int(input("Enter available stock: "))
required = int(input("Enter required quantity: "))

if stock >= required:
    print("Stock is sufficient")
    remaining = stock - required
    print("Remaining stock =", remaining)
else:
    print("Stock is insufficient")
    shortage = required - stock
    print("Additional stock needed =", shortage)