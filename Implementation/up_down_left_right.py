n = int(input())
x, y = 1, 1 // 기본 죄표 설정
plans = input().split()

dx = [0, 0, -1, 1] // 아래, 위, 왼, 오
dy = [-1, 1, 0, 0] // 아래, 위, 왼, 오
move = ['L', 'R', 'U', 'D'] // 방향 단어 넣어주기

for plan in plans:
  for i in range(len(move)):
    
