def firstlast(sequence):
    first = sequence[:1]
    last = sequence[-1:]
    return first + last

print(firstlast([1, 2, 3, 4, 5])) # [1, 5]
print(firstlast((1, 2, 3, 4, 5))) # (1, 5)
print(firstlast("12345")) # 15
print(firstlast(())) # ()

