def hex_output() -> int:
    """
    It takes hex num and  return decimal equivalent
    """
    hexnum = input("Enter your hex num: ")
    hexnum = hexnum.lower().strip()
    if hexnum.startswith("0x"):
        hexnum = hexnum[2:]    
    
    if not all(c in "0123456789abcdef" for c in hexnum):
        raise ValueError("Invalid hexadecimal number.")

    decimal_result = 0
    for i, n in enumerate(reversed(hexnum)):
        decimal_result += int(n, 16) * (16 ** i)
    return decimal_result
    
result = hex_output()
print(result)
