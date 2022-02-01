
for i in range(10):
    try:
        assert i < 5
    except AssertionError:
        print("Oh no! An exception was raised.")
    else:
        print("Oh good, no exceptions were raised.")

    # usage of finally is optional.
    finally:
        print(f'Round {i} is done.', end='; ')

    print(f'Yes, Round {i} is done.')