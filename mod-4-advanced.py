'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    follow = 0
    followed = 0
    for n in social_graph:
        if n is from_member:
            for m in social_graph[n]["following"]:
                if m is to_member:
                    follow = 1
    for n in social_graph:
        if n is to_member:
            for m in social_graph[n]["following"]:
                if m is from_member:
                    followed = 1
    if (follow == 1):
        if (followed == 0):
            return "followed by"
        else:
            return "friends"
    else:
        if (followed == 0):
            return "no relationship"
        else:
            return "follower"


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    for x in board:
        if len(set(x)) == 1 and x[0] != '':
            return x[0]
    for y in range(len(board)):
        if len(set([board[row][y] for row in range(len(board))])) == 1 and board[0][y] != '':
            return board[0][y]
    if len(set([board[i][i] for i in range(len(board))])) == 1 and board[0][0] != '':
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1 and board[0][len(board)-1] != '':
        return board[0][len(board)-1]
    return 'NO WINNER'


def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    time = 0
    current_stop = first_stop
    while current_stop != second_stop:
        if (current_stop, second_stop) in route_map:
            time += route_map[(current_stop, second_stop)]['travel_time_mins']
            break
        else:
            next_stops = [stop for stop in route_map if stop[0] == current_stop]
            if len(next_stops) == 0:
                return -1
            current_stop = next_stops[0][1]
            time += route_map[next_stops[0]]['travel_time_mins']
    return time

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

zx = eta("admu", "dlsu", legs)
print (zx)