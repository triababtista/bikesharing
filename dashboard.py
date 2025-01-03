# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PL1Pgr6NKtIOdseg7JRqSQP9C2vH9Uig
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
hourly_data_path = 'hour.csv'
daily_data_path = 'day.csv'

hourly_data = pd.read_csv(hourly_data_path)
daily_data = pd.read_csv(daily_data_path)

# Cleaning Data
hourly_data.rename(columns={
    'dteday': 'date',
    'weathersit': 'weather_situation',
    'hum': 'humidity',
    'cnt': 'total_rentals',
    'mnth': 'month',
    'yr': 'year',
}, inplace=True)

daily_data.rename(columns={
    'dteday': 'date',
    'weathersit': 'weather_situation',
    'hum': 'humidity',
    'cnt': 'total_rentals',
    'mnth': 'month',
    'yr': 'year',
}, inplace=True)

hourly_data['date'] = pd.to_datetime(hourly_data['date'])
daily_data['date'] = pd.to_datetime(daily_data['date'])

hourly_data['month'] = hourly_data['month'].map({
    1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
})
daily_data['month'] = daily_data['month'].map({
    1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
})

# Adding a day_type column
hourly_data['day_type'] = np.where(hourly_data['workingday'] == 1, 'Weekday', 'Weekend/Holiday')
daily_data['day_type'] = np.where(daily_data['workingday'] == 1, 'Weekday', 'Weekend/Holiday')

# EDA: Average Rentals by Month
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
daily_data['month'] = pd.Categorical(daily_data['month'], categories=month_order, ordered=True)

avg_month = daily_data.groupby('month')['total_rentals'].mean()

# EDA: Average Rentals by Season
avg_season = daily_data.groupby('season')['total_rentals'].mean()

# Streamlit Dashboard
st.title("Bike Sharing Data Analysis Dashboard")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page", ["Overview", "Hourly Rentals", "Monthly Rentals", "Seasonal Rentals"])

if page == "Overview":
    st.write("## Data Overview")
    st.write("### Dataset Summary")
    st.write("Hourly Data:")
    st.write(hourly_data.describe())
    st.write("Daily Data:")
    st.write(daily_data.describe())

elif page == "Hourly Rentals":
    st.write("## Hourly Bike Rentals by Day Type")

    # Add a selectbox for user type selection (Registered, Casual, or All Users)
    user_type = st.selectbox("Select User Type", ["All Users", "Casual Users", "Registered Users"])

    # Create different plots based on the selection
    if user_type == "All Users":
        avg_hour_day_type = hourly_data.groupby(['day_type', 'hr'])['total_rentals'].mean().unstack()
        fig, ax = plt.subplots(figsize=(12, 6))
        avg_hour_day_type.T.plot(kind='line', ax=ax)
        ax.set_title("Average Bike Usage per Hour: Weekdays vs. Weekends (All Users)")
        ax.set_xlabel("Hour")
        ax.set_ylabel("Average Rentals")
        ax.grid(True)
        st.pyplot(fig)

    elif user_type == "Casual Users":
        avg_hour_day_type_casual = hourly_data.groupby(['day_type', 'hr'])['casual'].mean().unstack()
        fig, ax = plt.subplots(figsize=(12, 6))
        avg_hour_day_type_casual.T.plot(kind='line', ax=ax)
        ax.set_title("Average Bike Usage per Hour: Weekdays vs. Weekends (Casual Users)")
        ax.set_xlabel("Hour")
        ax.set_ylabel("Average Rentals")
        ax.grid(True)
        st.pyplot(fig)

    elif user_type == "Registered Users":
        avg_hour_day_type_registered = hourly_data.groupby(['day_type', 'hr'])['registered'].mean().unstack()
        fig, ax = plt.subplots(figsize=(12, 6))
        avg_hour_day_type_registered.T.plot(kind='line', ax=ax)
        ax.set_title("Average Bike Usage per Hour: Weekdays vs. Weekends (Registered Users)")
        ax.set_xlabel("Hour")
        ax.set_ylabel("Average Rentals")
        ax.grid(True)
        st.pyplot(fig)

elif page == "Monthly Rentals":
    st.write("## Monthly Bike Rentals")

    fig, ax = plt.subplots(figsize=(10, 6))
    avg_month.plot(kind='bar', color='purple', alpha=0.7, ax=ax)
    ax.set_title("Average Bike Usage by Month")
    ax.set_ylabel("Average Usage")
    ax.set_xlabel("Month")
    ax.set_xticklabels(avg_month.index, rotation=45)
    ax.grid(axis='y')
    st.pyplot(fig)

elif page == "Seasonal Rentals":
    st.write("## Seasonal Bike Rentals")

    fig, ax = plt.subplots(figsize=(8, 5))
    avg_season.plot(kind='bar', color=['springgreen', 'yellow', 'orange', 'blue'], alpha=0.7, ax=ax)
    ax.set_title("Average Bike Usage by Season")
    ax.set_ylabel("Average Usage")
    ax.set_xlabel("Season")
    ax.set_xticklabels(["Spring", "Summer", "Fall", "Winter"], rotation=0)
    ax.grid(axis='y')
    st.pyplot(fig)