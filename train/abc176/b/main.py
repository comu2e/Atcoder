n = list(input())

sum_n = sum(list(map(int, n)))
if sum_n % 9 == 0:
    print("Yes")
else:
    print("No")
