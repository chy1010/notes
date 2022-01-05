a = dict(c=1,e=2,f=5,g=0)

matching_procedure = iter(sorted(a.items(), key=lambda k: k[1]))
Item = next(matching_procedure)

try:
    while True:
        print(Item)
        Item = next(matching_procedure)
except StopIteration:
    print('End of procedure.')

matching_procedure = iter(sorted(a.items(), key=lambda k: k[1]))
Item = next(matching_procedure)
try:
    while True:
        print(Item)
        Item = next(matching_procedure)
        assert Item[1] != 5
        
except StopIteration:
    print('End of procedure.')
    
except AssertionError:
    raise AssertionError('this item Item[1] is 5!!')