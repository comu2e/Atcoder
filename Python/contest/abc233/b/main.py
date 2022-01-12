
l, r = map(int,input().split())
s = input()
ans = ""

ans += s[:l-1]
ans += s[l-1:r][::-1]
ans += s[r:]
print(ans)
