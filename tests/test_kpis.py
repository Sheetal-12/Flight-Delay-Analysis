# tests/test_kpis.py
import pandas as pd
from src.kpis import (
    total_flights, percentage_delayed,
    avg_departure_delay, avg_arrival_delay,
    longest_delay, shortest_delay
)


def test_kpis_basic():
    df = pd.DataFrame({
        'Dep_Delay': [10, 0, -5, 20],
        'Arr_Delay': [5, 0, -2, 15]
    })

    assert total_flights(df) == 4
    assert abs(percentage_delayed(df) - 50) < 1e-6  # two positive Dep_Delay
    assert abs(avg_departure_delay(df) - 6.25) < 1e-6
    assert abs(avg_arrival_delay(df) - 4.5) < 1e-6
    assert longest_delay(df) == 20
    assert shortest_delay(df) == -5


def test_kpis_empty():
    df = pd.DataFrame({'Dep_Delay': [], 'Arr_Delay': []})
    assert total_flights(df) == 0
    assert percentage_delayed(df) == 0
    assert avg_departure_delay(df) == 0
    assert avg_arrival_delay(df) == 0
    assert longest_delay(df) == 0
    assert shortest_delay(df) == 0
