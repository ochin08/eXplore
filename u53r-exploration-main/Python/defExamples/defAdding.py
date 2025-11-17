



while True:
    fir_input = input("Enter first number (or type 'exit' to quit): ")
    if fir_input.lower() == "exit":
        print("Exiting program... 👋")
        break

    sec_input = input("Enter second number (or type 'exit' to quit): ")
    if sec_input.lower() == "exit":
        print("Exiting program... 👋")
        break

    # Convert to integers after checking for 'exit'
    firNum = int(fir_input)
    secNum = int(sec_input)

    def add(a, b):
        total = a + b
        print("The total is:", total)

    add(firNum, secNum)