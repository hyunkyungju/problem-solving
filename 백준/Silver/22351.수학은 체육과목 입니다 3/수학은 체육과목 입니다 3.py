# 456789101112131415161718192021 -> 4 21
# a, b <=999

lst = input()


length = len(lst)
if length>=6:
  if int(lst[0:3])+1==int(lst[3:6]):
    digit=3
    start=int(lst[0:3])
  elif int(lst[0:2])+1==int(lst[2:4]) or lst[0:5]=="99100":
    digit=2
    start=int(lst[0:2])
  else:
    digit=1
    start=int(lst[0:1])

elif length==4 or length==5:
  if int(lst[0:2])+1==int(lst[2:4]) or lst[0:4]=="9910":
    digit=2
    start=int(lst[0:2])
  else:
    digit=1
    start=int(lst[0:1])

elif length==3:
  if lst=="910":
    digit=2
    start=9
  elif int(lst[0:1])+1==int(lst[1:2]) and int(lst[1:2])+1==int(lst[2:3]):
    digit=1
    start=int(lst[0:1])
  else:
    digit=3
    start=int(lst)

elif length==2:
  if int(lst[0:1])+1==int(lst[1:2]):
    digit=1
    start=int(lst[0:1])
  else:
    digit=2
    start=int(lst)
else:
  digit=1
  start=int(lst[0:1])


i=0
value=0
isLast=False
while length>i:
  if digit==1:
    if lst[i]=='9':
      digit=2
      value=9
      isLast=True
    i+=1
  elif digit==2:
    isLast=False
    if lst[i:i+2]=='99':
      digit=3
      value=99
      isLast=True
    i+=2
  else:
    isLast=False
    i+=3
if isLast==False:
  value = int(lst[len(lst)-digit:len(lst)])
print(start, value)


