[print(w)for G in['whsyonsorblegohgcotnytloerchswnybtbowgcerl']for w in{l.strip().lower()for l in open(__builtins__.__import__('sys').argv[1])}if w[0]in G and all(p+q in G+G[-2::-1]for p,q in zip(w,w[1:]))]