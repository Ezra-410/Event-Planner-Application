def export_event_list():
    if not events:
        print("\nNo events to export.")
        return
    
    with open("events.txt", "w") as file:
        for event in events:
            file.write(f"{event['name']} on {event['date']} at {event['time']} - Location: {event['location']} - {event['description']}\n")
            print("Event Deposited to 'events.txt'.")
            
# Save In History

def save_history(action):
    with open(file_name, "a") as file_obj:
        file_obj.write(action + "\n")

# View Event History

def view_event_history():
    try:
        with open(file_name, "r") as file_obj:
            contents = file_obj.read()
            if contents:
                print("\nEvent History:")
                print(contents)
            else:
                print("Found nothing Fool!.")
    except:
        print("Nothing Fuck!.")

# Main menu loop

def main():

    while True:
        print("\nEvent Planner Menu:")
        print("1. Add Event")
        print("2. View Events")
        print("3. Edit Event Details")
        print("4. Delete Event")
        print("5. Search Events")
        print("6. Export Event List")
        print("7. Save History")
        print("8. View Event History")
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
        elif choice == "6":
            save_history()
        elif choice == "7":
            view_event_history()
        elif choice == "0":
            print("Exiting Event Planner Application. Goodbye!")
            break
        else:
            print("Invalid input. Goat try again.")

# Run the program

if __name__ == "__main__":
    main()