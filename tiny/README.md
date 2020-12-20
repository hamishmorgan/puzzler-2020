# Puzzler 2020: tiny.py

The goals of this implementation is to create a Python solution in as few characters and lines as possible. 

At time of writing it is a single line and 201 characters. You can make is slightly less characters in two lines. 

```shell
wc -c tiny.py
     201 tiny.py
    
time python tiny.py  | wc -l
     439
python tiny.py  0.55s user 0.04s system 98% cpu 0.600 total
```

It works by taking each word and splitting it into pairs, then search a representation of the graph for each pair. If all pairs are found then the word is accepted.

The tricky bit is in creating a minimal graph representation. This is discussed in more detail in `compress_graph.ipynb` but in essence: We perform random walks on the graph exhaustively until all edges have been traversed exactly once in either direction. This produces a candidate string representation which is then further shortened by deleting any characters we can. This process is repeated many times to find the shortest. At time of writing the best I've found is 42 characters long.