import torch
import random

import numpy as np

def box_area(bboxes: torch.Tensor):
    return (bboxes[:, 2] - bboxes[:, 0]) * (bboxes[:, 3] - bboxes[:, 1])

def bboxes_iou(bboxes1, bboxes2):
    """[summary]
    Args:
        bboxes1 (torch.Tensor): of shape (N,4)
        bboxes2 (torch.Tensor): of shape (M,4)

    Returns:
        ious: the NxM matrix containing the pairwise IoU values
    """    
    area1 = box_area(bboxes1)
    area2 = box_area(bboxes2)

    lt = torch.max(bboxes1[:, None, :2], bboxes2[:, :2])  # [N,M,2]
    rb = torch.min(bboxes1[:, None, 2:], bboxes2[:, 2:])  # [N,M,2]

    wh = (rb - lt).clamp(min=0)  # [N,M,2]
    inter = wh[:, :, 0] * wh[:, :, 1]  # [N,M]
    union = area1[:, None] + area2 - inter
    return inter/union


def np_bboxes_iou(box1: np.ndarray, box2: np.ndarray, format: str = 'xyxy'):
    """[summary]
        Modified from the utils functions in https://github.com/WongKinYiu/ScaledYOLOv4

    Args:
        box1 (np.ndarray): group of bboxes of the format [[x1, y1, x2, y2], ...]
        box2 (np.ndarray): as above.
        format (optional[str]): . Defaults to 'xyxy'.
    """
    # box1 is of shape (N, 4) and box2 is of shape (M, 4)
    # change to shape (4, N) and obtain x1, y1, x2, y2 coordinates of each bbox.
    n, m = len(box1), len(box2)
    box1 = box1.T
    box2 = box2.T

    if format == 'xywh':
        box1[2:] += box1[:2]
        box2[2:] += box2[:2]
    elif format == 'xyxy':
        pass
    else:  # format == 'cxywh
        raise BaseException("the format is not xywh or xyxy")

    b1xyxy = [box1[i][:, None].repeat(m, axis=1) for i in range(4)]
    b2xyxy = [box2[i][None, :].repeat(n, axis=0) for i in range(4)]
    b1_x1, b1_y1, b1_x2, b1_y2 = b1xyxy
    b2_x1, b2_y1, b2_x2, b2_y2 = b2xyxy
    w1, h1 = b1_x2 - b1_x1, b1_y2 - b1_y1
    w2, h2 = b2_x2 - b2_x1, b2_y2 - b2_y1

    # Intersection area
    inter = (np.minimum(b1_x2, b2_x2) - np.maximum(b1_x1, b2_x1)).clip(0) * (
        np.minimum(b1_y2, b2_y2) - np.maximum(b1_y1, b2_y1)).clip(0)

    # Union Area
    union = (w1 * h1) + w2 * h2 - inter + np.finfo(float).eps

    return inter / union

if __name__ == '__main__':
    
    num_list = list(range(10,200,10))
    
    # bboxes_list1 = [ [*sorted(random.sample(num_list,2)), *sorted(random.sample(num_list,2))] for _ in range(50)]
    # bboxes1 = torch.Tensor(bboxes_list1).to(int)
    # bboxes_list2 = [ [*sorted(random.sample(num_list,2)), *sorted(random.sample(num_list,2))] for _ in range(50)]
    # bboxes2 = torch.Tensor(bboxes_list2).to(int)
    
    TEST_TIME = 1000
    time_duration = 0
    from time import time
    for _ in range(TEST_TIME):
        bboxes_list1 = [ [*sorted(random.sample(num_list,2)), *sorted(random.sample(num_list,2))] for _ in range(50)]
        bboxes1 = torch.Tensor(bboxes_list1).to(int)
        bboxes_list2 = [ [*sorted(random.sample(num_list,2)), *sorted(random.sample(num_list,2))] for _ in range(50)]
        bboxes2 = torch.Tensor(bboxes_list2).to(int)
        start = time()
        ious = bboxes_iou(bboxes1, bboxes2)
        time_duration += time() - start

    print(f'[torch] time duration for {TEST_TIME} times: {time_duration}')
    
    # TEST_TIME = 1000
    # time_duration = 0
    # from time import time
    # for _ in range(TEST_TIME):
    #     bboxes_list1 = [ [*sorted(random.sample(num_list,2)), *sorted(random.sample(num_list,2))] for _ in range(50)]
    #     bboxes1 = np.asarray(bboxes_list1)
    #     bboxes_list2 = [ [*sorted(random.sample(num_list,2)), *sorted(random.sample(num_list,2))] for _ in range(50)]
    #     bboxes2 = np.asarray(bboxes_list2)
    #     start = time()
    #     ious = np_bboxes_iou(bboxes1, bboxes2)
    #     time_duration += time() - start

    # print(f'[numpy] time duration for {TEST_TIME} times: {time_duration}')
        