import sys
input = sys.stdin.readline

def sol():
  h = [0] * 9
  for i in range(9):
    h[i] = int(input())
  
  for i in range(9):
    for j in range(i+1, 9):
      sum_ = 0
      for k in range(9):
        if k!=i and k!=j:
          sum_ +=h[k]
      if sum_ ==100:
        lst = list()
        for k in range(9):
          if k!=i and k!=j:
            lst.append(h[k])
        print('\n'.join(map(str, sorted(lst))))
        return
sol()      