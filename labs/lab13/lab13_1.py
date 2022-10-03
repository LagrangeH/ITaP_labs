#!/usr/bin/env python3.10


def main():
    config_acl = 'acl 3001 \nrule 5 permit tcp source 10.1.4.1 0 destination-port eq telnet \nrule 10 deny tcp'
    try:
        file = open('lab13_1.txt')
    except FileNotFoundError:
        filename = input("Такого файла нет, давайте создадим его. Введите имя файла, который хотите создать: ")
        if filename != 'lab13_1.txt':
            print("Что-то пошло не так")
            return
        file = open(filename, 'wt')
        file.write(config_acl)
    except Exception:
        print("Непредвиденная ошибка")
        return
    else:
        print("Файл был найден")
    finally:
        file.close()
    with open('lab13_1.txt', 'rt') as  file:
        print(file.read())


if __name__ == '__main__':
    main()
