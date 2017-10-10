from random import randrange, seed
SEED_VALUE = 3
seed(SEED_VALUE)
from event import Event

class World:
    """
    World is an abstraction for defining the coordinate grid on which the program operates on.

    Public Variables:
        * events - list of all Event objects in this world.

        * maxNumberOfEvents - used by the randomPopulate() function to define a seed for pseudo-randomly choosing the number of events to populate the world with.

        * activeCoordinates - list of coordinate tuples (x, y) representing the locations that are have already been assigned events when randomly populating the world.

    Private Variables:    
        * __eventIDGenerator - handler for a generator function __identifier() used to assign a unique numeric identifier to an event.

        * __randomLocationGenerator - handler for a generator function __identifier() used to assign a new/unused location to an event when randomly populating the world.
    """
    def __init__(self, x_min=-10, x_max=10, y_min=-10, y_max=10):
        """Initialize function for World class"""
        self.events = []
        self.x_min, self.x_max, self.y_min, self.y_max = x_min, x_max, y_min, y_max
        size_x = abs(x_min) + abs(x_max) + 1
        size_y = abs(y_min) + abs(y_max) + 1
        self.maxNumberOfEvents = size_x * size_y
        self.__eventIDGenerator = self.__identifier()
        self.__randomLocationGenerator = self.__coordinates()
        self.activeCoordinates = []

    def __identifier(self):
        """Generator function that yields a unique numeric identifier."""
        n = 0
        while True:
            n += 1
            yield n
    
    def __coordinates(self):
        """Generator function that yields an unused tuple of coordinates."""
        while True:
            setReturned = False
            while setReturned == False:
                rand_x = randrange(self.x_min - 1, self.x_max + 1)
                rand_y = randrange(self.y_min - 1, self.y_max + 1)
                if (rand_x, rand_y) not in self.activeCoordinates:
                    self.activeCoordinates.append((rand_x, rand_y))
                    setReturned = True
                    yield (rand_x, rand_y)

    def randomPopulate(self):
        """Public method that populates the defined world with random events and locations"""
        numberOfEvents = randrange(self.maxNumberOfEvents)
        for _ in range(numberOfEvents):
            _id = next(self.__eventIDGenerator)
            _location = next(self.__randomLocationGenerator)
            _event = Event(_id, _location)
            _event.setRandomTicketPrices()
            self.events.append(_event)
        

    def getClosestEvents(self, location, degree=5):
        """
        Public method that returns 'degree' number of events that are closest to 'location'. The default degree is 5.
        
        Input:
            * location - tuple (x,y)
            * degree - number of events
        
        Output:
            * [event.Event objects]
        """
        closestEvents = sorted(self.events, key=lambda x: x.getDistanceTo(location))
        return closestEvents[:degree] 