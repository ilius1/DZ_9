a = int(input())
b = int(input())

i=a
j=1
while i<=b:
    while j<=10:
        print(i*j, end='\t')
        j=j+1
    print('\n')
    j=1
    i=i+1