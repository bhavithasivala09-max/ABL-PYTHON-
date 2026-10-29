distance = float(input("Distance in km: "))
travel_class = input("Class (Sleeper/AC): ").strip().lower()
count = int(input("Number of passengers: "))
if distance <= 0 or count <= 0 or travel_class not in ("sleeper", "ac"):
    print("Invalid travel details")
else:
    rate = 1 if travel_class == "sleeper" else 2
    total_fare = 0
    total_penalty = 0
    cancelled = input("Cancel reservation? (yes/no): ").lower() == "yes"
    for i in range(count):
        age = int(input(f"Age of passenger {i + 1}: "))
        if age < 0:
            print("Invalid age")
            continue
        if age < 5:
            fare = 0
        else:
            base = distance * rate
            if age >= 60:
                base *= 0.80
            fare = base + 40
        penalty = fare * 0.25 if cancelled else 0
        total_fare += fare
        total_penalty += penalty
        print("Passenger", i + 1, "fare: ", round(fare, 2),
              "cancellation penalty: ", round(penalty, 2))
    print("Total fare: ", round(total_fare, 2))
    print("Total cancellation penalty: ", round(total_penalty, 2))
    print("Estimated refund after penalty: ", round(total_fare-total_penalty, 2))