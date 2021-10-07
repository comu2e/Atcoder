H,W,K= map(int,input().split())
matrix = []
for i in range(H):
    matrix.append(input())

ans = 0
for shift_h in range(1<<H):
    for shift_w in range(1<<W):
        black = 0
        for h in range(H):
            for w in range(W):
                if shift_h >> h & 1 == 0 and shift_w >> w & 1 == 0:
                    if matrix[h][w] == "#":
                        black+=1
        if black == K:
            ans += 1
print(ans)
                    