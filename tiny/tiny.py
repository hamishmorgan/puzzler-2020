import sys
G='whsyonsorblegohgcotnytloerchswnybtbowgcerl'
[print(w)for w in open(sys.argv[1])if w[0]in G and all(p+q in G+G[-2::-1]for p,q in zip(w,w[1:-1]))]