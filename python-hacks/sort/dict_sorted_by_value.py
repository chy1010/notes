"""
as title.
"""

def return_sorted_by_value(data: dict, descending: bool = False):
    return dict(sorted(data.items(), key=lambda d: d[1], reverse=descending))


if __name__ == '__main__':
    
    scores = dict(A=90, B=100, C=98, D=50)

    for k, v in return_sorted_by_value(scores, descending=True).items():
        print(f'{k}: {v: 3d}')