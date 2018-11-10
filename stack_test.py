def stack_test():
    s = []
    for i in range(5):
        s.append(i)

    print(s)
    while len(s) > 0:
        print(s.pop(), end=' ')
    print()


stack_test()
