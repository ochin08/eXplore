"""
Campus Lost and Found System
Fundamentals of Programming Project

Python 3.12+
Standard Library Only
"""

import csv
import math
import os
import re
from datetime import datetime
from pathlib import Path


# ==================================================
# 1. CONSTANTS
# ==================================================

APP_TITLE = "CAMPUS LOST AND FOUND SYSTEM"

CSV_FIELDS = (
    "item_id",
    "item_name",
    "category",
    "location",
    "date_reported",
    "status",
    "estimated_value",
    "contact_email",
)

VALID_STATUSES = ("Lost", "Found", "Claimed")

MENU_OPTIONS = {
    "1": "Add New Item",
    "2": "View All Items",
    "3": "Search Items",
    "4": "Update Item",
    "5": "Delete Item",
    "6": "Generate Summary Report",
    "7": "Save and Exit",
}

ITEM_ID_PATTERN = r"ITM-[0-9]{4}"

EMAIL_PATTERN = (
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
DATA_FILE = DATA_DIR / "records.csv"
LOG_FILE = DATA_DIR / "activity_log.txt"


# ==================================================
# 2. DATA STORAGE
# ==================================================

records = []
csv_file_damaged = False


# ==================================================
# 3. ACTIVITY LOGGING
# ==================================================

def log_activity(action, details=""):
    """Append a timestamped activity to the log file."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(
                f"[{timestamp}] {action}: {details}\n"
            )

    except OSError as error:
        print(f"Warning: Activity log could not be written: {error}")


# ==================================================
# 4. VALIDATION FUNCTIONS
# ==================================================

def validate_item_id(item_id):
    """Check the required item ID format."""

    return re.fullmatch(ITEM_ID_PATTERN, item_id) is not None


def validate_email(email):
    """Check whether an optional email has a valid-looking format."""

    return (
        not email
        or re.fullmatch(EMAIL_PATTERN, email) is not None
    )


def validate_date(date_text):
    """Check date format and actual calendar validity."""

    try:
        parsed_date = datetime.strptime(date_text, "%Y-%m-%d")
        return parsed_date.strftime("%Y-%m-%d") == date_text

    except ValueError:
        return False


def validate_status(status):
    """Check whether the status is one of the allowed choices."""

    return status.title() in VALID_STATUSES


def validate_value(value):
    """Validate an optional nonnegative, finite numeric value."""

    if value == "":
        return True, None

    try:
        number = float(value)

        # float() also accepts "nan" and "inf", so reject those.
        if not math.isfinite(number) or number < 0:
            return False, None

        return True, number

    except ValueError:
        return False, None


def make_record(**fields):
    """Create a record dictionary using named fields."""

    return {field: fields.get(field) for field in CSV_FIELDS}


# ==================================================
# 5. CSV FILE HANDLING
# ==================================================

def load_records():
    """Load and validate existing records from the CSV file."""

    global csv_file_damaged

    loaded_records = []
    csv_file_damaged = False

    try:
        # utf-8-sig also handles files saved by Excel (with BOM).
        with open(DATA_FILE, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames != list(CSV_FIELDS):
                raise ValueError("Invalid or missing CSV header.")

            seen_ids = set()

            for row in reader:

                if None in row or any(
                    row.get(field) is None for field in CSV_FIELDS
                ):
                    raise ValueError("Incomplete CSV record.")

                item_id = row["item_id"].strip()

                if not validate_item_id(item_id):
                    raise ValueError(f"Invalid item ID: {item_id}")

                if item_id in seen_ids:
                    raise ValueError(f"Duplicate item ID: {item_id}")

                if not all(
                    row[field].strip()
                    for field in (
                        "item_name",
                        "category",
                        "location",
                        "date_reported",
                        "status",
                    )
                ):
                    raise ValueError("A required field is empty.")

                if not validate_date(row["date_reported"].strip()):
                    raise ValueError("Invalid date in CSV.")

                if not validate_status(row["status"].strip()):
                    raise ValueError("Invalid status in CSV.")

                if not validate_email(row["contact_email"].strip()):
                    raise ValueError("Invalid email in CSV.")

                valid_value, numeric_value = validate_value(
                    row["estimated_value"].strip()
                )

                if not valid_value:
                    raise ValueError("Invalid estimated value in CSV.")

                row["item_id"] = item_id
                row["status"] = row["status"].strip().title()
                row["estimated_value"] = numeric_value
                row["contact_email"] = row["contact_email"].strip()

                for field in (
                    "item_name",
                    "category",
                    "location",
                    "date_reported",
                ):
                    row[field] = row[field].strip()

                seen_ids.add(item_id)
                loaded_records.append(row)

        print(f"Successfully loaded {len(loaded_records)} records.")

    except FileNotFoundError:
        print("CSV file not found. Starting with empty records.")

    except (OSError, csv.Error, ValueError, UnicodeError) as error:
        print(f"Unable to load CSV: {error}")
        print("Original CSV will be preserved.")
        csv_file_damaged = True

    return loaded_records


def save_records(records_to_save=None):
    """Save records safely using a temporary CSV file."""

    if csv_file_damaged:
        print("Save cancelled: CSV recovery is required first.")
        return False

    if records_to_save is None:
        records_to_save = records

    temporary_file = DATA_FILE.with_suffix(".tmp")

    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        with open(
            temporary_file, "w", newline="", encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=CSV_FIELDS
            )

            writer.writeheader()

            for record in records_to_save:

                row = {
                    field: (
                        ""
                        if record.get(field) is None
                        else record.get(field)
                    )
                    for field in CSV_FIELDS
                }

                writer.writerow(row)

        os.replace(temporary_file, DATA_FILE)

        return True

    except (OSError, csv.Error) as error:
        print(f"Unable to save records: {error}")
        return False

    finally:
        if temporary_file.exists():
            try:
                temporary_file.unlink()
            except OSError:
                pass


# ==================================================
# 6. DISPLAY FUNCTIONS
# ==================================================

def display_menu():
    """Display the main menu."""

    print("\n" + "=" * 65)
    print(APP_TITLE.center(65))
    print("=" * 65)

    for choice, description in MENU_OPTIONS.items():
        print(f"{choice}. {description}")

    print("=" * 65)


def display_table(headers, rows, *widths):
    """Display records using aligned columns and row numbers."""

    if not rows:
        print("No records available.")
        return

    if not widths:
        widths = tuple(15 for _ in headers)

    print()

    print(f"{'No.':<5}", end="")

    for header, width in zip(headers, widths):
        print(f"{header:<{width}}", end="")

    print()
    print("-" * (5 + sum(widths)))

    for number, row in enumerate(rows, start=1):

        print(f"{number:<5}", end="")

        for value, width in zip(row, widths):
            display_value = str(value)

            # Shorten long values so columns stay aligned.
            if len(display_value) >= width:
                display_value = display_value[: width - 4] + "..."

            print(f"{display_value:<{width}}", end="")

        print()

    print("-" * (5 + sum(widths)))


def format_records(record_list):
    """Convert record dictionaries into table rows."""

    return [
        (
            record["item_id"],
            record["item_name"],
            record["category"],
            record["location"],
            record["date_reported"],
            record["status"],
        )
        for record in record_list
    ]


def show_records(record_list):
    """Display a collection of item records."""

    headers = (
        "ITEM ID",
        "ITEM NAME",
        "CATEGORY",
        "LOCATION",
        "DATE",
        "STATUS",
    )

    rows = format_records(record_list)

    display_table(
        headers,
        rows,
        13, 22, 18, 22, 13, 12
    )


# ==================================================
# 7. ADD NEW ITEM
# ==================================================

def add_item():
    """Collect, validate, and save a new item record."""

    if csv_file_damaged:
        print("Adding records is disabled until CSV recovery.")
        return

    print("\nADD NEW ITEM")

    item_id = input("Item ID (ITM-0001): ").strip().upper()

    if not validate_item_id(item_id):
        print("Invalid item ID format.")
        return

    if any(record["item_id"] == item_id for record in records):
        print("Duplicate item ID.")
        return

    item_name = input("Item Name: ").strip()
    category = input("Category: ").strip()
    location = input("Location: ").strip()
    date_reported = input("Date Reported (YYYY-MM-DD): ").strip()
    status = input("Status (Lost/Found/Claimed): ").strip().title()
    estimated_text = input("Estimated Value (optional): ").strip()
    contact_email = input("Contact Email (optional): ").strip()

    required_values = (
        item_name,
        category,
        location,
        date_reported,
        status,
    )

    if not all(required_values):
        print("Required fields cannot be empty.")
        return

    if not validate_date(date_reported):
        print("Invalid date. Use YYYY-MM-DD.")
        return

    if not validate_status(status):
        print("Status must be Lost, Found, or Claimed.")
        return

    valid_value, estimated_value = validate_value(estimated_text)

    if not valid_value:
        print("Estimated value must be a nonnegative number.")
        return

    if not validate_email(contact_email):
        print("Invalid email format.")
        return

    new_record = make_record(
        item_id=item_id,
        item_name=item_name,
        category=category,
        location=location,
        date_reported=date_reported,
        status=status,
        estimated_value=estimated_value,
        contact_email=contact_email,
    )

    records.append(new_record)

    if save_records():
        log_activity("ADD", item_id)
        print("Item successfully added.")

    else:
        records.pop()
        print("Item was not added because saving failed.")


# ==================================================
# 8. VIEW ALL ITEMS
# ==================================================

def view_all_items():
    """Display all existing item records."""

    print("\nALL LOST AND FOUND ITEMS")

    if not records:
        print("No records available.")
        return

    show_records(records)

    print(f"Total Records: {len(records)}")


# ==================================================
# 9. SEARCH ITEMS
# ==================================================

def search_items(records_list=None):
    """Search item records using a case-insensitive keyword."""

    if records_list is None:
        records_list = records

    keyword = input("Enter search keyword: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    results = [
        record
        for record in records_list
        if any(
            keyword in record[field].lower()
            for field in (
                "item_name",
                "category",
                "location",
                "status",
            )
        )
    ]

    if results:
        print("\nSEARCH RESULTS")
        show_records(results)
        print(f"Matching Records: {len(results)}")

    else:
        print("No matching records found.")


# ==================================================
# 10. UPDATE ITEM
# ==================================================

def update_item():
    """Update an existing record after validating new information."""

    if csv_file_damaged:
        print("Updating records is disabled until CSV recovery.")
        return

    item_id = input("Enter Item ID to update: ").strip().upper()

    record = next(
        (item for item in records if item["item_id"] == item_id),
        None
    )

    if record is None:
        print("Item not found.")
        return

    fields = {
        "1": "item_name",
        "2": "category",
        "3": "location",
        "4": "date_reported",
        "5": "status",
        "6": "estimated_value",
        "7": "contact_email",
    }

    print("\nSELECT FIELD TO UPDATE")

    for choice, field in fields.items():
        print(f"{choice}. {field.replace('_', ' ').title()}")

    choice = input("Enter choice: ").strip()

    if choice not in fields:
        print("Invalid update choice.")
        return

    field = fields[choice]
    new_value = input("Enter new value: ").strip()

    if field in (
        "item_name",
        "category",
        "location",
        "date_reported",
        "status",
    ) and not new_value:
        print("This field cannot be empty.")
        return

    if field == "date_reported" and not validate_date(new_value):
        print("Invalid date. Use YYYY-MM-DD.")
        return

    if field == "status":
        new_value = new_value.title()

        if not validate_status(new_value):
            print("Invalid status.")
            return

    if field == "estimated_value":
        valid, new_value = validate_value(new_value)

        if not valid:
            print("Invalid estimated value.")
            return

    if field == "contact_email" and not validate_email(new_value):
        print("Invalid email.")
        return

    old_value = record[field]
    record[field] = new_value

    if save_records():
        log_activity("UPDATE", f"{item_id}: {field}")
        print("Record successfully updated.")

    else:
        record[field] = old_value
        print("Update cancelled because saving failed.")


# ==================================================
# 11. DELETE ITEM
# ==================================================

def delete_item():
    """Delete an item only after user confirmation."""

    if csv_file_damaged:
        print("Deleting records is disabled until CSV recovery.")
        return

    item_id = input("Enter Item ID to delete: ").strip().upper()

    record = next(
        (item for item in records if item["item_id"] == item_id),
        None
    )

    if record is None:
        print("Item not found.")
        return

    print(f"Item: {record['item_name']}")
    confirmation = input("Confirm deletion? (Y/N): ").strip().upper()

    if confirmation != "Y":
        print("Deletion cancelled.")
        return

    position = records.index(record)
    records.remove(record)

    if save_records():
        log_activity("DELETE", item_id)
        print("Record successfully deleted.")

    else:
        # Restore the record in its original position.
        records.insert(position, record)
        print("Deletion cancelled because saving failed.")


# ==================================================
# 12. SUMMARY REPORT
# ==================================================

def generate_report():
    """Generate summary statistics for all item records."""

    total_items = len(records)

    lost_items = sum(
        record["status"] == "Lost" for record in records
    )

    found_items = sum(
        record["status"] == "Found" for record in records
    )

    claimed_items = sum(
        record["status"] == "Claimed" for record in records
    )

    print("\nCAMPUS LOST AND FOUND SUMMARY REPORT")
    print("=" * 40)
    print(f"Total Items:   {total_items}")
    print(f"Lost Items:    {lost_items}")
    print(f"Found Items:   {found_items}")
    print(f"Claimed Items: {claimed_items}")
    print("=" * 40)


# ==================================================
# 13. MAIN PROGRAM
# ==================================================

def main():
    """Run the application and control its menu."""

    global records

    print(f"\nWelcome to {APP_TITLE}")

    records = load_records()

    log_activity("START", "Application started")

    running = True

    while running:

        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_item()

        elif choice == "2":
            view_all_items()

        elif choice == "3":
            search_items()

        elif choice == "4":
            update_item()

        elif choice == "5":
            delete_item()

        elif choice == "6":
            generate_report()

        elif choice == "7":

            if csv_file_damaged:
                # Nothing can be saved, so allow exit without
                # touching the original (damaged) CSV file.
                print("CSV was damaged; exiting without saving.")
                print("The original file was left untouched.")
                log_activity("EXIT", "Closed without saving (damaged CSV)")
                running = False

            elif save_records():
                log_activity("EXIT", "Application closed")
                print("Records saved successfully.")
                print("Thank you for using the system!")
                running = False

        else:
            print("Invalid choice. Please select 1 to 7.")

    print("Application closed.")


# ==================================================
# PROGRAM ENTRY POINT
# ==================================================

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Every add/update/delete is already saved immediately.
        print("\nProgram interrupted. Saved records are kept.")