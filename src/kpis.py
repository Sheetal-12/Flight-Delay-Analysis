import pandas as pd


def total_flights(df: pd.DataFrame) -> int:
    return len(df)


def percentage_delayed(df: pd.DataFrame) -> float:
    return (df['Dep_Delay'] > 0).mean() * 100


def avg_departure_delay(df: pd.DataFrame) -> float:
    return df['Dep_Delay'].mean()


def avg_arrival_delay(df: pd.DataFrame) -> float:
    return df['Arr_Delay'].mean()


def longest_delay(df: pd.DataFrame) -> int:
    return df['Dep_Delay'].max()


def shortest_delay(df: pd.DataFrame) -> int:
    return df['Dep_Delay'].min()
