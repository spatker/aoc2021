from utils.util import file2list

def test_bit(i, bit):
    return bool((i & (1 << bit)) >> bit)

def to_num(l):
    res = 0
    for i in l:
        res <<= 1
        res |= i
    return res

def most_common(ones, zeros):
    res = [0 for _ in ones]
    for i in range(0, len(ones)):
        if ones[i] != zeros[i]:
            res[i] = ones[i] > zeros[i]
        else:
            res[i] = -1
    return res

def count_bits(l, mask_length):
    ones = [0]*mask_length
    zeros = [0]*mask_length
    for i in l:
        for j in range(0, mask_length):
            is_set = test_bit(i, j)
            idx = mask_length - 1 - j
            ones[idx] += is_set
            zeros[idx] += not is_set
    return ones, zeros

def get_o2(l, length):
    if(len(l) == 1):
        return l[0]
    
    ones, zeros = count_bits(l, length)
    mc = most_common(ones, zeros)
    search = mc[0] if mc[0] >= 0 else 1
    new_l = [x for x in l if test_bit(x, length-1) == search]
    
    return get_o2(new_l, length-1)

def get_co2(l, length):
    if(len(l) == 1):
        return l[0]
    
    ones, zeros = count_bits(l, length)
    mc = most_common(ones, zeros)
    lc = list(map(lambda x: not x if x >=0 else 0, mc))
    search = lc[0] if lc[0] >= 0 else 0
    new_l = [x for x in l if test_bit(x, length-1) == search]
    
    return get_co2(new_l, length-1)

def main():
    l = file2list("./3/input.txt")
    length = len(l[0])
    l = [int(x, 2) for x in l]

    ones, zeros = count_bits(l, length)
    mc = most_common(ones, zeros)
    lc = [not x for x in mc]
    gamma = to_num(mc)
    epsilon = to_num(lc)
    print(gamma*epsilon)

    o2 = get_o2(l, length)
    co2 = get_co2(l, length)
    print(o2*co2)




main()