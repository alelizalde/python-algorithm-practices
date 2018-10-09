class Trie(object):

    def __init__(self):
        self.root_node = {}

    def add_word(self, word):

        current_node = self.root_node
        is_new_word = False

        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]

        if 'EOW' not in current_node:
            is_new_word = True
            current_node['EOW'] = {}

        return is_new_word


def main():
    t = Trie()
    print(t.add_word('foo'))
    print(t.add_word('ood'))
    print(t.add_word('food'))
    print(t.root_node)


if __name__ == '__main__':
    main()
