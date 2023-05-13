a = int(input())
b = int(input())
for num in range(a, b+1):
    count = 0
    delitel = 2
    while delitel < num:
        if num % delitel == 0:
            count += 1
        delitel += 1
    if count == 0:
        print(f'{num} простое число')
