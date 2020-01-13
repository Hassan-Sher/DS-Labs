# Insertion Sort
l = [4,2,5,1,3]
for i in range(1,len(l)):
    cur_val = l[i]
    pos = i
    while(pos > 0 and l[pos - 1] > cur_val):
        l[pos] = l[pos - 1]
        pos = pos - 1
    l[pos] = cur_val
print(l)
