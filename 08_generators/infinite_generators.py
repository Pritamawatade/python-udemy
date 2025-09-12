def infinite_gen():
    count = 1

    while(True):
        yield f"Refill #{count}"
        count += 1

refill = infinite_gen()

for _ in range(3):
    print(next(refill))
