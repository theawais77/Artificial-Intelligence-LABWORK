from collections import deque

def bfs(graph, start, goal):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found!")
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs(graph, 'A', 'F')


def dfs(graph, start, goal):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found!")
            return

        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

dfs(graph, 'A', 'F')

import heapq

def ucs(graph, start, goal):
    pq = [(0, start)]   # (cost, node)
    visited = {}

    while pq:
        cost, node = heapq.heappop(pq)
        print(f"Visiting {node} with cost {cost}")

        if node == goal:
            print("Goal Found!")
            return

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if neighbor not in visited or new_cost < visited[neighbor]:
                visited[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('F', 3)],
    'D': [],
    'F': []
}

ucs(graph, 'A', 'F')

def depth_limited_search(graph, node, goal, limit):
    print(node, end=" ")

    if node == goal:
        return True
    if limit == 0:
        return False

    for child in graph[node]:
        if depth_limited_search(graph, child, goal, limit - 1):
            return True
    return False

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

found = depth_limited_search(graph, 'A', 'F', 2)
print("\nGoal Found!" if found else "\nCutoff Reached")

def dls(graph, node, goal, limit):
    if node == goal:
        return True
    if limit == 0:
        return False
    for child in graph[node]:
        if dls(graph, child, goal, limit - 1):
            return True
    return False

def ids(graph, start, goal):
    depth = 0
    while True:
        print(f"\nDepth = {depth}")
        if dls(graph, start, goal, depth):
            print("Goal Found!")
            return
        depth += 1

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

ids(graph, 'A', 'F')

from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    q_start = deque([start])
    q_goal = deque([goal])

    visited_start = {start: None}
    visited_goal = {goal: None}

    while q_start and q_goal:
        current = q_start.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited_start:
                visited_start[neighbor] = current
                q_start.append(neighbor)
                if neighbor in visited_goal:
                    return build_path(visited_start, visited_goal, neighbor)

        current = q_goal.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited_goal:
                visited_goal[neighbor] = current
                q_goal.append(neighbor)
                if neighbor in visited_start:
                    return build_path(visited_start, visited_goal, neighbor)

def build_path(vs, vg, meet):
    path = []
    node = meet
    while node:
        path.append(node)
        node = vs[node]
    path.reverse()

    node = vg[meet]
    while node:
        path.append(node)
        node = vg[node]
    return path

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['F'],
    'D': ['E'],
    'E': ['F'],
    'F': []
}

print(bidirectional_search(graph, 'A', 'F'))

import heapq

def a_star(graph, start, goal, h):
    pq = [(h[start], 0, start)]  # (f, g, node)
    visited = {}

    while pq:
        f, g, node = heapq.heappop(pq)
        print(f"Visiting {node}")

        if node == goal:
            print("Goal Found!")
            return

        for neighbor, cost in graph[node]:
            g_new = g + cost
            f_new = g_new + h[neighbor]
            if neighbor not in visited or g_new < visited[neighbor]:
                visited[neighbor] = g_new
                heapq.heappush(pq, (f_new, g_new, neighbor))

# Example graph
graph = {
    'A': [('B',1), ('C',4)],
    'B': [('F',5)],
    'C': [('F',1)],
    'F': []
}

h = {'A':4, 'B':3, 'C':1, 'F':0}

a_star(graph, 'A', 'F', h)

import heapq

def greedy_best_first(graph, start, goal, h):
    pq = [(h[start], start)]
    visited = set()

    while pq:
        _, node = heapq.heappop(pq)
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found!")
            return

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (h[neighbor], neighbor))

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['F'],
    'C': ['F'],
    'F': []
}

h = {'A':5, 'B':3, 'C':1, 'F':0}

greedy_best_first(graph, 'A', 'F', h)
