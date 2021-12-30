import os

# Usage of fileObject.seek(offset[, whence])

# `whence` for seeking end is os.SEEK_END
print(f'os.SEEK_END: {os.SEEK_END}')

# see the contents of the file
with open('data/simple-num-seq.txt') as fp:
    contents = fp.read()
    print('CONTENTS:')
    print('-' * 30)
    print(contents)
    print('-' * 30)

with open('data/simple-num-seq.txt') as fp:

    # Usage of os.SEEK_END: Move the cursor to the EOF (end of file).
    # In this case, offset must be set to 0.
    offset = 0
    fp.seek(offset, os.SEEK_END)

    # Tell the position of the cursor.
    # In this case, the cursor is at the end. It's the number of characters of the documents.
    # Notice that '\n' also counts.
    print(
        f'After SEEK_END, the cursor is at the end and the position is now at: {fp.tell()}.'
    )

    # whence = 0: the positive relative to the beginning (after offset).
    offset = 10
    fp.seek(offset, 0)
    print(
        f'fp.seek({offset}, 0):',
        f'By setting the offset={offset}, now the beginning position is at {fp.tell()}.'
    )

    # This usage is like an option different to 0.
    # When `whence=1`, the cursor stay at current position.

    # In this case, the offset is still fixed to be 0.
    # Because we may didn't record the current position,
    # it may be set under an `if` condition:
    # if go to position i, then fp.seek(i, 0). Otherwise fp.seek(0,1).

    fp.seek(3, 0)
    line = fp.readline()
    print(f'Read Line: {line}')
    fp.seek(0, 1)
    line = fp.readline()
    print(f'Read Line: {line}')
