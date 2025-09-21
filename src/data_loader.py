import pandas as pd
import os


def load_data(sample: bool = True) -> pd.DataFrame:
    """
    Load flight dataset.
    :param sample: If True, loads sample dataset. Otherwise loads raw dataset.
    """
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(
        base_path,
        "data",
        "sample" if sample else "raw",
        "flight_data_sample.csv" if sample else "US_flights_2023.csv"
    )
    df = pd.read_csv(file_path)
    return df
