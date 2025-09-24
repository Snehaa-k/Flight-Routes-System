from .models import Route
from .models import Airport


def find_nth_node_graph(airport_code, steps, direction):
    """Find the Nth Left or Right Node using graph traversal"""
    
    try:
        # Verify airport exists
        Airport.objects.get(code=airport_code)
        
        # Build adjacency list for specified direction
        graph = {}
        for route in Route.objects.filter(position=direction).select_related('source', 'destination'):
            graph[route.source.code] = route.destination.code
        
        # Traverse the graph for specified steps
        current = airport_code
        for step in range(steps):
            if current not in graph:
                return f"No {direction} route found after {step + 1} steps from {current}"
            current = graph[current]
        
        return current
        
    except Airport.DoesNotExist:
        return "Airport not found"

def find_longest_route():
    """Find the route with maximum duration"""
    return Route.objects.order_by('-duration').first()

def find_shortest_path(source_code, dest_code):
    
    """Find shortest path between airports using Dijkstra's algorithm"""
    
    try:
        # Verify airports exist
        Airport.objects.get(code=source_code)
        Airport.objects.get(code=dest_code)
        
        # Build graph
        graph = {}
        airports = set()
        for route in Route.objects.select_related('source', 'destination'):
            if route.source.code not in graph:
                graph[route.source.code] = []
            graph[route.source.code].append((route.destination.code, route.duration))
            airports.add(route.source.code)
            airports.add(route.destination.code)
        
        # Initialize distances
        distances = {}
        for airport in airports:
            distances[airport] = float('inf')
        distances[source_code] = 0
        
        unvisited = list(airports)
        previous = {}
        
        while unvisited:
            # Find unvisited node with minimum distance
            current = min(unvisited, key=lambda x: distances[x])
            unvisited.remove(current)
            
            if current == dest_code:
                break
                
            if current in graph:
                for neighbor, weight in graph[current]:
                    if neighbor in unvisited:
                        new_distance = distances[current] + weight
                        if new_distance < distances[neighbor]:
                            distances[neighbor] = new_distance
                            previous[neighbor] = current
        
        if distances[dest_code] == float('inf'):
            return {"path": None, "distance": None, "message": "No path found"}
        
        # Reconstruct path
        path = []
        current = dest_code
        while current in previous:
            path.append(current)
            current = previous[current]
        path.append(source_code)
        path.reverse()
        
        return {
            "path": " → ".join(path),
            "distance": distances[dest_code],
            "message": None
        }
        
    except Airport.DoesNotExist:
        return {"path": None, "distance": None, "message": "Airport not found"}
