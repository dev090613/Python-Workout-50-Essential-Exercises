def run_timing():
    cnt, total = 0, 0
    while s := input("Enter 10 km run time: "):
        try:
            time = float(s)
            total += time 
            cnt += 1
        except ValueError as e:
            print("That's not a valid number.")
    
    avg = (total / cnt) if cnt else 0
    return (avg, cnt)

avg, cnt = run_timing()

msg = f"Average of {avg:.2f}, over {cnt} runs"
print(msg)
