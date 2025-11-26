import sys
sys.path.append('..')
import pytest
from src.greedy_search import find_best_station, greedy_search


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

#Test para verificar un paso del greedy#

def test_greedy_reduces_states():
    states_needed = {"ID", "NV", "UT"}
    stations = {
        "kone": {"ID", "NV", "UT"},
        "kfour": {"NV", "UT"},
    }

    result = greedy_search(states_needed, stations)

    assert "kone" in result
    assert len(result) == 1
    print("test_greedy_reduces_states passed")

#Test global del conjunto completo del ejercicio#
def test_greedy_search_complete():
    states_needed = {"ID", "NV", "UT", "WA", "MT"}
    stations = {
        "kone": {"ID", "NV", "UT"},
        "ktwo": {"WA", "ID", "MT"},
        "kthree": {"NV", "UT"},
    }

    result = greedy_search(states_needed, stations)

    assert set(result) == {"kone", "ktwo"}
    print("test_greedy_search_complete passed")

#Test para garantizar que siempre haya progreso#
def test_greedy_no_stagnation():
    states_needed = {"ID", "NV", "UT", "WA"}
    stations = {
        "kone": {"ID", "NV"},
        "ktwo": {"UT"},
        "kthree": {"WA"},
    }

    result = greedy_search(states_needed, stations)

    assert set(result) == {"kone", "ktwo", "kthree"}
    print("test_greedy_no_stagnation passed")
#Test para caso vacío#
def test_greedy_empty_case():
    states_needed = set()
    stations = {
        "kone": {"ID", "NV"},
        "ktwo": {"UT"},
    }

    result = greedy_search(states_needed, stations)

    assert result == []
    print("test_greedy_empty_case passed")