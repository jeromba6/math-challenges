#!/usr/bin/env python3

"""
This program returns the weight of a givven number of pieces that a weight
breaks in to. The combiniation of the pieces makes it posible to weight every
 posible weight from 1 to the original weight in steps of 1
"""

__author__ = "Jeroen van Gemert"
__license__ = "GPL"
__email__ = "github@jeroen.van.gemert.net"
__status__ = "Production"


# Set variables
weight = 40
nr_of_parts = 4

# weight = 13
# nr_of_parts = 3

# weight = 121
# nr_of_parts = 5


def main():
    parts = [0] * nr_of_parts
    # Endless loop
    while True:
        # Call function for determine an option of combination of weights
        parts, valid = set_parts(parts, 0, nr_of_parts, weight)

        # Check or there might be a still a vallid solution posible
        if not valid:
            print(parts)
            print ('No solution posible')
            exit()

        # Check or current solution is vallid
        if test_solution(parts,weight):
            print(parts,'    ')
            test_solution(parts,weight,True)
            exit()

        # Output current solution which is not vallid
        else:
            print(parts,'   ', end='\r')


# For each weight check or it can be made in a combination of the pieces
def test_solution(p, weight,show_result=False):
    cv=[0] * nr_of_parts
    for check_weight in range(1,weight+1):
        sum_ok = False
        for nr_of_parts_used in range(2 ** nr_of_parts):
            for options in range(2 ** nr_of_parts):
                for pos in range(nr_of_parts):
                    pos_neg = int('{0:0{1}b}'.format(options,nr_of_parts)[pos]) * 2 - 1
                    use = int('{0:0{1}b}'.format(nr_of_parts_used,nr_of_parts)[pos])
                    cv[pos] = p[pos] * pos_neg * use
                if sum(cv) == check_weight:
                    if show_result:
                        print("{} = sum of:{}".format(check_weight, cv))
                    sum_ok = True
                    break
        if sum_ok:
            continue
        else:
            return False
    return True


# Sugest next solution
def set_parts(parts,position, nr_of_parts, weight):
    if position == 0:
        parts[position] = 1
        parts, valid = set_parts(parts,position+1,nr_of_parts,weight)
        return parts, valid
    if position == nr_of_parts - 1:
        parts[position] = weight - sum(parts)
        if parts[position -1] >= parts[position]:
            return parts, False
        return parts, True
    parts[position]=max(parts[position-1]+1,parts[position])
    parts, valid = set_parts(parts, position + 1, nr_of_parts, weight)
    if not valid:
        parts[position]=max(parts[position-1]+1,parts[position]+1)
        parts=parts[0:position+1] + [0] * (nr_of_parts - position - 1)
        parts, valid = set_parts(parts, position + 1, nr_of_parts, weight)
    return parts, valid


main()




