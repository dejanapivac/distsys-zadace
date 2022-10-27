def f2(l, d):
    assert (isinstance(l, list) and isinstance(d, dict))
    assert len(l) == len(d)
    assert (all(isinstance(i, int) for i in l) and all(isinstance(i, int) for i in d))
    return {k:v if 10 > v > 5 else -1 for k,v in zip(d,l)}

print(f2([8, 7, 1], {1: 2, 2: 1, 3: 2}))
