from typing import List

def outer_product(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]

def vector(a: List[int], b: List[int]):
    return [b[0]-a[0], b[1]-a[1]]

def two_segments_intersect(seg1: List[List[int]], seg2: List[List[int]]):
    a, b = seg1
    c, d = seg2

    ab = vector(a,b)
    ac = vector(a,c)
    ad = vector(a,d)

    cd = vector(c,d)
    ca = vector(c,a)
    cb = vector(c,b)

    # oppsite signs if on different sides
    return (outer_product(ab, ac) * outer_product(ab, ad) <= 0) and (
        outer_product(cd, ca) * outer_product(cd, cb) <= 0)

if __name__ == '__main__':
    
    seg1 = [[0,0], [1,1]]
    seg2 = [[1,0], [0,1]]
    seg3 = [[10,0], [11,3]]

    print(two_segments_intersect(seg1, seg2))
    print(two_segments_intersect(seg1, seg3))
    
    from time import time
    start = time()
    two_segments_intersect(seg1, seg2)
    two_segments_intersect(seg1, seg3)
    for _ in range(10000):
        two_segments_intersect(seg1, seg2)
        two_segments_intersect(seg1, seg3)
    print(f'time duration: {time() - start}')