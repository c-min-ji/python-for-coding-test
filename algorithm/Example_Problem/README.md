# 목차
 * [Greedy](./README.md#greedy)<br>
 * [Implementation](./README.md#implementation)<br>
 * [DFS/BFS](./README.md#dfsbfs)<br>
 * [Sort](./README.md#sort)<br>

## Greedy
[1. 모험가 길드](./adventure.py)<br>
모험자 n명이 모험을 떠나는데 공포도가 x인 사람은 x명의 사람과 그룹을 이루어 모험을 떠나야 합니다. 모험을 떠날 수 있는 최대 그룹의 수를 구하시오.<br>

[2. 곱하기 혹은 더하기](./mul_sum.py)<br>
+혹은 \*를 이용해 연산하여 주어진 값의 최대값을 구하시오.<br>

[3. 문자열 뒤집기](./reverse_str.py)<br>
0혹은 1이 주어지는 데 둘 중 하나로 통일할 수 있는 최소 횟수를 구하시오.<br>

[4. 만들 수 없는 금액](./cant_make.py)<br>
n개의 돈으로 만들 수 없는 최소 금액을 구하시오.<br>

[5. 볼링공 고르기](./pick_ball.py)<br>
n가지의 m 무게의 공이 있을 때 두 명이 무게가 서로 다른 공을 고를 수 있는 경우의 수를 구하시오.<br>

[6. 무지의 먹방 라이브](./mukbang.py)<br>
[링크 참조!](https://programmers.co.kr/learn/courses/30/lessons/42891)


## Implementation
[1. 럭키 스트레이트](./lucky.py)<br>
주어진 점수의 자리수로 반으로 나누어 오른쪽 점수와 왼쪽 점수의 각 자리수 합이 동일하면 LUCKY 출력, 다르면 READY 출력하시오.<br>

[2. 문자열 재정렬](./sorted_str.py)<br>
알파벳 대문자와 숫자(0-9)로 이루어진 문자열을 알파벳 오름차순으로, 숫자는 전부 더해서 맨뒤에 출력하시오.<br>

[3. 문자열 압축](./short_str.py)<br>
[링크 참조!](https://programmers.co.kr/learn/courses/30/lessons/60057)<br>

[4. 자물쇠와 열쇠](./key.py)<br>
[링크 참조!](https://programmers.co.kr/learn/courses/30/lessons/60059)<br>

[5. 뱀](./snake.py)<br>
뱀이 nxn 정사각형 보드 위에서 사과를 먹으면 몸이 늘어나고, 뱀이 벽이나 자신의 몸에 부딪히면 게임이 끝난다. 이 때 게임이 몇 초에 끝나는지 구하시오.<br>

[6. 기둥과 보 설치](./pillar.py)<br>
[링크 참조!](https://programmers.co.kr/learn/courses/30/lessons/60061)<br>

[7. 치킨 배달](./chicken.py)<br>
치킨 집을 줄여서 최대 M개로 유지하여 일반 집과 M개의 치킨 집까지의 가장 적은 거리를 구하시오.<br>

[8. 외벽 점검](./wall.py)<br>
[링크 참조!](https://programmers.co.kr/learn/courses/30/lessons/60062)


## DFS/BFS
[1. 특정 거리의 도시 찾기](./find_city.py)<br>
N개의 도시와 M개의 거리가 1인 단방향 도로가 존재. 도시 X에서 출발해 도달할 수 있는 도시 중 최단 거리가 정확히 K인 도시의 번호를 출력하시오.<br>
 * 최단 거리니까 BFS탐색!<br>

[2. 연구소](./lab.py)<br>
바이러스가 퍼지지 않도록 벽을 세울 때 안전 영역의 최댓값을 구하시오.<br>

[3. 경쟁적 전염](./competit.py)<br>
바이러스가 주변으로 전파되었을 때 주어진 (x,y)의 바이러스를 구하시오.<br>

[4. 괄호 변환](./parenthesis.py)<br>
[링크 참조!](https://programmers.co.kr/learn/courses/30/lessons/60058)<br>

[5. 연산자 끼워 넣기](./operator.py)<br>
연산자가 주어졌을 때 해당 연산자를 이용해서 만들 수 있는 최소, 최대값을 구하시오.<br>

[6. 감시 피하기](./void.py)<br>
3개의 벽을 세워 선생님의 감시에서 학생이 피할 수 있다면 YES 출력, 아니면 NO를 출력하시오.<br>

[7. 인구 이동](./move.py)<br>
각 나라의 인구수가 주어졌을 때, 인구 이동이 몇 번 발생하는 지 구하시오.<br>
> 1. 국경선은 두 나라의 인구 수 차이가 L이상 R이하이면 열리고 인구 이동이 사작된다.
> 2. 인접한 국가만 이동을 할 수 있고 그 나라는 하루동안 연합이라고 칭한다.
> 3. 연합의 각 인구수는 (연합의 인구수)/(연합을 이루고 있는 나라 칸의 개수)
> 4. 연합을 해제하고 국경선 차단

[8. 블록 이동하기](./block.py)<br>
[링크 참조!](https://programmers.co.kr/learn/courses/30/lessons/60063)<br>

## Sort
