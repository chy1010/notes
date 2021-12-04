import timm

from pprint import pprint
pprint(timm.list_models())

resnetv2_50 = timm.models.resnetv2_50()

print('-=-'*30)
pprint(resnetv2_50)