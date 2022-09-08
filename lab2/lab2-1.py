#!/usr/bin/env python3.10

def print_ip_list(text: str, lst: list) -> None:
    """For more readable printing `ip_list`"""
    print(text, *lst, sep='\n\t', end=f"\n{16 * '-'}\n")


def main():
    ip_list = [
        '10.1.1.1',
        '10.1.1.2',
        '10.1.1.3',
        '10.1.1.4',
        '10.1.1.5',
    ]

    # Task 1
    print(f"First IP: {ip_list[0]}")
    print(f"Last IP: {ip_list[-1]}")

    # Task 2
    ip_list.append('10.1.1.6')
    ip_list.extend(['10.1.1.7', '10.1.1.8'])
    ip_list += ['10.1.1.9', '10.1.1.10']

    print_ip_list("New IP list:", ip_list)
    print(f"Second IP: {ip_list[1]}")
    print(f"Penultimate IP: {ip_list[-2]}")

    ip_list.pop(0)
    ip_list.pop()

    ip_list[0] = '2.2.2.2'
    print(f"New first IP: {ip_list[0]}")

    print_ip_list("Result IP list:", ip_list)


if __name__ == '__main__':
    main()
