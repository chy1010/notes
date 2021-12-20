import random

BAR_LENGTH = 20
NUM_OF_DATA = random.randint(10,20)
for i in range(NUM_OF_DATA):
    pbar = int((i+1) * BAR_LENGTH / NUM_OF_DATA)
    progress = f'[Progress]:[{">"*pbar}{" "*(BAR_LENGTH - pbar)}] {(i+1)/NUM_OF_DATA:5.2%} ({i+1}/{NUM_OF_DATA})'
    print(progress, end='\r')

print('\nEnd of iteration.')