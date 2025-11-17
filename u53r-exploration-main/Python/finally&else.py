
# Ang 'finally' block ay laging mag-e-execute kahit na may exception o wala.
# Halimbawa ng paggamit ng finally:
try:
    print(1)        # Sinusubukang i-execute ang print(1); magpi-print ng 1 sa console
except:
    print(2)        # Kung may exception na mangyari sa try block, ito ang mag-e-execute at magpi-print ng 2
finally:
    print(3)        # Anuman ang mangyari (may exception man o wala), laging mag-e-execute ito at magpi-print ng 3

# Output:
# 1
# 3



# Ang 'else' block ay mag-e-execute lamang kung walang exception na nangyari sa try block.
# Halimbawa ng paggamit ng else:
try: 
    print(1) 
except ZeroDivisionError: 
    print(2) 
else: 
    print(3) 


try: 
    print(1/0) 
except ZeroDivisionError: 
    print(4) 
else: 
    print(5)





