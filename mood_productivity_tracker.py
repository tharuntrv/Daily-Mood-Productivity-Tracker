import json
import datetime
import statistics

DATA_FILE = "mood_productivity_data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def log_entry():
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mood = int(input("Enter your mood (1-10): "))
    productivity = int(input("Enter your productivity (1-10): "))
    note = input("Enter any notes for today: ")
    
    entry = {"date": date, "mood": mood, "productivity": productivity, "note": note}
    data = load_data()
    data.append(entry)
    save_data(data)
    print("Entry logged successfully!\n")

def view_entries():
    data = load_data()
    if not data:
        print("No entries found.\n")
        return
    
    for entry in data:
        print(f"Date: {entry['date']}, Mood: {entry['mood']}, Productivity: {entry['productivity']}, Note: {entry['note']}")
    print()

def analyze_trends():
    data = load_data()
    if not data:
        print("No data available for analysis.\n")
        return
    
    moods = [entry["mood"] for entry in data]
    productivity = [entry["productivity"] for entry in data]
    
    print("--- Trend Analysis ---")
    print(f"Average Mood: {statistics.mean(moods):.2f}")
    print(f"Average Productivity: {statistics.mean(productivity):.2f}")
    print(f"Highest Mood Recorded: {max(moods)}")
    print(f"Highest Productivity Recorded: {max(productivity)}")
    print()

def search_entries():
    search_date = input("Enter date to search (YYYY-MM-DD): ")
    data = load_data()
    results = [entry for entry in data if search_date in entry["date"]]
    
    if results:
        for entry in results:
            print(f"Date: {entry['date']}, Mood: {entry['mood']}, Productivity: {entry['productivity']}, Note: {entry['note']}")
    else:
        print("No entries found for this date.\n")

def delete_entry():
    view_entries()
    delete_date = input("Enter the date of the entry to delete (YYYY-MM-DD HH:MM:SS): ")
    data = load_data()
    
    new_data = [entry for entry in data if entry["date"] != delete_date]
    if len(new_data) == len(data):
        print("No entry found with that date.\n")
    else:
        save_data(new_data)
        print("Entry deleted successfully!\n")

def main():
    while True:
        print("\nDaily Mood & Productivity Tracker")
        print("1. Log Entry")
        print("2. View Entries")
        print("3. Analyze Trends")
        print("4. Search Entries")
        print("5. Delete Entry")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            log_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            analyze_trends()
        elif choice == "4":
            search_entries()
        elif choice == "5":
            delete_entry()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
