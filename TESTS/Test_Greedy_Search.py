import sys
sys.path.append('..')
import pytest
from SRC.greedy_search import find_best_station


def test_find_best_station():
    states_needed = {"ID", "NV", "UT"}
    stations = {
        "kone": {"ID", "NV", "UT"},
        "ktwo": {"WA", "ID", "MT"},
        "kfour": {"NV", "UT"},
    }

    best_station = find_best_station(states_needed, stations)

    assert best_station == "kone"
    print("test_find_best_station passed")
# Additional test cases
# test devuelve None si ningun estacion cubre estados necesarios
def test_find_best_station_no_coverage():
    states_needed = {"TX", "FL"}
    stations = {
        "a": {"ID"},
        "b": {"NV"},
    }
    assert find_best_station(states_needed, stations) is None
# test devuelve estacion correcta cuando hay empate en cobertura

def test_find_best_station_tie():
    states_needed = {"ID", "UT"}
    stations = {
        "a": {"ID", "UT"},
        "b": {"ID", "UT"},
    }
    best = find_best_station(states_needed, stations)
    assert best in {"a", "b"}

# test devuelve estacion correcta cuando solo una estacion cubre todos los estados necesarios
def test_find_best_station_single_partial_match():
    states_needed = {"TX", "NV"}
    stations = {
        "a": {"NV"},
        "b": {"WA"},
    }
    assert find_best_station(states_needed, stations) == "a"

