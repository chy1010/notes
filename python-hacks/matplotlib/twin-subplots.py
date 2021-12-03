import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

with open('python-hacks/matplotlib/data/fake-logs.txt', mode='r') as fp:
    logs = fp.read().splitlines()

fake_logs = defaultdict(list)
for log in logs:
    iter, loss, bbox_mAP, segm_mAP = log.split(',')
    fake_logs['iter'].append(int(iter))
    fake_logs['loss'].append(float(loss))
    fake_logs['bbox_mAP'].append(float(bbox_mAP))
    fake_logs['segm_mAP'].append(float(segm_mAP))

fig, ax1 = plt.subplots(figsize=(20, 5))
ax1.plot(fake_logs['iter'], fake_logs['loss'], 'b', label='loss')
# ax1.legend(loc="upper left");

ax2 = ax1.twinx()
ax2.plot(fake_logs['iter'], fake_logs['bbox_mAP'], 'g', label='bbox_mAP')
ax2.set_ylabel('BoundingBox mAP')
# ax2.legend(loc="center left");

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 70))
ax3.plot(fake_logs['iter'],
         fake_logs['segm_mAP'],
         color='r',
         linestyle='dashed',
         label='segm_mAP')
ax3.set_ylabel('Segmentation mAP', labelpad=10)
# ax3.legend(loc="lower right")

# ask matplotlib for the plotted objects and their labels
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax1.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc=5)

plt.savefig('temp/plot.png', bbox_inches='tight', pad_inches=0.2)
