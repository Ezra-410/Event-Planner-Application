import add
import view_event 
import edit
import delete_event
import search
import export_event_list

def main_menu():
    while True:
        print("\nEvent Planner Menu:")
        print("1. Add Event")
        print("2. View Events")
        print("3. Edit Event Details")
        print("4. Delete Event")
        print("5. Search Events")
        print("6. Export Event List")
        print("0. Exit")

        choice = input("Enter your god damn choice nigga (0-6): ")

        if choice == "1":
            add.add_event()
        elif choice == "2":
            view_event.view_events()
        elif choice == "3":
            edit.edit_event_details()
        elif choice == "4":
            delete_event.delete_event()
        elif choice == "5":
            search.search_events()
        elif choice == "6":
            export_event_list.export_event_list()
        elif choice == "0":
            print("Exiting Event Planner Application. Goodbye!")
            break
        else:
            print("Invalid input. Goat try again.")

# Run the program

if __name__ == "__main__":
    main_menu()
