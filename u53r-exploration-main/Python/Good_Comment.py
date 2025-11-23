

# --- Daily Sales Report Script ---
# This script processes raw sales data to generate key daily statistics.
# It handles data cleaning, aggregation, and reporting.

# Raw sales data for the day. Includes potential invalid entries.
sales_data = [150.75, 200.00, -25.50, 50.25, 300.50, 0.00, 180.00]

# Filter out invalid sales entries.
# Sales must be strictly positive to be considered valid for reporting.
# This prevents skewing averages and totals with erroneous data.
valid_sales = []
for sale in sales_data:
    if sale > 0: # Only positive sales are accepted
        valid_sales.append(sale)

# Check if there are any valid sales to prevent division by zero errors
if not valid_sales:
    print("No valid sales recorded for the day.")
else:
    # Calculate key sales metrics
    total_sales = sum(valid_sales)
    average_sale = total_sales / len(valid_sales)
    highest_sale = max(valid_sales)

    # --- Report Generation ---
    # Display the calculated statistics in a user-friendly format.
    print(f"--- Sales Summary for Today ---")
    print(f"Total Sales: ${total_sales:.2f}") # Format to two decimal places
    print(f"Number of Valid Transactions: {len(valid_sales)}")
    print(f"Average Sale Amount: ${average_sale:.2f}")
    print(f"Highest Single Sale: ${highest_sale:.2f}")

    # TODO: Add functionality to save this report to a file
    # for long-term record keeping.