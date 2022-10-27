def f1(x):
    assert all(isinstance(i, str) for i in x)
    return [i for i in x if len(i) > 4]

print(f1(["Pas", "Macka", "Stol"]))

