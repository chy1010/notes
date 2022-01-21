a = [1,2,3,4]

iter_a = iter(a)

print(next(iter_a))

# next(obj) is equivalent to obj.__next__()
print(iter_a.__next__())

## equivalent code to a for loop

for item in a:
    print(item)

iter_a = iter(a)
while True:
    try:
        item = next(iter_a)
        print(item)
    except StopIteration:
        break
