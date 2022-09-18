#!/usr/bin/env python3.10

def main(mask: str):
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


if __name__ == '__main__':
    user_mask = input("Enter mask: ").split('.')[0]
    main(user_mask)
