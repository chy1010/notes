import re

with open('data/I-have-a-dream.txt') as fp:
    speech = fp.read()

# use r-string to tell compiler this is a raw string.
# i.e. \n can't be changed to change line.

# \b: check the boundary, i.e. matched by the blank character
print(re.findall(r'\b.ing\b', speech))