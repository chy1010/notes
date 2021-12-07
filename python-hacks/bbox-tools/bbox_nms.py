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
    selected_inds = []
    for ind, iou in enumerate(ious):
        if ind in poped_inds: continue

        overlap_inds = np.where(iou > iou_threshold)
        assert len(overlap_inds) <= 1
        overlap_inds = next(iter(overlap_inds))
        for j in overlap_inds:
            poped_inds.add(j)
        selected_inds.append(ind)

    return score_rankings[np.asarray(selected_inds)]


if __name__ == '__main__':
    N = 100
    iou_threshold = 0.4

    bboxes = torch.Tensor([generate_bbox(low=0, high=50, format='xyxy') for _ in range(N)])
    scores = torch.Tensor([np.random.random() for _ in range(N)])

    from time import time

    start_time = time()
    nms_result = nms(boxes=bboxes, scores=scores, iou_threshold=iou_threshold)
    print(f'torchvision nms takes: {time() - start_time} seconds.')
    nms_result = nms_result.numpy()

    bboxes = bboxes.numpy()
    scores = scores.numpy()

    start_time = time()
    np_nms_result = np_bbox_nms(bboxes, scores, iou_threshold=iou_threshold)
    print(f' my np bbox nms takes: {time() - start_time} seconds.')
