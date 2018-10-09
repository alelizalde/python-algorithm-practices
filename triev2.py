
class Trie(object):

    def __init__(self):
        self.root_node = {}


    def send_word(self, word):
        current_node = self.root_node
        is_new_word=False

        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char]={}
            current_node = current_node[char]

        if 'End of Word' not in current_node:
            is_new_word = True
            current_node['End of Word'] = {}

        return is_new_word


def main():

    trie = Trie()
    print(f"{trie.send_word ('hola')}")
    print(f"{trie.send_word('hola2')}")
    print(f"{trie.send_word('hola')}")
    print(f"{trie.send_word('a-hola')}")


if __name__ == '__main__':
    main()