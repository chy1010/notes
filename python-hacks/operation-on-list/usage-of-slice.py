

if __name__ == '__main__':
    
    a = [1, 2, 3, 4, 5, 6, 7]
    print(a)
    # substitute
    a[2:] = a[5:]
    print(a)
    
    ## reverse
    # the -1 used in the first 2 slices means the last element.
    # if we want to show the first element when using reverse order,
    # just put the second slice to be None
    print(a[-1:0:-1])  # no fist element
    print(a[-1:-1:-1]) # -1 is the last element, not the index before 0
    print(a[-1:None:-1]) # will show the first element
    print(a[-1::-1])