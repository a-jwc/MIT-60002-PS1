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
            split_list = pair.split(",")
            dict[split_list[0]] = [split_list(1)]
    print(dict)
    return dict