# Lifting weights

# Ollie is new to the gym and is figuring out the maximum weights she can lift. The maximum capacityof the barbell is given as maxCapacity.
# Each barbell plate has a weight, given by weights[i]. Now Ollie has to select as many plates as she can but the total weight of the selected plates should not exceed maxCapacity.
# What is the maximum weight of plates Ollie can add to the barbell?
# For example, given barbell plates of weights of 1, 3 and 5 lbs and a barbell of maximum capacity 7 lbs 
# the right plates to insert would be 1 and 5 lbs (1+5 = 6), thus making the right answer 6

# Function Description
# Complete the weightCapacity function in the editor below. The function must be return an integer denoting the maximum capacity of items that she can lift.


def weightCapacity(weights, maxCapacity):
    # create set with all combinations
    comb = set([0])
    # loop weights list
    for w in weights:
        # create a set to save comb 
        temp = set()
        # loop comb set
        for c in comb:
            if w + c == maxCapacity:
                return maxCapacity
            elif w + c < maxCapacity:
                temp.add(w + c)
        comb.update(temp)
    return max(comb)
