#!/usr/bin/env python3.10


def main():
    ip_addr = "172.16.1.1,172.16.2.1,172.16.3.1,172.16.4.1"

    for ip in ip_addr.split(','):
        print(ip)


if __name__ == '__main__':
    main()
