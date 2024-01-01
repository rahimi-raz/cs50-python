g={}



while True:

    try:
        inp=input().upper()
        v=g[inp]
        g[inp]=g[inp]+1
    except KeyError:
         g[inp]=1
    except EOFError:
        for i in sorted(g):
            print(g[i], i)
        break



