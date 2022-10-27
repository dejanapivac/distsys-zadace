def f4(l1, l2):
    if not (len(l1) == len(l2)):
        raise Exception("lists should be same len")
    return [a if a==b else -1 for a,b in zip(l1,l2) ]

print(f4( [1,2,3,4,5],[2,2,4,4,5]))