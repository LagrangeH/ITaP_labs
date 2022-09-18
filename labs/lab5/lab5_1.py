#!/usr/bin/env python3.10

def main():
    show_version = " *0 CISCO881-SEC-K9 FTX0000038X    "
    print(f"[1] {show_version = }")

    show_version = show_version.strip()
    print(f"[2] {show_version = }")

    show_version_splited = show_version.split()

    if 'cisco' in show_version.lower():
        print("[4] The word Cisco is contained in the string")
    else:
        print("[4] The word Cisco is not in the string")

    if '881' in show_version_splited[1]:
        print("[5] \"881\" is contained in the model number")
    else:
        print("[5] \"881\" is not included in the model number")

    print("[6] Model number: {}, serial number: {}".format(*show_version_splited[1:]))


if __name__ == '__main__':
    main()
