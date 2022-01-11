import torch
import random

def merge_bboxes(bbox1: torch.Tensor, bbox2: torch.Tensor):
    assert isinstance(bbox1, torch.Tensor) and isinstance(bbox2, torch.Tensor)
    left_top = torch.minimum(bbox1[:2], bbox2[:2])
    right_bottom = torch.maximum(bbox1[2:], bbox2[2:])
    return torch.cat([left_top, right_bottom]).to(int)

def merge_bboxes2(bbox1: torch.Tensor, bbox2: torch.Tensor):
    assert isinstance(bbox1, torch.Tensor) and isinstance(bbox2, torch.Tensor)
    left_top = torch.min(bbox1[:2], bbox2[:2])
    right_bottom = torch.max(bbox1[2:], bbox2[2:])
    return torch.cat([left_top, right_bottom]).to(int)


if __name__ == '__main__':
    
    num_list = list(range(10,200,10))
    bbox1 = torch.Tensor([*sorted(random.sample(num_list,2)), *sorted(random.sample(num_list,2))]).to(int)
    bbox2 = torch.Tensor([*sorted(random.sample(num_list,2)), *sorted(random.sample(num_list,2))]).to(int)
    bbox = merge_bboxes2(bbox1, bbox2)
    
    print(bbox1)
    print(bbox2)
    print(bbox)
    
    from time import time
    TEST_TIME = 1000
    time_duration = 0
    for _ in range(TEST_TIME):
        bbox1 = torch.Tensor([*sorted(random.sample(num_list,2)), *sorted(random.sample(num_list,2))])
        bbox2 = torch.Tensor([*sorted(random.sample(num_list,2)), *sorted(random.sample(num_list,2))])
        start = time()
        bbox = merge_bboxes2(bbox1, bbox2)
        time_duration += time() - start
    print(f'time duration: {time_duration/TEST_TIME}')