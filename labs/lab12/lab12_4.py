#!/usr/bin/env python3.10

if __name__ == '__main__':
    nums = (45, 36, 39, 37, 130, 105, 220, 169)
    e = lambda x: not x % 13
    print([x for x in nums if e(x)])
