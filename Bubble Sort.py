# Bubble Sort
l = [8,2,4,1]
i = 0
print("len(l)",len(l))
print("Before",l)
while i < len(l):
    j = 0
    while j < i:
        if l[i] < l[j]:
            # Swap Operation
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
        j = j + 1
    i = i + 1
print("After",l)
