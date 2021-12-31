def check_neighbor(coord_1, coord_2):
    a, b = coord_1
    c, d = coord_2
    return (a==c and (b==d+1 or d==b+1)) or (b==d and (a==c+1 or c==a+1))

def check_neighbor1D(x,y):
    return x==y+1 or y==x+1

if __name__ == '__main__':
    
    p = (-2,-1)
    q = (-2,-2)    
    print(check_neighbor(p, q))