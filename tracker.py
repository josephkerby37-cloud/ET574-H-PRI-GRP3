# Functions for the Reading List Tracker

import data


def add_session():
    """Add a book or article to the reading list."""

    title = input("Enter book title: ").strip()
    

    while title == "":
        print("Book title cannot be empty.")
        title = input("Enter book title: ").strip()

    while True:
        try:
            reading_time = int(input("Enter reading time (minutes): "))

            if reading_time <= 0:
                print("Reading time must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid whole number.")

    while True:
        status = input("Enter status (Finished/In Progress): ").strip().lower()

        if status == "finished":
            status = "Finished"
            break
        elif status == "in progress":
            status = "In Progress"
            break
        else:
            print("Please enter Finished or In Progress.")

    # Add information to the parallel lists
    data.book_titles.append(title)
    data.reading_times.append(reading_time)
    data.reading_statuses.append(status)

    print("Book added!")


def view_reading_list():
    """Display all books and their reading information."""

    print("\n===== YOUR READING LIST =====")

    if len(data.book_titles) == 0:
        print("Your reading list is empty.")
        return

    for i in range(len(data.book_titles)):
        print(f"\nBook #{i + 1}")
        print(f"Title: {data.book_titles[i]}")
        print(f"Reading Time: {data.reading_times[i]} minutes")
        print(f"Status: {data.reading_statuses[i]}")

    print("\nTotal books:", len(data.book_titles))


def summary_report():
    """Display statistics about the reading list."""

    print("\n===== READING SUMMARY =====")

    total_books = len(data.book_titles)

    if total_books == 0:
        print("No books have been added yet.")
        print("Total books: 0")
        print("Total reading time: 0 minutes")
        print("Finished: 0")
        print("In Progress: 0")
        return

    total_time = sum(data.reading_times)
    finished_count = data.reading_statuses.count("Finished")
    in_progress_count = data.reading_statuses.count("In Progress")

    # Find the book with the most reading time
    max_index = data.reading_times.index(max(data.reading_times))
    longest_book = data.book_titles[max_index]
    longest_time = data.reading_times[max_index]

    print(f"Total books: {total_books}")
    print(f"Total reading time: {total_time} minutes")
    print(f"Finished: {finished_count}")
    print(f"In Progress: {in_progress_count}")
    print(f"Book with most reading time: {longest_book} ")
    print(f"({longest_time} minutes)")
