import math

def is_triplet(n1, n2, n3):
    s = sorted([n1, n2, n3])
    return int(math.pow(s[0], 2) + math.pow(s[1], 2)) == math.pow(s[2], 2)
