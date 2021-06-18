###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import importlib

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    dict = {}
    with open(filename, 'r') as f:
        list = [line.strip() for line in f]
        for pair in list:
            i = pair.split(",")
            dict[i[0]] = i[1]
    return dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    trip = []
    agg_cows = []
    remaining = 10
    curr_weight = 0
    trip_count = 0
    cows_copy = cows
    print(cows_copy)

    while len(cows_copy) != 0:
        heaviest = 0
        heaviest_cow = ""
        if curr_weight == 0:
            for cow, weight in cows_copy.items():
                if int(weight) > int(heaviest):
                    heaviest = weight
                    heaviest_cow = cow
            trip.append(heaviest_cow)
            curr_weight += int(heaviest)
            remaining = limit - curr_weight       
        elif curr_weight < limit:
            for cow, weight in cows_copy.items():
                if int(weight) > int(heaviest) and cow not in trip and int(weight) <= remaining:
                    heaviest = weight
                    heaviest_cow = cow
            if remaining >= int(heaviest) and heaviest_cow != "":
                trip.append(heaviest_cow)
                # cows_copy = dict(cows.items())
                curr_weight += int(heaviest)
                remaining = limit - curr_weight                
            else:
                curr_weight = limit
                remaining = 0
        else:
            for cow in trip:
                if cow in cows:
                    cows.pop(cow)
            agg_cows.append(trip)
            cows_copy = cows          
            trip = []
            curr_weight = 0
            remaining = 0
            trip_count += 1

    print("Trip count:", trip_count)

    return agg_cows

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    curr_weight = 0
    optimal_list = []
    optimal_trip_count = 10
    p_weights = []
    weights_list = []
    overall_overweight = False
    
    for partition in get_partitions(cows):
        # print(partition)
        overweight = False
        overall_overweight = False
        trip_count = 0
        for p in partition:
            for cow, weight in cows.items():
                if cow in p:
                    curr_weight += int(weight)
            if(curr_weight <= limit):
                overweight = False
            else:
                overweight = True
            p_weights.append(curr_weight)
            trip_count += 1
            p_weights.append(trip_count)
            p_weights.append(overweight)
            weights_list.append(p_weights)
            curr_weight = 0
            p_weights = []
            if overweight == True:
                overall_overweight = True
    
        if trip_count <= optimal_trip_count and overall_overweight == False:
            optimal_trip_count = trip_count
            optimal_list = []
            optimal_list.extend(partition)
            print("optimal list:", optimal_list, "optimal trip count:", optimal_trip_count)
    if optimal_list == []:
        print("no solution")

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start_time = time.time()
    greedy_cow_transport(load_cows("ps1_cow_data.txt"), 10)
    print("Execution Time (Greedy):", time.time() - start_time)

    start_time = time.time()
    brute_force_cow_transport(load_cows("ps1_cow_data.txt"), 10)
    print("Execution Time (Brute Force):", time.time() - start_time)
