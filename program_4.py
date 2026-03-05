# By Nathan Nelsen
# Written 3/5/26
# Coordinates

# Write a distance function that will take two 3-dimensional coordinates (as input)
# and will return (as output) the distance between those points in space.
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)

import math

def distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return dist


def main():
    try:
        print("Enter the first 3D coordinate:")
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        z1 = float(input("z1: "))
        coord1 = (x1, y1, z1)

        print("\nEnter the second 3D coordinate:")
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        z2 = float(input("z2: "))
        coord2 = (x2, y2, z2)

        # call distance function
        dist = distance(coord1, coord2)

        # display result
        print("\nThe distance between the points is:", format(dist, '.2f'))

    except ValueError:
        print("Error: Please enter valid numeric values.")

main()
