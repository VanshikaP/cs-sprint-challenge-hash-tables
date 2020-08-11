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
    # put all tickets except source in hash table with source as key and destination as value
    sourceTicket = None
    ticketsMap = {}

    for i in range(length):
        if tickets[i].source is 'NONE':
            sourceTicket = tickets[i]
        else:
            ticketsMap[tickets[i].source] = tickets[i].destination
    
    # start route with destination of startRoute and traverse through map to find ultimate destination
    flying = True
    route = []
    point = sourceTicket.destination
    while flying:
        route.append(point)
        if ticketsMap[point] is 'NONE':
            flying = False
            route.append('NONE')
        else:
            point = ticketsMap[point]

    return route


