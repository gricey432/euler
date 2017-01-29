from math import log10, ceil, sqrt
from itertools import permutations


def digits(n):
    d = []
    n = abs(n)
    while n >= 1:
        d.append(n % 10)
        n //= 10
    return d


def digit_length(n):
    return int(log10(n)) + 1


def is_pandigital(n):
    d = digits(n)
    if len(d) != len(set(d)):
        return False

    for m in range(digit_length(n)):
        if m+1 not in d:
            return False
    return True


def is_prime(n):
    j = 2
    root = int(ceil(sqrt(n)))
    while j <= root:
        if n % j == 0:
            return False
        j += 1
    return True


def main():
    for d in range(9, 0, -1):
        for p in permutations(range(d, 0, -1)):
            n = sum(v * 10 ** (len(p) - i - 1) for i, v in enumerate(p))
            if is_pandigital(n) and is_prime(n):
                return n


print main()
