def calculate(lime):
    items = []

    for i in range(lime):
        position = len(items) - 1

        if len(items) == 0:
            items.insert(0, 1)
        else:
            flag = True
            v = 1
            while flag:
                flag = iguales(items[position], v)
                items.pop()
                v += 1
                position -= 1
                if position <= 0:
                    flag = False
            items[position] = v

    print(items)


def iguales(ultimo, v):
    if ultimo == v:
        return True
    else:
        return False


def main():
    print(calculate(5))


if __name__ == '__main__':
    main()