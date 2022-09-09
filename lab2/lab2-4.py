#!/usr/bin/env python3.10

def main(*x):
    user_input = input("Enter data for processing separated by a space: ")

    list3 = user_input.split()
    print(f"{list3 = }")

    len_list3 = len(list3)
    print(f"{len_list3 = }")

    count_x = sum(list3.count(string) for string in x)
    print(f"For x = {list(x)} {count_x = }")


if __name__ == '__main__':
    # Since the task does not say what exactly to count,
    # we will grant such a right to the user.
    # We also use set to avoid recalculating the same value.
    main(*set(input("Enter data for counting separated by a space: ").split(r'\s')))
