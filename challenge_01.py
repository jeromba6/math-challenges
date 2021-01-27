#!/usr/bin/env python3

def main():
    topper = [0,[]]
    ct = 0
    max_pos = 4
    for puzzel in range(10000,100000):
        values = []
        count = 0

        solution = 0
        while not solution == puzzel:
            count += 1
            ct += 1
            if len(values) == 0 or len(values) < max_pos:
                values.append(next_value(puzzel-solution,values))
                if len(values) > 1 and values[-1] > values[-2]:
                    values[-1] == values[-2]
            else:
                values = decrease(values)
            solution = calc_solution(values)
        print('Puzzel: {}, Count: {}, Solution: {}, Values: {}'.format(puzzel,count,solution,values))
        if count > topper[0]:
            topper = [count, puzzel, values]
    print('Hardest to solve: Puzzel: {}, Count: {}, Values: {}'.format(topper[1], topper[0], topper[2]))
    print('Total tries: {}'.format(ct))

def calc_solution(val):
    solution = 0
    for v in val:
        solution += v ** 2
    return solution

def decrease(vals):
    res = vals[:-1]
    if res == []:
        print('No solutions')
        exit()
    res[-1] -= 1
    if res[-1] == 0:
        res = decrease(res)
    return res

def next_value(val,values):
    if len(values) > 1:
        return min(values[-1],int(val**0.5))
    return int(val**0.5)

def number_pos(pos):
    min_val = int('1'+'0'*(pos -1))-1
    max_val = int('9'*pos)
    val = 0
    val = random.randint(min_val,max_val)
    return val

main()