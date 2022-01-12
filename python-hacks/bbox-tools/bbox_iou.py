from itertools import product
from timeit import timeit
import numpy as np
import random


def bbox_iou(box1: np.ndarray, box2: np.ndarray, format: str = 'xyxy'):
    """[summary]

    Args:
        box1 (np.ndarray): single bbox in the format [x1, y1, x2, y2] or [x, y, w, h].
        box2 (np.ndarray): as above.
        format (optional[str]):
            format of the bbox: 'xyxy', 'xywh', or 'cxywh';
            Defaults to 'xyxy'.
    """
    assert format in ['xyxy', 'xywh',
                      'cxywh'], f'The format is not supported now.'
    if format == 'xyxy':
        x1, y1, x2, y2 = box1
        a1, b1, a2, b2 = box2
        assert all([x1 < x2, y1 < y2, a1 < a2, b1 < b2])
        w1, h1 = x2 - x1, y2 - y1
        w2, h2 = a2 - a1, b2 - b1
    elif format == 'xywh':
        x1, y1, w1, h1 = box1
        a1, b1, w2, h2 = box2
        x2 = x1 + w1
        y2 = y1 + h1
        a2 = a1 + w2
        b2 = b1 + h2
    else:  # format == 'cxywh'
        xc1, yc1, w1, h1 = box1
        ac1, bc1, w2, h2 = box2
        x1, y1 = xc1 + w1 / 2, yc1 + h1 / 2
        a1, b1 = ac1 + w2 / 2, bc1 + h2 / 2
        x2, y2 = x1 + w1, y1 + h1
        a2, b2 = a1 + w2, b1 + h2

    ix1, iy1 = max(x1, a1), max(y1, b1)
    ix2, iy2 = min(x2, a2), min(y2, b2)
    intersection = max(ix2 - ix1, 0) * max(iy2 - iy1, 0)
    union = w1 * h1 + w2 * h2 - intersection
    iou = intersection / union
    return iou


def bboxes_iou(box1: np.ndarray, box2: np.ndarray, format: str = 'xyxy'):
    """[summary]
        Modified from the utils functions in https://github.com/WongKinYiu/ScaledYOLOv4

    Args:
        box1 (np.ndarray): single bbox of the format [x1, y1, x2, y2]
        box2 (np.ndarray): group of bboxes of the format [[x1, y1, x2, y2], ...]
        format (opitonal[str]): Defaults to 'xyxy'.
    """
    # box1 is of shape (4,) and box2 is of shape (N, 4)
    # change to shape (4, N) and obtain x1, y1, x2, y2 coordinates of each bbox.

    box2 = box2.T
    assert format in ['xyxy', 'xywh',
                      'cxywh'], f'The format is not supported now.'
    if format == 'xyxy':
        b1_x1, b1_y1, b1_x2, b1_y2 = box1[0], box1[1], box1[2], box1[3]
        b2_x1, b2_y1, b2_x2, b2_y2 = box2[0], box2[1], box2[2], box2[3]
        w1, h1 = b1_x2 - b1_x1, b1_y2 - b1_y1
        w2, h2 = b2_x2 - b2_x1, b2_y2 - b2_y1
    elif format == 'xywh':
        b1_x1, b1_y1, w1, h1 = box1[0], box1[1], box1[2], box1[3]
        b2_x1, b2_y1, w2, h2 = box2[0], box2[1], box2[2], box2[3]
        b1_x2, b1_y2 = b1_x1 + w1, b1_y1 + h1
        b2_x2, b2_y2 = b2_x1 + w2, b2_y1 + h2
    else:  # format == 'cxywh'
        raise BaseException("the format is not xywh or xyxy")

    # Intersection area
    inter = (np.minimum(b1_x2, b2_x2) - np.maximum(b1_x1, b2_x1)).clip(0) * (
        np.minimum(b1_y2, b2_y2) - np.maximum(b1_y1, b2_y1)).clip(0)

    # Union Area
    union = (w1 * h1) + w2 * h2 - inter

    return inter / union  # iou


