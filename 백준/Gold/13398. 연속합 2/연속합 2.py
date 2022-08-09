import sys
input = sys.stdin.readline

def sol(inputs, removed, unremoved):
  if max(inputs)<0:
    print(max(inputs))
    return
  unremoved[0] = max(0, inputs[0])
  for i in range(1, n):
    value = inputs[i]
    unremoved[i] = max(0, unremoved[i-1]+value)
    removed[i] = max(removed[i-1]+value, 0, unremoved[i-1])
  print(max(max(unremoved), max(removed)))

n = int(input())
inputs = list(map(int, input().split()))

removed = [0] * n
unremoved = [0] * n
sol(inputs, removed, unremoved)
