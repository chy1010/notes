"""
Use xml related packages to load VOC-type annotations.
require packages:
`pip install beautifulsoup4`
`pip install lxml`
"""

#%%
import cv2
from pathlib import Path
import xml.etree.ElementTree as ET


#%%
annot_file = 'data/voc-type-data/000001.xml'
annot_file = annot_file if Path(annot_file).exists() else '../' + annot_file

tree = ET.parse(annot_file)
root = tree.getroot()

# %%

filename = root.find('filename').text
size = root.find('size')
width = size.find('width').text
height = size.find('height').text

# %%

labels = []
for ind, obj in enumerate(root.iter('object')):
    truncated = next(obj.iter('truncated')).text
    box2d = obj.find('bndbox')
    x1 = int(box2d.find('xmin').text)
    y1 = int(box2d.find('ymin').text)
    x2 = int(box2d.find('xmax').text)
    y2 = int(box2d.find('ymax').text)
    box2d = dict(x1=x1,y1=y1,x2=x2,y2=y2)
    attributes=dict(INSTANCE_ID=ind, cameraIndex=0, truncated=bool(truncated))
    labels.append(dict(box2d=box2d, attributes=attributes))
    
# %%

image = cv2.imread('../data/voc-type-data/000001.jpg')
for label in labels:
    box2d = label['box2d']
    x1, y1, x2, y2 = int(box2d['x1']), int(box2d['y1']), int(box2d['x2']), int(box2d['y2'])
    cv2.rectangle(image, (x1,y1), (x2,y2), (127,255,0), 5)
    
# cv2.imwrite('../temp/test-read-voc-label.jpg', image)
