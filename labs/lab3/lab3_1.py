#!/venv/bin python3.10

def main():
    ip_list = [
        '10.1.1.1',
        '10.1.1.2',
        '10.1.1.3',
        '10.1.1.2',
        '10.1.1.3',
        '10.1.1.1',
        '10.1.1.1',
        '10.1.1.2',
    ]

    ip_addr_unique = set(ip_list)
    print(f"[2] {ip_addr_unique = }")

    ip_sorted = sorted(ip_addr_unique)
    print(f"[3] {ip_sorted = }")

    len_iplist = len(ip_addr_unique)
    print(f"[4] {len_iplist = }")


if __name__ == '__main__':
    main()
