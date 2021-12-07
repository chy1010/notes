import numpy as np
import torch

from torchvision.ops import nms

from bbox_iou import generate_bbox, multi_bboxes_iou

N = 100
iou_threshold = 0.4

bboxes = torch.Tensor([generate_bbox(low=0, high=50, format='xyxy') for _ in range(N)])
scores = torch.Tensor([np.random.random() for _ in range(N)])

# bboxes = [[10,10,100,100], [20,20,120,120], [200,200,230,230], [201,202,231,232], [1,2,3,4], [5,7,8,9]]
# scores = [0.4, 0.5, 0.2, 0.6, 0.9, 0.2]
# bboxes = torch.Tensor(bboxes)
# scores = torch.Tensor(scores)

nms_result = nms(boxes=bboxes, scores=scores, iou_threshold=iou_threshold)
nms_result = nms_result.numpy()

bboxes = bboxes.numpy()
scores = scores.numpy()
score_ranking = np.argsort(-scores)
bboxes = bboxes[score_ranking]

ious = multi_bboxes_iou(bboxes.copy(), bboxes.copy())
poped_index = set()
selected_index = []
ious = ious - np.eye(len(bboxes))
for ind, iou in enumerate(ious):
    if ind in poped_index: continue
    for j in np.where(iou > iou_threshold)[0]:
        if j > ind:
            poped_index.add(j)
    selected_index.append(ind)

np_nms_result = score_ranking[np.asarray(selected_index)]
print('torchvision nms result:')
print(nms_result)
print('here the result:')
print(np_nms_result)
