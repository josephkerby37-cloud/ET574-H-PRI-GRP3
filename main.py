# Main menu for the Reading List Tracker

import tracker


def main():
    print("=" * 35)
    print("Welcome to Reading List Tracker!")
    print("Track your books and reading time.")
    print("=" * 35)
    while True:
        print("\n1. Add Book")
        print("2. View Reading List")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            tracker.add_session()

        elif choice == "2":
            tracker.view_reading_list()

        elif choice == "3":
            tracker.summary_report()

        elif choice == "4":
            print("Thank you for using Reading List Tracker!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
