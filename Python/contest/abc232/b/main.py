import string
plain_s = input()
enc = input()
alphabets = string.ascii_lowercase

diff = set()
for i in range(len(plain_s)):
  p = ord(plain_s[i])
  e = ord(enc[i])
  k = (e-p) % 26
  diff.add(k)

if len(list(diff)) == 1:
  print("Yes")
else:
  print("No")