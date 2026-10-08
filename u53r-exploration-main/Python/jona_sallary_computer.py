



# Sahod Computer
# Input if how many days you work
# Input if How much your perday
# Minus the benifits


while True:

    for i in range(1):
            print("\n")

    number_of_days = float(input("Number of days: "))
    perday = float(input("Input perday: "))

    total = number_of_days * perday
    benefits_deduction_amount = 500
    benefits_deduction = total - benefits_deduction_amount
    sallary = benefits_deduction

    print("=" * 50)
    print(f"Gross Pay                   : {total}")
    print(f"Benefits Deduction Amount   : {benefits_deduction_amount}")
    print("-" * 50)
    print(f"\n\033[1;36mTotal                       : {sallary}\033[0m")
    print("=" * 50)

