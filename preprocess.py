import re
import pandas as pd
import streamlit as st

def preprocess(data):
    # Define pattern for date, time, user, and message in chat format
    pattern = r"(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}\s?[ap]m) - (.*?): (.*)"
    
    # Initialize lists for storing data
    dates, times, users, messages = [], [], [], []

    # Iterate over each line in the data and extract information
    for line in data.splitlines():
        match = re.match(pattern, line)
        if match:
            # Append extracted components to lists
            dates.append(match.group(1))
            times.append(match.group(2))
            users.append(match.group(3))
            messages.append(match.group(4))
    
    # Combine dates and times into a single datetime column
    date_time = [f"{d}, {t}" for d, t in zip(dates, times)]
    
    # Create DataFrame
    df = pd.DataFrame({'datetime': date_time, 'user': users, 'message': messages})
    
    # Convert datetime to pandas datetime format
    df['datetime'] = pd.to_datetime(df['datetime'], format='%d/%m/%Y, %I:%M %p')
    
    # Extract additional date and time information
    df['only_date'] = df['datetime'].dt.date
    df['year'] = df['datetime'].dt.year
    df['month_num'] = df['datetime'].dt.month
    df['month'] = df['datetime'].dt.month_name()
    df['day'] = df['datetime'].dt.day
    df['day_name'] = df['datetime'].dt.day_name()
    df['hour'] = df['datetime'].dt.hour
    df['minute'] = df['datetime'].dt.minute

    # Create 'period' column showing hour range (e.g., "23-00", "00-1", etc.)
    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(f"{hour}-00")
        elif hour == 0:
            period.append("00-1")
        else:
            period.append(f"{hour}-{hour + 1}")
    df['period'] = period

    return df

