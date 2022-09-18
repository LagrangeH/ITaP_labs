#!/usr/bin/env python3.10

def main():
    device = {
        'ip': '10.10.10.12',
        'username': 'user',
        'password': 'pass',
    }

    print(f"{device['password'] = }")

    device_key, device_value = device.keys(), device.values()
    print(f"{device_key = }\n{device_value = }")

    add_config = {
        'device_type': 'huawei',
        'session_log': 'output.txt',
    }
    print(f"{add_config = }")

    device.update(add_config)
    print(f"{device = }")


if __name__ == '__main__':
    main()
