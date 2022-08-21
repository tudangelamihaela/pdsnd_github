# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import pandas as pd
#import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('Please specify the city you want see data from the following list: Chicago, New York or Washington : ')
    city = city.casefold()
    while city not in CITY_DATA:
        city = input('Wrong city name.Please try once again: ')
        city = city.casefold()
        
    # TO DO: get user input for month (all, january, february, ... , june)

    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Provide a month from January to June. If you don\'t want to see the data for a specific month, please provuide "all": ')
    month = month.casefold()
    while month not in months:
        month = input('The input is invalid.Please try once again')
        month = month.casefold()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input('Select a day from Monday to Sunday. If you would like to see the datat for the whole month please type "all" : ')
    day = day.casefold()
    while day not in days:
        day = input('Invalid day of week provided. Please try again')
        day = day.casefold()
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # data file needs to be loaded into a dataframe:
    df = pd.read_csv(CITY_DATA[city])

    # transforming the start time column into datetime format:
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
     # month column:
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
        # day column
    df['day'] = df['Start Time'].dt.day_name()
    
    # filter by month
    if month != 'all':
      months = ['january', 'february', 'march', 'april', 'may', 'june']
      month = months.index(month) + 1
        
     # filter by month to create the new dataframe
      df = df[df['month'] == month]

     # filter by day 
      if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df

   

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # we create a 'month' column by extracting the month from 'Start Time' 
    df['month'] = df['Start Time'].dt.month
    #looking for the popular month of the year 
    popularmonth = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('The most common month is ', months[popularmonth-1])

    # TO DO: display the most common day of week
    # we create a 'dayofweek' column by extracting the day from 'Start Time'  
    df['dayofweek'] = df['Start Time'].dt.dayofweek
    # Looking for the most common day of week
    popularday = df['dayofweek'].mode()[0]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('The most common day is ', days[popularday])
    
    # TO DO: display the most common start hour
    #we create a 'hour' column by extracting the hour from 'Start Time'
    df['hour'] = df['Start Time'].dt.hour
    popularhour = df['hour'].mode()[0]
    print('The Most Popular hour is ', popularhour) 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most popular start station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most popular end station i ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('\nThe most frequent combination of start and end Station trip is \n\n',df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total duration for your trip is:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('The mean duration time for a trip is:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types,'\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:    
        gender = df['Gender'].value_counts()
        print(gender,'\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest year of Birth:', df['Birth Year'].min())
        print('Most Recent year of Birth:', df['Birth Year'].max())
        print('Most Common year of Birth:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# 3rd attempt of submision: The ability to display raw data to the user, upon their request.

def request_data(df):
    data_start = 0
    data_end = 5
    df_length = len(df.index)
    
    while data_start < df_length:
            data_raw = input("\nPress 'yes' if you would like to see individual data otherwise press 'no'.\n")
            if data_raw.lower() == 'yes':
            
                print("\nDisplaying the 5 rows with data.\n")
                if data_end > df_length:
                    data_end = df_length
                print(df.iloc[data_start:data_end])
                data_start += 5
                data_end += 5
            else:
                break

def main():
    while True:
        city, month, day = get_filters()
        print("You selected {}, {}, and {}.".format(city.title(), month.title(), day.title()))
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        request_data(df)

        restart = input('\nWould you like to restart? Just enter Yes or No to proceed.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
