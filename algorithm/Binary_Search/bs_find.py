def bn_search(arr, target, start, end):
  while start <= end:
    mid = (start+end)//2
    
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      end = mid-1
    else:
      start = mid+1
   return None

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))
arr.sort()

for i in want:
  result = bn_search(arr, i, 0, n-1)
  if result != None:
    print('yes', end=' ')
  else:
    print('no', end=' ')
