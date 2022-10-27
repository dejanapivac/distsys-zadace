def f6(x, y):
    assert type(x) == type(y)
    assert isinstance(x, list) or isinstance(x, dict)
    assert isinstance(y, list) or isinstance(y, dict)
    return (x + y if type(x) == list else x | y)

# print(f6( [1,2,1,2],[3,2]))
print(f6( [1,2,1,2], "3,2"))
# print(f6({1:2,3:2},{5:2,4:1}))
