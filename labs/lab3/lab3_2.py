#!/usr/bin/env python3.10
from random import randint


def main():
    vlan_mos = [randint(1, 10) for i in range(8)]
    vlan_kursk = [randint(1, 15) for i in range(10)]
    vlan_novosib = [randint(1, 20) for i in range(15)]
    print(f"[3] {vlan_mos = }")
    print(f"[3] {vlan_kursk = }")
    print(f"[3] {vlan_novosib = }")

    # If we keep in mind that vlans are unique in Moscow itself,
    # and not among the three cities.
    print(f"[4] There are {len(set(vlan_mos))} unique vlans in Moscow")

    vlan_mos = set(vlan_mos)
    vlan_kursk = set(vlan_kursk)
    vlan_novosib = set(vlan_novosib)
    print(f"[5] {vlan_mos = }")
    print(f"[5] {vlan_kursk = }")
    print(f"[5] {vlan_novosib = }")

    print("[6] Vlans that are the same in Moscow and Kursk: ",
          vlan_mos & vlan_kursk)
    print("[7] Vlans that are the same in Moscow, Kursk and Novosibirsk: ",
          vlan_mos & vlan_kursk & vlan_novosib)
    # If we keep in mind those vlans
    # that are unique in Novosibirsk relative to other cities.
    print("[8] Vlans that are unique in Novosibirsk: ",
          vlan_novosib - (vlan_mos | vlan_kursk))


if __name__ == '__main__':
    main()
