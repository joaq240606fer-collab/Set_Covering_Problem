#Test para comprobar que find_best_station funciona correctamente#

import pytest
from SRC.greedy_search import find_best_station, greedy_search


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


