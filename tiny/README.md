# Puzzler 2020: tiny.py

The goals of this implementation is to create a Python solution in as few characters and lines as possible.

Rules I've adopted:
 - shebash isn't needed
 - semi-colons count as new-lines
 - The dictionary must be passed as a program argument

At time of writing it is 3 lines and 164 characters.

```shell
wc -c tiny.py
     164 tiny.py
    
time python3 tiny.py | wc -l
     804
python tiny.py  0.55s user 0.04s system 98% cpu 0.600 total
```

It works by taking each word and splitting it into pairs, then search a representation of the graph for each pair. If all pairs are found then the word is accepted.

The tricky bit is in creating a minimal graph representation. This is discussed in more detail in `compress_graph.ipynb` but in essence: We perform random walks on the graph exhaustively until all edges have been traversed exactly once in either direction. This produces a candidate string representation which is then further shortened by deleting any characters we can. This process is repeated many times to find the shortest.

One such compressed representation is as follows:

```
whsyonsorblegohgcotnytloerchswnybtbowgcerl
```

The best graph representation I've found is 42 characters long, which I _believe_ is the theoretical limit. The theoretical limit for _any_ graph with 36 edges would be 1 start vertex + 36 traversals = 37 characters. However, this would require a single walk traversing all edges - the "Eulerian trail". That's not possible in this case because the graph contains 12 verticies with excess (odd) out-degree, which must be start or end states for a walk. Since excess degree can be start _or_ end states we can cover two per walk. Thus, 36 edges + 12/2 start states  = 42.

## Other ticks

 - `for p,q in zip(w,w[1:])` to generate all sequential pairs. Not that you don't have to shorten the argument because zip automatically take the min length.
 - `G+G[-2::-1]` so edges match in both directions.
 - I plagiarised `[print(w) for w in ...]` from JohnM's version. Before I had `print("\n".join(w for w in ...))` so I owe fully 9 characters to John's ingenuity.
 - Skipped `strip()`ing out newlines by slicing the words `w[1:-1]` (thanks Chris!)

## One line variation

There's a single line version which is a bit longer at 206 characters. This employs a couple of extra tricks: 

 - Drop the `import sys` line by replacing `sys.argv[1]` with `__builtins__.__import__('sys').argv[1]`.
 - Embed the graph variable as an aggregation of one thing.

