#!/usr/bin/env python3

GRAPH = {
    'b': {'r', 'l', 't', 'y', 'o'},
    'r': {'b', 'l', 'e', 'c', 'o'},
    'l': {'b', 'r', 't', 'e', 'o'},
    't': {'y', 'b', 'l', 'n', 'o'},
    'y': {'b', 't', 'n', 's', 'o'},
    'e': {'r', 'c', 'g', 'l', 'o'},
    'o': {'b', 'r', 'l', 't', 'y', 'e', 'n', 'c', 'g', 'w', 's', 'h'},
    'n': {'s', 'w', 'y', 't', 'o'},
    'c': {'r', 'e', 'g', 'h', 'o'},
    'g': {'h', 'w', 'e', 'c', 'o'},
    'w': {'s', 'n', 'g', 'h', 'o'},
    's': {'y', 'n', 'w', 'h', 'o'},
    'h': {'s', 'w', 'g', 'c', 'o'}
}

DEFAULT_WORDS_PATH = "/usr/share/dict/words"


def is_word_in_graph(word):
    return word[0] in GRAPH and all(
        p in GRAPH and q in GRAPH[p]
        for p, q in zip(word[:-1], word[1:])
    )


def find_words(words):
    for word in words:
        if is_word_in_graph(word):
            yield word


def read_words(path):
    with open(path) as file:
        return {line.strip().lower() for line in file.readlines()}


def main():
    import sys

    if len(sys.argv) > 2:
        print(f"Usage: {__file__} [path/to/words/lists]")
        exit(-1)

    words_path = DEFAULT_WORDS_PATH
    if len(sys.argv) == 2:
        words_path = sys.argv[1]

    for word in find_words(read_words(words_path)):
        print(word)


if __name__ == '__main__':
    main()
