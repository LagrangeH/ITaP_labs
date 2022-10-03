#!/usr/bin/env python3.10

def ssh_conn(ip_address, username, password):
    print(f"{ip_address = }\n{username = }\n{password = }")


if __name__ == '__main__':
    ssh_conn(ip_address='192.168.0.10', username='root', password='toor')
    ssh_conn('192.168.0.10', username='admin', password='adminadmin')
