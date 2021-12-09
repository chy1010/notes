from time import sleep

# \t: tab
# \n: change line
# \b: back space
# \r: return

# Example of backspace
print('aaa\b\b', end='')
print('bcde')

print('After printing aaa, \\b\\b makes the cursor back to the second a.')

# Example of return
print('This is a line.\r', end='')
print('Due to \\r, the cursor goes back to the head and prints this line.')

# self-made progress bar
print('By using \\r, make a progress bar.')
LENGTH = 345
for i in range(LENGTH):
    sleep(0.01)
    completed = ((i + 1) * 10) // LENGTH
    incompleted = 10 - completed
    message = '[' + '-' * completed + '>' + ' ' * incompleted + ']' + f'{(i+1): 6d} / {LENGTH}'
    print(message, end='\r')
    
# at the end of for loop, the cursor is back to head
# hence print the last completed progress bar.
print(message)