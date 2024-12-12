# Search Events

def search_events():
    search_term = input("Enter event name or date to search: ").lower()
    found_events = [event for event in events if search_term in event['name'].lower() or search_term in event['date']]
    
    if found_events:
        print("\nSearch Results:")
        for event in found_events:
            print (f"Event: {event['name']} on {event['date']} at {event['time']}")
            print(f"Location: {event['location']}")
            print(f"Description: {event['description']}")
    else:
        print("Fuck You!.")