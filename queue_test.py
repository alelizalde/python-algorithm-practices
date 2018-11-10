import queue


def test_queue():
    q = queue.Queue()

    for i in range(5):
        q.put(i)

    print(q.queue)
    while not q.empty():
        print(q.get(), end=' ')
    print()


test_queue()