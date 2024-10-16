def mysum(*items):
    if not (items):
        return items

    result = items[0]
    for item in items[1:]:
        result += item
    return result

print(mysum()) # ()
print(mysum(10, 20, 30, 40)) # 100
print(mysum('a', 'b', 'c', 'd')) # abcd
print(mysum([10, 20, 30], [40, 50, 60], [70, 80])) # [10, 20, 30, 40, 50, 60, 70, 80]
