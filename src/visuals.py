import pandas as pd
import plotly.express as px


def get_airline_distribution(df: pd.DataFrame) -> pd.DataFrame:
    return df['Airline'].value_counts(normalize=True).reset_index(
        name="proportion")


def get_delay_type_distribution(df: pd.DataFrame) -> pd.DataFrame:
    return df['Dep_Delay_Type'].value_counts(normalize=True).reset_index(
        name="proportion")


def avg_delay_by_airline(df: pd.DataFrame):
    avg_delay = df.groupby('Airline')['Dep_Delay'].mean().reset_index()
    fig = px.bar(avg_delay, x='Airline', y='Dep_Delay',
                 title='Average Departure Delay by Airline',
                 labels={'Dep_Delay': 'Avg Departure Delay (min)',
                         'Airline': 'Airline'})
    return fig


def delay_by_day_of_week(df: pd.DataFrame):
    avg_delay = df.groupby('Day_Of_Week')['Dep_Delay'].mean().reset_index()
    fig = px.line(avg_delay, x='Day_Of_Week', y='Dep_Delay', markers=True,
                  title='Average Departure Delay by Day of Week',
                  labels={'Dep_Delay': 'Avg Departure Delay (min)',
                          'Day_Of_Week': 'Day of Week'})
    return fig


def delay_scatter(df: pd.DataFrame):
    fig = px.scatter(df, x='Flight_Duration', y='Dep_Delay',
                     color='Airline',
                     hover_data=['Airline', 'Dep_Delay', 'Flight_Duration'],
                     title='Flight Duration vs Departure Delay')
    return fig


def delayed_percentage_over_time(df: pd.DataFrame):
    df['FlightDate'] = pd.to_datetime(df['FlightDate'])
    daily_delay = df.groupby('FlightDate').apply(lambda x: (
        x['Dep_Delay'] > 0).mean()).reset_index(name='Delayed_Percentage')
    fig = px.line(daily_delay, x='FlightDate', y='Delayed_Percentage',
                  title='Percentage of Flights Delayed Over Time',
                  labels={'Delayed_Percentage': 'Delayed Flights (%)',
                          'FlightDate': 'Date'})
    return fig


def delay_heatmap_airline_day(df: pd.DataFrame):
    heatmap_data = df.groupby(['Airline', 'Day_Of_Week'], as_index=False
                              )['Dep_Delay'].mean()
    fig = px.density_heatmap(heatmap_data, x='Day_Of_Week', y='Airline',
                             z='Dep_Delay',
                             color_continuous_scale='Viridis',
                             title='Avg. Dep Delay by Airline vs Day of Week',
                             labels={'Dep_Delay': 'Avg Departure Delay (min)',
                                     'Day_Of_Week': 'Day of Week'})
    return fig
