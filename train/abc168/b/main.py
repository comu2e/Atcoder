k = int(input())
s = input()
length = len(s)
if length <= k:
    print(s)
else:
    print(s[:k]+"...")
