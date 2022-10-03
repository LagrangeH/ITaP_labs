#!/usr/bin/env python3.10

def ssh_conn2(ip_address, username, password, device_type='huawei_vrp'):
    print(f"{ip_address = }\n{username = }\n{password = }\n{device_type = }")


if __name__ == '__main__':
    ssh_conn2(ip_address='192.168.0.10', username='root', password='toor', device_type='cisco')
    ssh_conn2(ip_address='192.168.0.20', username='root', password='qwerty')
    data = {
        'ip_address': '192.168.0.30',
        'username': 'admin1',
        'password': 'adminadminadmin',
        'device_type': 'apple'
    }
    ssh_conn2(**data)
