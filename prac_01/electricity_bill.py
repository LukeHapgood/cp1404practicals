print("Electricity bill estimator")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
cost = 0
TARIFF = int(input("Which tariff? 11 or 31: "))
while cost == 0:
    if TARIFF == 11:
        cost = TARIFF_11
    elif TARIFF == 31:
        cost = TARIFF_31
    else:
        print("Invalid Input")
        TARIFF = int(input("Which tariff? 11 or 31:"))
daily_use = float(input("Enter daily use in kWh: "))
period = int(input("Enter number of billing days: "))
bill = cost*daily_use*period
print("Estimated bill: ${:.2f}".format(bill))
