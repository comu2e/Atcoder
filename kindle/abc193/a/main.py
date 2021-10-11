from decimal import Decimal
a,b = map(int,input().split())
print("{:.20f}".format(100* (1 -  Decimal(b) /Decimal(a))))