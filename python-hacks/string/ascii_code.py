# >>> ord('a')
# 97
# >>> chr(97)
# 'a'
# >>> chr(ord('a') + 3)
# 'd'
# >>>


# ord changes char to int
# chr changes int to char

print(f'a is mapped to the ordinal number: {ord("a")}.')
print(f'the 97 is mapped to {chr(97)}.')

print(f'z is mapped to {ord("z")}')


# Russian letter:

russian_letters = 'ΑΒСΕΗΙЈΚΜΝΟΡԚЅΤԜΧΥΖ'
for s in russian_letters:
    print(f'{s} has ascii code {ord(s)}')