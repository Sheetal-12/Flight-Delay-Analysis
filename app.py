import streamlit as st
import plotly.express as px
import pandas as pd
from src.data_loader import load_data
from src.visuals import (
    get_airline_distribution, get_delay_type_distribution,
    avg_delay_by_airline, delay_by_day_of_week, delay_scatter,
    delayed_percentage_over_time, delay_heatmap_airline_day
)
from src.kpis import (
    total_flights, percentage_delayed, avg_departure_delay,
    avg_arrival_delay, longest_delay, shortest_delay
)

# Page config
st.set_page_config(page_title="Flight Delay Dashboard", layout="wide")

# Load data
df = load_data(sample=True)

# Sidebar filters
st.sidebar.header("Filters")
airlines = df['Airline'].unique()
selected_airlines = st.sidebar.multiselect("Select Airlines", airlines,
                                           default=airlines)

days = df['Day_Of_Week'].unique()
selected_days = st.sidebar.multiselect("Select Days of Week", days,
                                       default=days)

df['FlightDate'] = pd.to_datetime(df['FlightDate'])
df['Month'] = df['FlightDate'].dt.month
months = df['Month'].unique()
selected_months = st.sidebar.multiselect("Select Months", months,
                                         default=months)

df_filtered = df[
    (df['Airline'].isin(selected_airlines)) &
    (df['Day_Of_Week'].isin(selected_days)) &
    (df['Month'].isin(selected_months))
]


st.title("✈️ Flight Delay Dashboard")

# KPIs
st.header("Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Total Flights", total_flights(df_filtered))
col2.metric("Flights Delayed (%)", f"{percentage_delayed(df_filtered):.2f}%")
col3.metric("Avg Departure Delay",
            f"{avg_departure_delay(df_filtered):.1f} min")

col4, col5, col6 = st.columns(3)
col4.metric("Avg Arrival Delay", f"{avg_arrival_delay(df_filtered):.1f} min")
col5.metric("Longest Delay", f"{longest_delay(df_filtered)} min")
col6.metric("Shortest Delay", f"{shortest_delay(df_filtered)} min")

# Charts
st.header("Visualizations")

# Airline distribution
st.subheader("Proportion of Flights by Airline")
airline_dist = get_airline_distribution(df_filtered)
fig1 = px.bar(airline_dist, x="index", y="proportion",
              labels={"index": "Airline", "proportion": "Proportion"})
st.plotly_chart(fig1, use_container_width=True)

# Delay type distribution
st.subheader("Departure Delay Types")
delay_dist = get_delay_type_distribution(df_filtered)
fig2 = px.pie(delay_dist, names="index", values="proportion")
st.plotly_chart(fig2, use_container_width=True)

# Avg delay by airline
st.subheader("Average Departure Delay by Airline")
st.plotly_chart(avg_delay_by_airline(df_filtered), use_container_width=True)

# Avg delay by day of week
st.subheader("Average Departure Delay by Day of Week")
st.plotly_chart(delay_by_day_of_week(df_filtered), use_container_width=True)

# Scatter plot: flight duration vs delay
st.subheader("Flight Duration vs Departure Delay")
st.plotly_chart(delay_scatter(df_filtered), use_container_width=True)

st.subheader("Percentage of Flights Delayed Over Time")
st.plotly_chart(delayed_percentage_over_time(df_filtered),
                use_container_width=True)

st.subheader("Average Departure Delay by Airline vs Day of Week")
st.plotly_chart(delay_heatmap_airline_day(df_filtered),
                use_container_width=True)
