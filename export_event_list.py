def export_event_list():
    if not events:
        print("\nNo events to export.")
        return
    
    with open("events.txt", "w") as file:
        for event in events:
            file.write(f"{event['name']} on {event['date']} at {event['time']} - Location: {event['location']} - {event['description']}\n")
            print("Event Deposited to 'events.txt'.")