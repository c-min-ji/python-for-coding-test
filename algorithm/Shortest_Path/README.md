# 최단 경로
가장 짧은 경로를 찾는 알고리즘
 * 다익스트라 알고리즘
 * 플로이드 워셜
 * 벨만 포드 알고리즘

## 다익스트라 알고리즘 (데이크스트라 알고리즘)
여러 개의 노드 중 특정 노드에서 출발해 다른 노드로 가는 각각의 최단 경로를 구해줌<br>
__*조건*__: 음의 간선이 없어야 함<br>
cf. 음의 간선 = 0보다 작은 값<br>
<br>
많이 사용하는 곳: GPS 소프트웨어의 기본 알고리즘<br>
<br>
그리디 알고리즘으로 분류됨

1. 출발 노드 설정
2. 최단 거리 테이블(리스트) 초기화
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산해 최단 거리 테이블(리스트) 업데이트
5. 3, 4번 반복

> 방법<br>
> [1. 구현하기 쉽지만 속도가 느린 코드](./Easy_Dijkstra.py)<br> __시간복잡도__: O(V^2) <br>
> [2. 구현하기 까다롭지만 속도가 빠른 코드](./Diff_Dijkstra.py)<br> __시간복잡도__: O(ElogV) <br> __원리__: 우선순위 큐를 이용
<br>

## 플로이드 워셜 알고리즘
모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우 사용<br>
>방법<br>
>[플로이드 워셜 알고리즘](./Floyd.py)<br>

### 연습 문제
[미래도시](./future.py)<br>
__문제__: 방문 판매원이 1번 회사부터 x번 회사까지 방문해 물건을 판매해야하는데, 소개팅 약속이 잡혀있다. 소개팅은 k번 회사에서 진행한다. 판매원이 소개팅을 먼저 진행하고 x번 회사로 갈 때 가장 빠르게 이동할 수 있는 경우는?<br>
__설명__: 전형적인 플로이드 알고리즘 문제. 포인트는 k를 거쳐 x로 가는 최단 거리를 구하는 것<br><br>

[전보](./message.py)<br>
__문제__: C라는 도시에 긴급한 상황이 생겨 최대한 많은 도시로 전보를 보내려고 한다. 단, 전보를 보낼 때 x->y로 보내려 한다면 그 길이 있어야하고 y->x이면 보내지 못한다.<br>
__설명__: 다익스트라 알고리즘 사용, 범위가 크기때문에 우선순위 큐를 사용
