class Trie(object):

    def __init__(self):
        self.root_node = {}

    def add_word(self, word):

        is_new_node = False
        current_node = self.root_node

        for char in word:
            if char not in current_node:
                is_new_node = True
                current_node[char] = {}

            current_node = current_node[char]

        if 'End Of Word' not in current_node:
            is_new_node = True
            current_node['End Of Word'] = {}

        return is_new_node

    def search_word(self, word):

        current_node = self.root_node

        try:
            for char in word:
                current_node = current_node[char]

            current_node = current_node['End Of Word']
            return True
        except Exception:
            return False

    def rm_word(self, char_to_rm, current_dict):

        current_node = current_dict
        current_keys = current_node.keys()

        for char in current_keys:
            try:
                current_node = current_node[char]
                self.rm_word(char_to_rm, current_node)

                if char_to_rm in current_keys:
                    del current_node[char_to_rm]
                    return True
            except KeyError:
                pass

        return False


def main():

    trie = Trie()
    print(f"{trie.add_word('all')}")
    print(f"{trie.add_word('hello')}")
    print(f"{trie.add_word('hello')}")
    print(f"{trie.add_word('hello2')}")
    print(f"{trie.add_word('hello3')}")
    print(f"{trie.search_word('hello2')}")

    print(trie.root_node)

    print(f"{trie.rm_word('2', trie.root_node)}")

    print(trie.root_node)

    print(f"{trie.add_word('hello4')}")

    print(trie.root_node)


if __name__ == '__main__':
    main()