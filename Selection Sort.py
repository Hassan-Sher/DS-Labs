# Selection Sort
l = [5,4,1,7,6,2,3]
print(l)
for  i in range(len(l)):
    min_val = min(l[i:])
    min_idx = l.index(min_val)
    l[i],l[min_idx] = l[min_idx],l[i]
# OR
#    temp = l[i]
#    l[i] = l[min_idx]
#    l[min_idx] = temp
print(l)
