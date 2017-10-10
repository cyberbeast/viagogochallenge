from world import World

if __name__ == "__main__":
    newWorld = World() # Initialize a new object of World type.
    newWorld.randomPopulate() # Call randomPopulate() on this object to randomly generate coordinate/event data.

    print("Please Input Coordinates:")
    x, y = input("> ").split(',') # Get user input for location.

    print("Closest Events to (%s,%s):" % (x,y))
    events = newWorld.getClosestEvents((x,y)) # Call getClosestEvents() with location to get the a list of Event class objects

    # Iterate through the list and for each item in the list, print the id, price and distance. 
    for event in events:
        print(
            "Event %s - $%s, Distance %s" % (
                    event.id,
                    event.getCheapestTicketPrice(),
                    event.getDistanceTo((x,y))
                )
            )