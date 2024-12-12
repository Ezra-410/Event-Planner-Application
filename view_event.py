# View Events
from add import events
from events import events
def view_events():
    if not events:
        print("No events to display.")
    else:
        print("\nUpcoming Events:")
        for event in events:
            print(f"{event['name']} on {event['date']} at {event['time']} - Location: {event['location']} - {event['description']}")
