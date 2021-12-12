n = int(input())
if n >= 42:
  print("AGC0"+str(n+1))
else:
  if 1 <= n <= 9:
    print("AGC00"+str(n))
  else:
    print("AGC0"+str(n))