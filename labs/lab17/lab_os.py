import os

def main():
    tree = '/tree'
    switches = '/switches'
    routers = '/routers'
    cisco = '/cisco'
    other = '/other'
    for path in (
        "/tree/switches/other/cisco",
        "/tree/switches/other/huawei",
        "/tree/routers/other/juniper",
        "/tree/routers/other/huawei",
        "/tree/routers/other/huawei",
        "/tree/cisco/other/cisco",
        "/tree/cisco/other/meraki",
    ):
        os.mkdir(path)
    os.rename("/tree/routers/other/juniper", "/tree/routers/other/nokia")
    with open('tree/cisco/other/readme.txt', 'w') as readme:
        readme.write("Don't forget to save all configurations!")


if __name__ == '__main__':
    main()