def multi_bboxes_iou(box1: np.ndarray, box2: np.ndarray, format: str = 'xyxy'):
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

    return inter / union  # iou


# from numpy.random import default_rng
def generate_bbox(low=0, high=101, format="xyxy"):
    # numpy.random.Generator.choice() is available for numpy v1.17
    # rng = default_rng()
    # pairs = [sorted( rng.choice(range(low,high), 2, replace=False)  ) for _ in range(2)]

    # The sizes of xy pairs are samll. Using generator is much slower.
    pairs = [
        sorted(np.random.choice(range(low, high), 2, replace=False))
        for _ in range(2)
    ]
    bbox = np.asarray(pairs).T.flatten()
    if format == 'xywh':
        bbox[2:] -= bbox[:2]
    return bbox


if __name__ == '__main__':

    format_list = ['xyxy', 'xywh']
    format = format_list[np.random.randint(0, 2)]

    box1 = np.array([0, 0, 10, 10])
    box2 = np.array([5, 5, 10, 10])
    if format == 'xywh':
        box1[2:] -= box1[:2]
        box2[2:] -= box2[:2]
    iou = bbox_iou(box1, box2, format=format)
    assert iou == 0.25

    box1 = np.array([0, 0, 10, 10])
    box_list = [[1, 2, 3, 4], [5, 6, 7, 8], [5, 5, 10, 10], [10, 10, 20, 20]]
    if format == "xywh":
        box_list = [[box[0], box[1], box[2] - box[0], box[3] - box[1]]
                    for box in box_list]
    ious_1 = [
        bbox_iou(box1, np.asarray(box2), format=format) for box2 in box_list
    ]
    bboxes = np.array(box_list)
    ious_2 = bboxes_iou(box1, bboxes, format=format)
    assert np.array_equal(np.asarray(ious_1), ious_2)

    box1 = np.array([[0, 0, 10, 10], [1, 1, 9, 9]])
    box2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [10, 10, 20, 20]])
    if format == 'xywh':
        box1[:, 2:] -= box1[:, :2]
        box2[:, 2:] -= box2[:, :2]

    n, m = len(box1), len(box2)
    ious_1 = np.asarray([
        bbox_iou(box1[i], box2[j], format=format)
        for i, j in product(range(n), range(m))
    ]).reshape(n, m)
    ious_2 = multi_bboxes_iou(box1, box2, format=format)
    assert np.array_equal(ious_1, ious_2)

    number = 1000
    t = timeit("generate_xyxy()",
               "from __main__ import generate_xyxy",
               number=number)
    print(f"It takes {t:.4f} seconds to generate {number} bboxes.")

    bboxes_1 = [generate_bbox(format=format) for _ in range(50)]
    bboxes_2 = [generate_bbox(format=format) for _ in range(50)]

    def test_time_bbox_iou():
        i, j = np.random.randint(0, 50, size=(2, ))
        bbox_iou(bboxes_1[i], bboxes_2[j], format=format)

    def test_time_bboxes_iou():
        i = np.random.randint(0, 50)
        bboxes_iou(bboxes_1[i],
                   np.asarray(random.sample(bboxes_2, 10)),
                   format=format)

    def test_time_multi_bboxes_iou():
        multi_bboxes_iou(np.asarray(random.sample(bboxes_1, 10)),
                         np.asarray(random.sample(bboxes_2, 15)),
                         format=format)

    number = 1000
    t = timeit("test_time_bbox_iou()",
               "from __main__ import test_time_bbox_iou",
               number=number)
    print(
        f"It takes {t:.4f} seconds to calculate bbox_iou for {number} times.")
    t = timeit(
        "test_time_bboxes_iou()",
        "from __main__ import test_time_bboxes_iou",
        number=number,
    )
    print(
        f"It takes {t:.4f} seconds to calculate bboxes_iou for {number} times."
    )
    t = timeit(
        "test_time_multi_bboxes_iou()",
        "from __main__ import test_time_multi_bboxes_iou",
        number=number,
    )
    print(
        f"It takes {t:.4f} seconds to calculate multi_bboxes_iou for {number} times."
    )
