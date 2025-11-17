





while True:

    agecustomer = input("Enter your age or type exit to quit: ")

    if agecustomer == 'exit':
        print("Exiting the program, thank you!")
        break

    try:
        agecustomer = int(agecustomer)

        if agecustomer >=75:
            print("Customer is may discount dahil senior citizen ito.")
        else:
            print("Customer is walang discount")
    except ValueError:
        print("Invalid input. Please enter a valid age or type 'exit' to quit.")
print("Proceed to checkout")
print("Thank you for your purchase!")