#!/usr/bin/env python3.10
import sys


def with_conditions(mask: str):
    if mask == '0':
        print("/1")
    elif mask == '128':
        print("/2")
    elif mask == '192':
        print("/3")
    elif mask == '224':
        print("/4")
    elif mask == '240':
        print("/5")
    elif mask == '248':
        print("/6")
    elif mask == '252':
        print("/7")
    elif mask == '254':
        print("/8")
    else:
        print("Invalid mask")


def with_match_case(mask: str):
    match mask:
        case '0':
            print("/1")
        case '128':
            print("/2")
        case '192':
            print("/3")
        case '224':
            print("/4")
        case '240':
            print("/5")
        case '248':
            print("/6")
        case '252':
            print("/7")
        case '254':
            print("/8")
        case _:
            print("Invalid mask")


def with_dict(mask: str):
    print(
        {
            '0': '/1',
            '128': '/2',
            '192': '/3',
            '224': '/4',
            '240': '/5',
            '248': '/6',
            '252': '/7',
            '254': '/8'
        }.get(mask, "Invalid mask")
    )


def with_tuple(mask: str):
    try:
        print(
            "/", ('0', '128', '192', '224', '240', '248', '252', '254').index(mask) + 1,
            sep=''
        )
    except ValueError:
        print("Invalid mask")


def counting_ones(mask: str):
    # Check that mask contains only digits.
    if mask.isdigit():
        mask = int(mask)
        # Check that mask is valid.
        if mask < 255:
            # Create numerator
            x = 0
            # Convert to binary and take only binary part (e.g. 0b1101 -> 1101).
            mask = bin(mask)[2:]
            # Iterate through mask characters with numeration
            for i, n in enumerate(mask):
                if n != '1':
                    # Check that after '0' only '0'
                    if any(mask[i + 1:]):
                        print("Invalid mask")
                        return
                    break
                x += 1
            print('/', x)
    print("Invalid mask")


def main():
    # Import `statistics` decorator-function from parent directory
    sys.path.append("../../labs/statistics")

    from labs.statistics import statistic

    stats = statistic(with_conditions, with_match_case, with_dict, with_tuple, counting_ones,
                      to_file=True, calls=5)

    stats(mask="0.0.0.0")
    stats(mask="254.0.0.0")
    stats(mask="9999999999")
    stats(mask="sf3n2")


if __name__ == '__main__':
    main()
