# Delete Event
from events import events
from export_event_list import save_history
def delete_event():
    name = input("Enter event name to remove: ")

    for event in events:
        if event['name'].lower() == name.lower():
            events.remove(event)
            print(f"{name} Removed.")
            save_history(f"Removed event: {name}")
            return
    print(f"{name} not found. Check your input.")
