s = input()
s = s.split(' ')
s = s[::-1]
print(s)
op = ''
for i in range(len(s)):
    op += s[i] + ' '
print(op)