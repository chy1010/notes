
a = '  abcde '

print('strip the empty char')
print('\''+a.strip()+'\'')

print('strip the left empty char')
print('\''+a.lstrip()+'\'')

print('strip the right empty char')
print('\''+a.rstrip()+'\'')

b = '___abcd'
print('\''+b.strip('_')+'\'')