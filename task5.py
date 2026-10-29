plans = [
    {"name": "Plan A", "price": 199, "daily": 1.5, "days": 28},
    {"name": "Plan B", "price": 299, "daily": 2.0, "days": 28},
    {"name": "Plan C", "price": 399, "daily": 2.5, "days": 56},
]
required_days = int(input("Required validity in days: "))
usage = float(input("Expected total data usage (GB): "))
budget = float(input("Budget: "))
eligible = []

if required_days <= 0 or usage < 0 or budget < 0:
    print("Enter valid values")
else:
    for p in plans:
        included = p["daily"] * p["days"]
        excess = max(0, usage - included)
        cost = p["price"] + excess * 20
        if p["days"] >= required_days and cost <= budget:
            eligible.append((cost, p["name"], excess))

    if eligible:
        eligible.sort()
        cost, name, excess = eligible[0]
        print("Most economical eligible plan:", name)
        print("Estimated cost: ", round(cost, 2))
        print("Excess data: ", round(excess, 2), "GB")
    else:
        print("No plan satisfies validity and budget constraints")