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

 #cuando dos estaciones cubren la misma cantidad de estados, se puede elegir cualquiera de ellas#
def test_find_best_station_tie():
    states_needed = {"ID", "UT"}
    stations = {
        "a": {"ID", "UT"},
        "b": {"ID", "UT"},
    }
    best = find_best_station(states_needed, stations)
    assert best in {"a", "b"}


