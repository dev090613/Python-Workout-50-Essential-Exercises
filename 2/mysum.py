def mysum(*numbers):
    res = 0

    for n in numbers:
        res += n
    msg = f"The result of mysum is {res}."

    return msg

print(mysum(50, 40, 50, 60))
