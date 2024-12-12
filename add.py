# File To Save Events

file_name = "events.txt"

# Dictionary

events = []

# Add Event

def add_event():
    name = input("Enter event NAME: ")
    date = input("Enter event DATE (YYYY-MM-DD): ")
    time = input("Enter event TIME (HH:MM): ")
    location = input("Enter event LOCATION: ")
    description = input("Enter event DESCRIPTION: ")

# Keep in Dictionary

    event = {'name': name, 'date': date, 'time': time, 'location': location, 'description': description}
    events.append(event)

    print(f"{name} has been added.")
    save_history(f"Added event: {name}, Date: {date}, Time: {time}, Location: {location}")