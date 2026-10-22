import os
import time
import sys

# ------------------------------------------------------------
# Local Heritage Community (LHC) Artefact Management System
# ------------------------------------------------------------

# Data structure: list of dictionaries
artefacts = []


def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    """Displays the main menu options."""
    print("\n--- LHC Artefact Management System ---")
    print("1. View All Artefacts")
    print("2. Add New Artefact")
    print("3. Update Artefact Condition")
    print("4. Search Artefact by Name")
    print("5. Exit")
    print("--------------------------------------")


def view_artefacts():
    """Displays all artefacts."""
    clear_screen()
    print("\n--- Artefact List ---")

    if not artefacts:
        print("No artefacts in the system.")
    else:
        for item in artefacts:
            print(f"Name: {item['name']}")
            print(f"Category: {item['category']}")
            print(f"Location: {item['location']}")
            print(f"Condition: {item['condition']}")
            print("---------------------------")

    time.sleep(2)


def add_artefact():
    """Adds a new artefact to the system."""
    clear_screen()
    print("\n--- Add New Artefact ---")

    name = input("Enter artefact name: ").strip()
    category = input("Enter artefact category: ").strip()
    location = input("Enter artefact location: ").strip()

    condition = input("Enter condition (Good/Damaged/Under Repair): ").strip().lower()
    valid_conditions = ["good", "damaged", "under repair"]

    if condition not in valid_conditions:
        print("Invalid condition. Setting condition to 'Good'.")
        condition = "good"

    artefact_record = {
        "name": name,
        "category": category,
        "location": location,
        "condition": condition
    }

    artefacts.append(artefact_record)
    print("Artefact added successfully!")
    time.sleep(2)


def update_condition():
    """Updates the condition of an existing artefact."""
    clear_screen()
    print("\n--- Update Artefact Condition ---")

    search_name = input("Enter artefact name to update: ").strip()
    found = False

    for item in artefacts:
        if item["name"].lower() == search_name.lower():
            found = True
            print(f"Current condition: {item['condition']}")
            new_condition = input("Enter new condition (Good/Damaged/Under Repair): ").strip().lower()

            valid_conditions = ["good", "damaged", "under repair"]
            if new_condition not in valid_conditions:
                print("Invalid condition. Update cancelled.")
            else:
                item["condition"] = new_condition
                print("Condition updated successfully!")
            break

    if not found:
        print("Artefact not found.")

    time.sleep(2)


def search_artefact():
    """Searches for an artefact by name."""
    clear_screen()
    print("\n--- Search Artefact ---")

    search_name = input("Enter artefact name: ").strip()
    found = False

    for item in artefacts:
        if item["name"].lower() == search_name.lower():
            found = True
            print("Artefact found:")
            print(f"Name: {item['name']}")
            print(f"Category: {item['category']}")
            print(f"Location: {item['location']}")
            print(f"Condition: {item['condition']}")
            break

    if not found:
        print("No artefact found.")

    time.sleep(2)


def exit_program():
    """Exits the program gracefully."""
    print("Exiting the system. Have a great day!")
    time.sleep(2)
    sys.exit()


def main():
    """Main function to run the LHC system."""
    while True:
        clear_screen()
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            view_artefacts()
        elif choice == "2":
            add_artefact()
        elif choice == "3":
            update_condition()
        elif choice == "4":
            search_artefact()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            time.sleep(2)


# Run the system
if __name__ == "__main__":
    main()



