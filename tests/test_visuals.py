import pandas as pd
import plotly.graph_objects as go
from src.visuals import (
    get_airline_distribution, get_delay_type_distribution,
    avg_delay_by_airline, delay_by_day_of_week,
    delay_scatter, delayed_percentage_over_time,
    delay_heatmap_airline_day
)


def test_get_airline_distribution():
    df = pd.DataFrame({'Airline': ['A', 'B', 'A', 'C', 'B']})
    dist = get_airline_distribution(df)
    assert 'proportion' in dist.columns
    assert abs(dist['proportion'].sum() - 1) < 1e-6
    assert len(dist) == 3
    expected = {'A': 2/5, 'B': 2/5, 'C': 1/5}
    for _, row in dist.iterrows():
        assert abs(row['proportion'] - expected[row['index']]) < 1e-6


def test_get_delay_type_distribution():
    df = pd.DataFrame({'Dep_Delay_Type': ['Low', 'High', 'Low', 'Medium']})
    dist = get_delay_type_distribution(df)
    assert 'proportion' in dist.columns
    assert abs(dist['proportion'].sum() - 1) < 1e-6
    expected = {'Low': 2/4, 'Medium': 1/4, 'High': 1/4}
    for _, row in dist.iterrows():
        assert abs(row['proportion'] - expected[row['index']]) < 1e-6


def test_visuals_figures():
    df = pd.DataFrame({
        'Airline': ['A', 'B', 'A'],
        'Dep_Delay': [10, 20, 30],
        'Arr_Delay': [5, 15, 25],
        'Day_Of_Week': [1, 2, 3],
        'Flight_Duration': [60, 120, 180],
        'FlightDate': pd.date_range('2023-01-01', periods=3)
    })
    # check if all functions return a plotly Figure object
    assert isinstance(avg_delay_by_airline(df), go.Figure)
    assert isinstance(delay_by_day_of_week(df), go.Figure)
    assert isinstance(delay_scatter(df), go.Figure)
    assert isinstance(delayed_percentage_over_time(df), go.Figure)
    assert isinstance(delay_heatmap_airline_day(df), go.Figure)


def test_empty_dataframe():
    df = pd.DataFrame(columns=['Airline', 'Dep_Delay_Type', 'Dep_Delay',
                               'Arr_Delay', 'Day_Of_Week', 'Flight_Duration',
                               'FlightDate'])
    assert get_airline_distribution(df).empty
    assert get_delay_type_distribution(df).empty
