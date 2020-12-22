def trees_list(filename):
    """ Returns list of tree (#) slope terrain
    """
    infile = open(filename, "r")
    slope = []
    while True:
        slope_line = infile.readline()
   
        if len(slope_line) == 0:
            break
        if "\n" in slope_line:
            slope_line = slope_line[:-1] 
    
        slope.append(slope_line)

    return slope


def trees_in_ski_route(filename):
    """ Returns number of trees encounters on a 3 across, 1 down ski route down the slope
    """
    slope = trees_list(filename) # put the slope into a list
    slope_width = len(slope[0]) # find out the width of the slope to use as the remainder finder
    slope_horiz_pos = 0 # start at the left end of the slope
    slope_vert_pos = 0 # start at the first row of the slope
    horiz_increment = 3 # number of indexes to move across (on the row) each iteration
    tree_count = 0

    for slope_vert_pos in range(len(slope)): # range function naturally iterates the vertical row increment by 1 each iteration which is desired for part 1
        slope_horiz_pos = slope_horiz_pos % slope_width
        if slope[slope_vert_pos][slope_horiz_pos] == "#":
            tree_count += 1
        
        slope_horiz_pos += horiz_increment

    return tree_count

def trees_in_ski_route_inc_cont(filename, horiz_increment, vert_increment):
    """ Returns number of trees encounters on a 3 across, 1 down ski route down the slope
    """
    slope = trees_list(filename) # put the slope into a list
    slope_width = len(slope[0]) # find out the width of the slope to use as the remainder finder
    slope_horiz_pos = 0 # start at the left end of the slope
    slope_vert_pos = 0 # start at the first row of the slope
    tree_count = 0

    for slope_vert_pos in range(0, len(slope), vert_increment):
        slope_horiz_pos = slope_horiz_pos % slope_width
        if slope[slope_vert_pos][slope_horiz_pos] == "#":
            tree_count += 1
        
        slope_horiz_pos += horiz_increment


    return tree_count

# print(trees_list("day_3.txt"))

print("The answer for part 1 is: ", trees_in_ski_route("day_3.txt"))

slope_design_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total_trees = 1
for i, j in slope_design_list:
    total_trees *= trees_in_ski_route_inc_cont("day_3.txt", i, j)
    
print("The answer for part 2 is: ", total_trees)
