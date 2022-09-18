#!/usr/bin/env python3.10

def main():
    ips = [f'10.10.100.{i}' for i in range(1, 255)]
    for i, ip in enumerate(ips):
        print(f"{i} -> {ip}")

    print("--------")
    for ip in ips[2:6]:
        print(ip)


if __name__ == '__main__':
    main()
