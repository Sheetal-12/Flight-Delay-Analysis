# import pytest
import pandas as pd
from src.data_loader import load_data


def test_load_sample_data():
    df = load_data(sample=True)
    # Check type
    assert isinstance(df, pd.DataFrame)
    # Check columns exist
    expected_cols = ['FlightDate', 'Day_Of_Week', 'Airline', 'Dep_Delay',
                     'Dep_Delay_Type']
    for col in expected_cols:
        assert col in df.columns
    # Check sample has reasonable number of rows
    assert len(df) > 0
