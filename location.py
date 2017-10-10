class Location:
    """
    Location is an abstraction for representing a location in the World. An instance of the World can have multiple Event(s). Each event has a single Location.

    Public Variables:
        * x - x coordinate of the location
        
        * y - y coordinate of the location
    """
    def __init__(self, location):
        """Catch ValueError exception if incorrect number of values are passed as part of the location tuple."""
        if type(location) == 'tuple' and len(location) == 2:
            self.x, self.y = location
        else:
            raise ValueError
        