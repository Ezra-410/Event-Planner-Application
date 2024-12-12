import add
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
        
        
