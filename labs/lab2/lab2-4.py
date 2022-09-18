#!/usr/bin/env python3.10

def main():
    user_input = input("Enter data for processing: ")

    list3 = list(user_input)
    print(f"{list3 = }")

    len_list3 = len(list3)
    print(f"{len_list3 = }")

    count_x = sum(list3.count(string) for string in ('2', '3'))
    print(f"2 and 3 contains in list3 {count_x} times")


if __name__ == '__main__':
    main()
