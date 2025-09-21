import pandas as pd
from src.visuals import get_airline_distribution, get_delay_type_distribution


def test_get_airline_distribution():
    df = pd.DataFrame({'Airline': ['A', 'B', 'A', 'C', 'B']})
    dist = get_airline_distribution(df)
    assert 'proportion' in dist.columns
    assert abs(dist['proportion'].sum() - 1) < 1e-6


def test_get_delay_type_distribution():
    df = pd.DataFrame({'Dep_Delay_Type': ['Low', 'High', 'Low', 'Medium']})
    dist = get_delay_type_distribution(df)
    assert 'proportion' in dist.columns
    assert abs(dist['proportion'].sum() - 1) < 1e-6
