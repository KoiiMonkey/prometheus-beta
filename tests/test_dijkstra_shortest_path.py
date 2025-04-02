import pytest
from src.dijkstra_shortest_path import dijkstra, reconstruct_path

def test_dijkstra_basic_graph():
    # Simple graph with multiple paths
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    distances, previous = dijkstra(graph, 'A')
    
    assert distances == {
        'A': 0,
        'B': 3,  # via C
        'C': 2,
        'D': 6   # via C and B
    }
    
    # Test path reconstruction
    path = reconstruct_path(previous, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']

def test_dijkstra_single_node_graph():
    graph = {'A': {}}
    
    distances, previous = dijkstra(graph, 'A')
    
    assert distances == {'A': 0}
    assert previous == {'A': None}
    
    path = reconstruct_path(previous, 'A', 'A')
    assert path == ['A']

def test_dijkstra_disconnected_node():
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {}
    }
    
    distances, previous = dijkstra(graph, 'A')
    
    assert distances['C'] == float('inf')
    assert previous['C'] is None
    
    with pytest.raises(ValueError, match="No path exists from A to C"):
        reconstruct_path(previous, 'A', 'C')

def test_dijkstra_negative_weights_error():
    graph = {
        'A': {'B': -1},
        'B': {}
    }
    
    # Dijkstra's algorithm does not support negative weights
    distances, previous = dijkstra(graph, 'A')
    assert distances['B'] == -1

def test_dijkstra_invalid_start_node():
    graph = {'A': {}, 'B': {}}
    
    with pytest.raises(ValueError, match="Start node 'C' not found in graph"):
        dijkstra(graph, 'C')

def test_dijkstra_complex_graph():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5},
        'D': {'E': 2},
        'E': {}
    }
    
    distances, previous = dijkstra(graph, 'A')
    
    assert distances == {
        'A': 0,
        'B': 3,  # via C
        'C': 2,
        'D': 6,  # via C and B
        'E': 4   # via B
    }
    
    path_a_to_e = reconstruct_path(previous, 'A', 'E')
    assert path_a_to_e == ['A', 'C', 'B', 'E']