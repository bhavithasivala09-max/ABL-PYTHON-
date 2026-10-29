basic = float(input("Basic salary: "))
hours = float(input("Overtime hours: "))
incentive = float(input("Incentive: "))
if basic < 0 or hours < 0 or incentive < 0:
    print("Inputs cannot be negative")
else:
    hra = basic * 0.20
    da = basic * 0.10
    overtime = hours * 200
    gross = basic + hra + da + overtime + incentive
    deduction = 0
    deduction += max(0, min(gross, 40000) - 20000) * 0.05
    deduction += max(0, gross - 40000) * 0.10
    net = gross - deduction
    print("\n--- SALARY STATEMENT ---")
    print("Basic: ", round(basic, 2))
    print("HRA: ", round(hra, 2), " DA: ", round(da, 2))
    print("Overtime: ", round(overtime, 2))
    print("Incentive: ", round(incentive, 2))
    print("Gross salary: ", round(gross, 2))
    print("Deduction: ", round(deduction, 2))
    print("Net salary: ", round(net, 2))