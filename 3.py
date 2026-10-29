consultation = float(input("Enter consultation fee: "))
tests = float(input("Enter test charges: "))
treatment = float(input("Enter treatment charges: "))

total = consultation + tests + treatment

print("Total hospital bill =", total)

if total >= 5000:
    print("High bill")
else:
    print("Normal bill")