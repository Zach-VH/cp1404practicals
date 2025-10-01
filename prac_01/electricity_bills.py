
#Constant Variables
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff_chosen = 11
MENU = """1 - Estimate bill estimator
2 - Estimate bill estimator 2.0
Q - Quit"""

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "1":
        print("Estimate bill estimator")
        cents_per_kWh = float(input("Enter cents per kWh: "))
        kWh_per_day = float(input("Enter daily use in kWh: "))
        days = int(input("Enter number of billing days: "))

        print(f"Estimated bill: ${cents_per_kWh * kWh_per_day * days / 100:.2f}")
    elif choice == "2":
        print("Estimate bill estimator 2.0")
        tariff_chosen = input("Which tariff? 11 or 31: ")
        while tariff_chosen != '11' and tariff_chosen != '31':
            tariff_chosen = input("Tariff does not exist. Input 11 or 31: ")
        match tariff_chosen:
            case '11':
                cents_per_kWh = TARIFF_11
            case '31':
                cents_per_kWh = TARIFF_31
        kWh_per_day = float(input("Enter daily use in kWh: "))
        days = int(input("Enter number of billing days: "))

        print(f"Estimated bill: ${cents_per_kWh * kWh_per_day * days:.2f}")
    else:
        print("Invalid Option")

    print(MENU)
    choice = input(">>> ").upper()
print("Close Program")