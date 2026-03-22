"""
📊 CSV DATA ANALYZER (PRO)
--------------------------
A manual data processing tool built with Python's built-in CSV module.
- Level 1: File loading and raw data display.
- Level 2: Math analysis (Average, Max, Min).
- Level 3: Advanced filtering and search logic.
- Level 4: Grouped data analysis and CSV updates.
"""

import csv
import os

# --- Configuration ---
DATA_FILE = "student_data.csv"
FIELDNAMES = ['Name', 'Subject', 'Score']

def create_sample_csv():
    """Create a sample CSV file if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        sample_data = [
            {'Name': 'Alice', 'Subject': 'Math', 'Score': 85},
            {'Name': 'Bob', 'Subject': 'Science', 'Score': 72},
            {'Name': 'Charlie', 'Subject': 'Math', 'Score': 92},
            {'Name': 'Alice', 'Subject': 'Science', 'Score': 78},
            {'Name': 'Bob', 'Subject': 'Math', 'Score': 65},
            {'Name': 'Charlie', 'Subject': 'Science', 'Score': 88}
        ]
        with open(DATA_FILE, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(sample_data)
        print(f"📝 Created sample file: {DATA_FILE}")

# --- Level 1 & 3: Loading & Display ---
def load_data():
    """Load CSV rows into a list of dictionaries."""
    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert Score to integer for math operations
                row['Score'] = int(row['Score'])
                data.append(row)
    return data

def display_data(data, title="All Records"):
    """Format and display rows."""
    if not data:
        print("\nNo data found.")
        return
    print(f"\n--- {title} ---")
    print(f"{'Name':<12} | {'Subject':<10} | {'Score':<5}")
    print("-" * 35)
    for row in data:
        print(f"{row['Name']:<12} | {row['Subject']:<10} | {row['Score']:<5}")

# --- Level 2: Analysis ---
def calculate_stats(data):
    """Compute basic statistics (Avg, Max, Min)."""
    if not data: return
    scores = [row['Score'] for row in data]
    avg = sum(scores) / len(scores)
    
    print("\n📈 Statistical Analysis:")
    print(f"- Average Score: {avg:.2f}")
    print(f"- Highest Score: {max(scores)}")
    print(f"- Lowest Score:  {min(scores)}")

# --- Level 3: Filtering ---
def filter_and_search(data):
    """Filter records by score threshold or name."""
    print("\n1. Filter by minimum score")
    print("2. Search by student name")
    choice = input("Select filter type: ")
    
    if choice == '1':
        threshold = int(input("Show scores greater than: "))
        filtered = [r for r in data if r['Score'] > threshold]
        display_data(filtered, f"Students with Score > {threshold}")
    elif choice == '2':
        name = input("Enter student name: ").strip().lower()
        results = [r for r in data if name in r['Name'].lower()]
        display_data(results, f"Search results for '{name}'")

# --- Level 4: Advanced Grouping & Editing ---
def group_analysis(data):
    """Calculate totals and averages per subject."""
    groups = {} # Subject -> [Scores]
    for row in data:
        subj = row['Subject']
        if subj not in groups: groups[subj] = []
        groups[subj].append(row['Score'])
    
    print("\n📚 Subject-wise Performance:")
    for subj, scores in groups.items():
        avg = sum(scores) / len(scores)
        print(f"- {subj}: Avg {avg:.1f} (Count: {len(scores)})")

def add_and_save(data):
    """Add a new row and save to disk."""
    name = input("Name: ").title()
    subject = input("Subject: ").title()
    try:
        score = int(input("Score: "))
        new_row = {'Name': name, 'Subject': subject, 'Score': score}
        data.append(new_row)
        
        with open(DATA_FILE, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(data)
        print("✅ Data saved to CSV!")
    except ValueError:
        print("❌ Error: Score must be a number.")

# --- Main Menu ---
def main():
    create_sample_csv()
    while True:
        data = load_data()
        print("\n" + "═"*30)
        print("📂 CSV DATA ANALYZER")
        print("═"*30)
        print("1. View Raw Data")
        print("2. Run General Stats")
        print("3. Filter or Search")
        print("4. Subject-wise Grouping")
        print("5. Add New Row")
        print("6. Exit")
        
        choice = input("\nSelect (1-6): ")
        if choice == '1': display_data(data)
        elif choice == '2': calculate_stats(data)
        elif choice == '3': filter_and_search(data)
        elif choice == '4': group_analysis(data)
        elif choice == '5': add_and_save(data)
        elif choice == '6': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
