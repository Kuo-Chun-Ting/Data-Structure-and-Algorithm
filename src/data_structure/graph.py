
from typing import List
from typing import Set
from typing import Dict


def dfs(graph: Dict[str, Set[str]], start: str, visited: List[str] = None, stack: List[str] = None) -> List[str]:
    if visited is None:
        visited = []

    visited.append(start)
    print(start)
    
    for vertex in graph[start]:
        if stack is None:
            stack = []

        if vertex not in visited and vertex not in stack:
            stack.insert(0, vertex)

    while stack is not None and len(stack) != 0:
        next_visited_node = stack.pop(0)
        dfs(graph, next_visited_node, visited, stack)

    return visited


def bfs(graph: Dict[str, Set[str]], start: str, visited: List[str] = None, queue: List[str] = []) -> List[str]:
    if visited is None:
        visited = []

    visited.append(start)
    print(start)

    for vertex in graph[start]:
        if vertex not in visited and vertex not in queue:
            queue.insert(0, vertex)

    while queue is not None and len(queue) != 0:
        next_visited_node = queue.pop()
        bfs(graph, next_visited_node, visited, queue)

    return visited


if __name__ == "__main__":
    l = ["1", "2", "3"]
    for i in l:
        print(i)

    graph = {
        "0": ["1", "2", "3"],
        "1": ["0", "2", "4"],
        "2": ["0", "1", "4"],
        "3": ["0"],
        "4": ["2"]
    }

    print("graph:")
    print(graph)

    print("dfs")
    dfs(graph, "0")
    
    print("bfs")
    bfs(graph, "0")
