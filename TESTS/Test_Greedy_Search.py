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
