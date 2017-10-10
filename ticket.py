class Ticket:
    """
    Ticket is an abstraction for representing tickets associated with objects of the Event class. An Event can have multiple Ticket objects associated with it.

    Public Variables:
        * price - price of the ticket
    """
    def __init__(self, price):
        """Raise ValueError exception if price is not non-zero"""
        if price > 0:
            self.price = price
        else:
            raise ValueError
        
        return None