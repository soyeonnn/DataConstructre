from collections import deque
from SubwayGraphDFS import *


def dfs(graph, start_node):
    """dfs 함수"""
    stack = deque()  # 빈 스택 생성

    # 모든 노드를 처음 보는 노드로 초기화
    for station_node in graph.values():
        station_node.visited = 0

    # 시작점 노드를 옅은 회색 표시 후, 스택에 넣는다
    start_node.visited = 1
    stack.append(start_node)

    # 스택에 아무 노드도 없을 때까지:
    while stack:
        # 스택에서 가장 위 노드를 꺼낸다
        front_node = stack.pop()
        # 짙은 회색(방문 처리) 표시
        front_node.visited = 2
        # 인접해 있는 노드들 돌기
        stations = front_node.adjacent_stations
        for station in stations:
            # 처음 방문한 노드이면 방문한 노드로 표시하고, 큐에 넣는다
            if station.visited == 0:
                station.visited = 1
                stack.append(station)


stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
dfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)

