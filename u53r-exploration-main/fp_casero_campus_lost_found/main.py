



"""
Campus Lost and Found System

A menu-driven Python application for managing
lost and found items within the campus.
"""

from pathlib import Path


# ==========================================
# 1. PROJECT CONFIGURATION
# ==========================================

PROJECT_DIR = Path(__file__).resolve().parent

DATA_DIR = PROJECT_DIR / "data"
DOCS_DIR = PROJECT_DIR / "docs"

RECORDS_FILE = DATA_DIR / "records.csv"
ACTIVITY_LOG_FILE = DATA_DIR / "activity_log.txt"


# ==========================================
# 2. SYSTEM CONSTANTS
# ==========================================

APP_TITLE = "CAMPUS LOST AND FOUND SYSTEM"

ALLOWED_STATUSES = {
    "Lost",
    "Found",
    "Claimed"
}

FIELDNAMES = (
    "item_id",
    "item_name",
    "category",
    "location",
    "date_reported",
    "status",
    "estimated_value",
    "contact_email"
)


# ==========================================
# 3. DATA STRUCTURE
# ==========================================

records: list[dict] = []


# ==========================================
# 4. MAIN FUNCTION
# ==========================================

def main():
    """Start the Campus Lost and Found System."""

    print("=" * 50)
    print(APP_TITLE)
    print("=" * 50)

    print("Project directory:", PROJECT_DIR)
    print("Records file:", RECORDS_FILE)

    print("\nSystem foundation initialized.")


# ==========================================
# 5. PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":
    main()
