#!/usr/bin/env python3.10

def task_1():
    # Tasks 2-4
    list_devices = []
    file = open('devices.txt', 'rt')
    for item in file:
        item.strip()
        list_devices.append(item)
        print(item)
    file.close()
    print(f"{list_devices = }")

    # Tasks 5-8
    with open('devices.txt', 'r+') as file_2:
        old_file = file_2.readlines()
        file_2.seek(0)
        file_2.write("/---START---/\n")
        for line in old_file:
            file_2.write(line)
        file_2.write("/---END---/\n")

    with open('devices.txt', 'rt') as file_r:
        print(file_r.read())


# def task_2():
#     from pprint import pprint
#
#     pprint(set(map(lambda x: tuple(l[:2]) if 'active' in (l := x.split()) else None, open('show_vlan.txt', 'rt').readlines()[2:])))


if __name__ == '__main__':
    task_2()
