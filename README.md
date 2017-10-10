# Viagogo Coding Challenge

## Problem Statement
Write a program which accepts a user location as a pair of co-ordinates, and returns a list of the five closest events, along with the cheapest ticket price for each event.

## Running the Program
This implementation was programmed in **`python 3.6`**. Make sure **`python 3`** is installed on the machine which you intend to use for the evaluation of this implementation.

To run the program, type the following command in a terminal:

```
python3 main.py
``` 

## Running Unit Tests
This implementation uses python's **`unittest`** framework for testing. Unit tests have been defined in `tests.py`.  This step **is not required** for running the program.

The unit tests can be called by typing the following command in a terminal:

```
python3 tests.py
```
## Assumptions
* The maximum number of tickets that can be assigned to a **randomly generated event** has an upper limit on `MAX_NUMBER_OF_TICKETS` which is set to a default value of `100`. When randomly populating the grid with events, the number of tickets that are assigned to an event is determined by a random number '_n_' such that `0 <= n <= MAX_NUMBER_OF_TICKETS`.
* Similarly, the maximum price of a **randomly generated ticket** is capped by `MAX_TICKET_PRICE` which is set to a default value of `500`. When randomly generating tickets, the price of each ticket is determined by a random number '_p_' such that `0 < p <= MAX_TICKET_PRICE`.
* The seed value for all the random value generator functions used throughout the program are controlled by `SEED_VALUE`. This variable is set to a default value of `3`. This is done to ensure reproducibility of the random population of the grid with events, tickets and locations.

## Other Questions

> How might you change your program if you needed to support multiple events at the same location?
* This program can utilize a list data structure as a data variable inside the `Location` class.  The essence of this modification would be to hold pointers to the `Event` object that are mapped to this location.
```python
class Location:
    def __init__(self, location, ...):
        ...
        self.x, self.y = location
        self.eventsAtThisLocation = [<event.Event Object>,...]
        ...
```

> How would you change your program if you were working with a much larger world size?
* For working with a much larger world size and assuming that finding _n_ nearest events is the only query my system needs to respond to, I would try to utilize an optimized strategy for representing the world. For example, an **R-Tree** is a data structure that can be used to effectively store the multi-dimensional information that is used to represent the geographic co-ordinates.
* The primary motivation for moving towards a tree-like structure in this regards arises due to the fact that when looking for the _n_ nearest events, the search space for finding these _n_ events need not span the entire input space. In other words, when looking for the top _n_ closest events in New York, the resultant geographical space where these events might exist, would highly unlikely be in Tokyo (unless our world contains very few locations and/or events).
* Representing the world using an R-Tree would optimize searching by reducing the search space of valid possible regions where a "nearest" event might be at every stage of traversing down the R-Tree. 
* Another benefit of accessing information in this manner is the improvement in time-complexity. Search/Access time-complexity would be `O(log n)`.
* The image below (accessed from https://upload.wikimedia.org/wikipedia/commons/4/46/R*-tree_built_using_topological_split.png) shows an R-Tree representation of US Postal Districts.
![R-Tree ](https://upload.wikimedia.org/wikipedia/commons/4/46/R*-tree_built_using_topological_split.png)

