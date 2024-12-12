# Edit Event Details
from events import events
from export_event_list import save_history

def edit_event_details():
    name = input("Enter event name to update: ")
    for event in events:
        if event['name'].lower() == name.lower():
            print(f"Updating {name}.")
            event['name'] = input(f"Enter new name ({event['name']}): ")
            event['date'] = input(f"Enter new date ({event['date']}): ")
            event['time'] = input(f"Enter new time ({event['time']}): ")
            event['location'] = input(f"Enter new location ({event['location']}): ")
            event['description'] = input(f"Enter new description ({event['description']}): ")
            print(f"{name} has been updated.")
            save_history(f"Updated event: {name}, New details: {event}")
            return
    print(f"{name} not found.")