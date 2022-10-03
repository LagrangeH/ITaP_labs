#!/usr/bin/env python3.10
from random import randint


def main(f: str = '192', s: str = '168', t: str = '1') -> None:
    print('.'.join((f, s, t, str(randint(1, 254)))))


if __name__ == '__main__':
    main()
    main('192', '167', '0')
    main(f='191', s='166', t='2')
    main('192', s='160', t='1')
