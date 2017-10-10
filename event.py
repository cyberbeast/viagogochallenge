from ticket import Ticket
from location import Location

from random import randrange, uniform

class Event:
    """
    The Event class is an abstraction for defining an event with respect to the following constraints:
        * Each event has a unique numeric identifier.
        * Each event has 0 or more tickets.
    
    Public Variables:
        * id - unique numeric identifier

        * tickets - list of ticket objects available for this event.

        * location - Object of 'Location' class that represents the location of this event in the world.

        * distancesToLocation - Dictionary/HashMap structure containing the distance of this event to other locations in the world.
    """
    MAX_NUMBER_OF_TICKETS = 100
    MAX_TICKET_PRICE = 500

    def __init__(self, identifier, location_xy):
        """Initialize function for Event class"""
        self.id = identifier
        self.tickets = []

        try:
            self.location = Location(location_xy)
        except ValueError:
            print("Either incorrect number of parameters provided to unpack for location or incorrect type used.")
            exit(0)

        self.distancesToLocation = {}

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return self.id
    
    def setRandomTicketPrices(self):
        """Public method that sets random ticket prices for events. Since ticket prices are non-zero values, the random price generated is always greater than 0."""
        numberOfTickets = randrange(self.MAX_NUMBER_OF_TICKETS)
        if numberOfTickets > 0:
            for _ in range(numberOfTickets):
                randomPrice = round(uniform(1, self.MAX_TICKET_PRICE), 2)
                try:
                    self.tickets.append(Ticket(randomPrice))
                except ValueError:
                    print('Ticket price has to be a non-zero value. Exiting...')
                    exit(0)
                    
    
    def getCheapestTicketPrice(self):
        """
        Public method that gets the cheapest ticket price among the available tickets for the event.

        Output:
            * cheapest ticket price
        """
        temp = []
        if len(self.tickets) is not 0:
            for ticket in self.tickets:
                temp.append(ticket.price)
        else:
            return 0

        return min(temp)

    def __manhattanDistanceTo(self, location):
        """
        Private method for computing the distance between the current event's location and another location using the Manhattan Distance metric.

        Input:
            * location - tuple (x,y)

        Output:
            * Manhattan distance
        """
        x1, y1 = location
        return abs(int(x1) - self.location.x) + abs(int(y1) - self.location.y)
    
    def getDistanceTo(self, location):
        """
        Public method for retrieving the distance from the currrent event's location to a location parameter provided to the method. If this distance has been previously computed (and hence present in the 'distancesToLocation' dictionary) it is not re-computed and is returned directly. If this distance has not been previously computed, it adds this to the 'distancesToLocation' dictionary and returns this newly computed value.

        Input:
            * location - tuple (x,y)

        Output:
            * distance to the specified location
        """
        if location not in self.distancesToLocation.keys():
            self.distancesToLocation[location] = self.__manhattanDistanceTo(location)

        return self.distancesToLocation[location]
