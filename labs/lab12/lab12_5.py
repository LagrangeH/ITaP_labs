#!/usr/bin/env python3.10


def main():
    result = []
    while (d := input("Enter data: ")) != 'end':
        if d.isalpha():
            result.append(d)
    return result


if __name__ == '__main__':
    print(main())
