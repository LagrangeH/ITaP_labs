#!/usr/bin/env python3.10

def main():
    user_ip = input("Enter IP address in 255.255.255.255 format: ").split('.')

    n = int(user_ip[0])

    if n < 128:
        return "A"
    elif n < 192:
        return "B"
    elif n < 224:
        return "C"
    elif n < 240:
        return "D"
    elif n < 255:
        return "E"
    else:
        raise ValueError


if __name__ == '__main__':
    try:
        print("IP address belongs to class", main())
    except ValueError:
        print("Invalid IP address entered")
