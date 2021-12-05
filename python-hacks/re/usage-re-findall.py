import re


with open('python-hacks/re/data/fake-log.txt', mode='r') as fp:
    log_data = fp.read().splitlines()

# find only train loss or valid loss
losses = [ re.findall(',? (train|val) (loss: \{.*?\})', log) for log in log_data]

# here the (...) means matching groups, a single match is returned if all its groups are matched.

# may see the result:
print(losses[0])