from math import inf


class MinStack:
    def __init__(self):
        self.stack = []

    def min(self):
        minStack = []
        minValue  = inf
        for i in range(0, len(self.stack)): # 5, 4, 3, 2, 1
            value = self.stack.pop() # 1
            if value < minValue: #
                minValue = value
            minStack.append(value)
        self.stack = minStack[::-1]
        return minValue

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)


def main():
    s = MinStack()
    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    print(s.min())
    s.pop()
    print(s.min())
    print(s.peek())
    print(s.size())


if __name__ == '__main__':
    main()
