






sales_data = [150.75, 200.00, -25.50, 50.25, 300.50, 0.00, 180.00] # sales figures
valid_sales = [] # empty list
for sale in sales_data: # loop through sales
    if sale > 0: # check if positive
        valid_sales.append(sale) # add to valid
total_sales = sum(valid_sales) # sum of valid sales
average_sale = total_sales / len(valid_sales) # calculate average
highest_sale = max(valid_sales) # find max
print("Total sales:", total_sales) # print total
print("Average sale:", average_sale) # print average
print("Highest sale:", highest_sale) # print highest