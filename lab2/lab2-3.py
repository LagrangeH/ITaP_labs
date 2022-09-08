#!/usr/bin/env python3.10

from random import randint


def main():
    acl_list = [randint(1, 199) for i in range(10)]
    acl_list.sort()
    print(f"Sorted ACL list: {acl_list}")

    acl_list.insert(-1, acl_list.pop(0))
    acl_list.insert(0, acl_list.pop())

    acl_list.reverse()
    print(f"Reversed ACL list with method reverse: {acl_list}")
    acl_list = acl_list[::-1]
    print(f"Reversed ACL list with method reverse: {acl_list[::-1]}")

    # If it is initially known that the length of the list is 10
    acl_list1, acl_list2 = acl_list[:5], acl_list[5:]
    print(f'{acl_list1 = }\n{acl_list2 = }')


if __name__ == '__main__':
    main()
