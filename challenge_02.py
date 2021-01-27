#!/usr/bin/env python3

weight = 121
nr_of_parts = 5

# weight = 40
# nr_of_parts = 4

weight = 13
nr_of_parts = 3


part=[0] * nr_of_parts

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

def set_parts(part,position, nr_of_parts, weight):
    if position == 0:
        part[position] = 1
        part, valid = set_parts(part,position+1,nr_of_parts,weight)
        return part, valid
    if position == nr_of_parts - 1:
        part[position] = weight - sum(part)
        if part[position -1] >= part[position]:
            return part, False
        return part, True
    part[position]=max(part[position-1]+1,part[position])
    part, valid = set_parts(part, position + 1, nr_of_parts, weight)
    if not valid:
        part[position]=max(part[position-1]+1,part[position]+1)
        part=part[0:position+1] + [0] * (nr_of_parts - position - 1)
        part, valid = set_parts(part, position + 1, nr_of_parts, weight)
    return part, valid

while True:
    part, valid = set_parts(part, 0, nr_of_parts, weight)
    if not valid:
        print(part)
        print ('No solution posible')
        exit()
    if test_solution(part,weight):
        print(part,'    ')
        test_solution(part,weight,True)
        exit()
    else:
        print(part,'   ', end='\r')



