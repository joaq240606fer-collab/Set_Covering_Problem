states_needed = {
    "WA", "ID", "MT", "OR", "NV", "UT", "CA", "AZ", "NM", "TX", "OK",
    "KS", "CO", "NE", "SD", "WY", "ND", "IA", "MN", "MO", "AR", "LA"
}

stations = {
    "kone": {"ID", "NV", "UT"},
    "ktwo": {"WA", "ID", "MT"},
    "kthree": {"OR", "NV", "CA"},
    "kfour": {"NV", "UT"},
    "kfive": {"CA", "AZ"},
    "ksix": {"NM", "TX", "OK"},
    "kseven": {"OK", "KS", "CO"},
    "keight": {"KS", "CO", "NE"},
    "knine": {"NE", "SD", "WY"},
    "kten": {"ND", "IA"},
    "keleven": {"MN", "MO", "AR"},
    "ktwelve": {"LA"},
    "kthirteen": {"MO", "AR"},
}

final_stations = set()

def find_best_station (states_needed, stations):
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    return best_station