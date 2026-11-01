colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

result = {}

def color_map(state):
    if state == len(graph):
        return True

    place = list(graph.keys())[state]

    for color in colors:
        safe = True

        for neighbour in graph[place]:
            if result.get(neighbour) == color:
                safe = False

        if safe:
            result[place] = color

            if color_map(state + 1):
                return True

            del result[place]

    return False

if color_map(0):
    print("Map Coloring:")
    print(result)
else:
    print("No Solution")