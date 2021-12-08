import numpy as np
from typing import List, Union
from bbox_iou import multi_bboxes_iou, generate_bbox
from torchvision.ops import nms
import torch

def np_bbox_nms(bboxes: Union[np.ndarray, List[np.ndarray]],
                scores: Union[np.ndarray, List[np.ndarray], List[float]],
                iou_threshold: float = 0.8):
    bboxes = np.asarray(bboxes)
    scores = np.asarray(scores)
    
    assert bboxes.ndim <= 2
    if bboxes.ndim == 1:
        assert len(bboxes) == 4
        bboxes = np.asarray([bboxes])
    else: # bboxes.ndim == 2
        assert bboxes.shape[1] == 4

    assert scores.ndim == 1
    assert len(scores) == len(bboxes)

    # reverse order
    score_rankings = np.argsort(-scores)
    bboxes = bboxes.copy()[score_rankings]
    scores = scores.copy()[score_rankings]

    ious = multi_bboxes_iou(bboxes, bboxes.copy()) - np.eye(len(bboxes))

    poped_inds = set()
    rows, columns = np.where(ious > iou_threshold)
    for row, col in zip(rows, columns):
        if row in poped_inds: continue
        poped_inds.add(col)
    selected_inds = list(set(range(len(ious))) - poped_inds)

    # poped_inds = set()
    # selected_inds = []
    # for ind, iou in enumerate(ious):
    #     if ind in poped_inds: continue

    #     overlap_inds = np.where(iou > iou_threshold)
    #     assert len(overlap_inds) <= 1
    #     overlap_inds = next(iter(overlap_inds))
    #     for j in overlap_inds:
    #         poped_inds.add(j)
    #     selected_inds.append(ind)

    return score_rankings[np.asarray(selected_inds)]


if __name__ == '__main__':
    N = 100
    iou_threshold = 0.4

    bboxes = [generate_bbox(low=0, high=50, format='xyxy') for _ in range(N)]
    scores = [np.random.random() for _ in range(N)]

    np_bboxes = np.asarray(bboxes)
    np_scores = np.asarray(scores)

    from time import time
    start_time = time()
    np_nms_result = np_bbox_nms(np_bboxes, np_scores, iou_threshold=iou_threshold)
    print(f' my np bbox nms takes: {time() - start_time} seconds.')

    t_bboxes = torch.Tensor(bboxes)
    t_scores = torch.Tensor(scores)

    start_time = time()
    nms_result = nms(boxes=t_bboxes, scores=t_scores, iou_threshold=iou_threshold)
    nms_result = nms_result.numpy()
    print(f'torchvision nms takes: {time() - start_time} seconds.')

