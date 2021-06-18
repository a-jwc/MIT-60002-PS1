###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here

    curr_weight = 0
    total_egg_count = 0
    indiv_egg_count = 0
    egg_weights_reverse = ()
    target_weight_copy = target_weight

    for e in reversed(egg_weights):
        egg_weights_reverse = egg_weights_reverse + (e,)

    for e in egg_weights_reverse:
        indiv_egg_count = target_weight_copy//int(e)
        if indiv_egg_count > 0:
            memo.update({e: indiv_egg_count})
            curr_weight = indiv_egg_count * e
            target_weight_copy = target_weight_copy - curr_weight
            indiv_egg_count = 0
    
    print(memo)
    output_string = ""
    for m in memo:
        total_egg_count += memo.get(m)
        output_string += str(memo.get(m)) + " * " + str(m) + " + "
        # output_string += " + "
    output_string = output_string.rstrip(output_string[-1])
    output_string = output_string.rstrip(output_string[-1])
    output_string = "(" + output_string + "= " + str(target_weight) + ")"
    return str(total_egg_count) + " " + output_string


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    # egg_weights = (1, 5, 10, 25)
    # n = 99
    # print("Egg weights = ", egg_weights)
    # print("n =", n)
    # print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    # print("Actual output:", dp_make_weight(egg_weights, n))
    # print()

    egg_weights = (1, 5, 7, 10, 13, 25, 67, 78, 94, 2324, 2333, 2349)
    n = 934634623634626243627275
    print("Egg weights = ", egg_weights)
    print("n =", n)
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()