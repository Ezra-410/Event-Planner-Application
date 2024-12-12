import add
<<<<<<< HEAD
import view 
import edit
import delete
import search
import export

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

        choice = input("Enter your god damn choice nigga (0-8): ")

        if choice == "1":
            add_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            edit_event_details()
        elif choice == "4":
            delete_event()
        elif choice == "5":
            search_events()
        elif choice == "6":
            export_event_list()
        elif choice == "0":
            print("Exiting Event Planner Application. Goodbye!")
            break
        else:
            print("Invalid input. Goat try again.")

# Run the program

if __name__ == "__main__":
    main()
=======
import delete event
import edit
import export-event-list
import search
import view event

def main():
    while True:
        print("\nEvent Planner Menu:")
        print("1. Add Event")
        print("2. Delete Event")
        print("3. Edit Event")
        print("4. Export Event List")
        print("5. Search Event")
        print("6. View Event Details")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == "1":
            add.add_event()
        elif choice == "2":
            delete_event.delete_event()
            print("\nEvent deleted.")
            input("\nPress Enter to continue...")
        elif choice == "3":
            edit.edit_event()
            print("\nEvent updated.")
            input("\nPress Enter to continue...")
        elif choice == "4":
            export_event_list.export_event_list()
            input("\nEvent list exported to 'events.txt'.")
            print("\nPress Enter to continue...")
        elif choice == "5":
            search.search_event()
           
            print("\nPress Enter to continue...")
        elif choice == "6":
            view_event.view_event()
            input("\nPress Enter to continue...")
        elif choice == "7":
            print("\nExiting the program...")
            break
        
        
>>>>>>> f15cc0062d649ff8868cd2aa3e0e2f33ddaadbbe
