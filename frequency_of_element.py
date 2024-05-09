l = [1,1,2,2,2,3,4,4,5,1,1,3,5]

# find the frequenct of 1

k = 1

f = {}

for i in l:
    if i in f:
        f[i] +=1
    else:
        f[i] = 1

print(f)
print(max(f.values()))
print(f'frequency of 1 is {f[k]}' )