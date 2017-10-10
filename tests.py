import unittest

from world import World
from event import Event
from ticket import Ticket
from location import Location

class TestSuite(unittest.TestCase):
    """TestSuite defines the test methods for unit testing of the python implementation."""
    def testTicket_1(self):
        """
        Input:              zero integer and floating point value.
        Expected Output:    raise ValueError
        """
        with self.assertRaises(ValueError):
            Ticket(0)
            Ticket(0.00)
    
    def testTicket_2(self):
        """
        Input:              non-zero integer value.
        Expected Output:    return None. (Success)
        """
        self.assertTrue(Ticket(10))
    
    def testTicket_3(self):
        """
        Input:              non-zero floating point value.
        Expected Output:    return None. (Success)
        """
        self.assertTrue(Ticket(10.00))
    
    def testLocation_1(self):
        """
        Input:              >2 parameters.
        Expected Output:    raise TypeError
        """
        with self.assertRaises(TypeError):
            Location(1,1,1)

    def testLocation_2(self):
        """
        Input:              Single integer valued tuple to Location()
        Expected Output:    raise TypeError
        """
        with self.assertRaises(TypeError):
            Location((1))
    
    def testLocation_3(self):
        """
        Input:              >3 integer valued tuples to Location()
        Expected Output:    raise ValueError
        """
        with self.assertRaises(ValueError):
            Location((1,2,3))
    
    def testManhattanDistance_1(self):
        """
        Expected Behavior:  Correctly calculate Manhattan Distance from test_event object to valid points.
        """
        test_event = Event('TestEvent1', (1,1))
        self.assertEqual(test_event.getDistanceTo((3,3)), 4)
        self.assertEqual(test_event.getDistanceTo((-2,5)), 7)        

if __name__ == '__main__':
    unittest.main()  