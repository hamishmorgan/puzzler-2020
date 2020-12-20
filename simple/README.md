# Puzzler 2020: simple.py

This is a fairly straightforward implementation. The graph is stored as a dictionary, where the keys are the source verticies and values are the set destination verticies for which there are valid edges. Words are matched by checking that all subsequent pairs of characters exists as edges in the graph. There's also a check that the first character in the word exists as a vertex because otherwise all single character words are accepted. 

Usage:

```shell
./simple.py /usr/share/dict/words
gel
ronyon
colorer
bleo
geologer
tonsor
bo
tyt
snot
core
...
```


```shell
time ./simple.py /usr/share/dict/words | wc -l
439
./simple.py  0.34s user 0.03s system 98% cpu 0.373 total
```