def demo():
    yield 10
    yield 20
d=demo()
#print(d.__next__())
print(next(d))
print(next(d))