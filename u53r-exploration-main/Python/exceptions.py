


#Halimbawa ng Exception kapag nag-divide ka ng number sa zero:
x = 10
y = 0
result = x / y  # Maglalabas ito ng ZeroDivisionError



# Paano gamitin ang try at except
try:
    x = 10
    y = 0
    result = x / y
    print(result)
except ZeroDivisionError:
    print("Hindi puwedeng mag-divide sa zero.") #Output: Hindi puwedeng mag-divide sa zero.



