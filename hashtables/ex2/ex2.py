#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    tickdict = {}

    for i in tickets:
        if i.source == "NONE":
            tickdict["starts"] = i
        else:
            tickdict[i.source] = i

    route = [None] * length

    route[0] = tickdict["starts"].destination

    for index, i in enumerate(route):
        if index + 1 == length:
            break
        route[index + 1] = tickdict[i].destination

    return route
