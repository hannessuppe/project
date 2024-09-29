import time
import pandas as pd
import numpy as np

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
    while True:
        city = input("Which city are you intrested in? Choose between Chicago, New York City and Washington: ").lower()
        if city in ['chicago', 'new york city', 'washington']:
                print(f"Alright. You selected {city}.")
                break
        else: 
                print("Oh, seems like there is a typo. Please choose between Chicago, New York City and Washington.")
        
        
 
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        time_filter = input("Would you like to filter by month, day, both or not at all? Type 'none' for no time filter.")
        if time_filter in ['month', 'day', 'both']:
                print(f"Alright. You will filter by {time_filter}.")
                break
        elif time_filter == 'none': 
                print(f"Alright. You will see the unfiltered data.")
                break
        else: 
                print("Oh, seems like there is a typo. Please choose between month, day, both or none")
    
    month = 'none'
    day = 'none'
            
    if time_filter == 'month' or time_filter == 'both':
       while True:
           month = input("Which month? January, February, March, April, May or June? ").title()
           if month in ['January', 'February', 'March', 'April', 'May', 'June']:
               print(f"Alright. You selected {month}.")
               break
           else: 
               print("Oh, seems like there is a typo. Please choose between January, February, March, April, May, June")  

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if time_filter == 'day' or time_filter == 'both':
        while True:
            day = input("Which Day (Monday - Sunday)? ").title()
            if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                print(f"Alright. You selected {day}.")
                break
            else: 
                print("Oh, seems like there is a typo. Please choose a day between Monday and Sunday")


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'none':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        #filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'none':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    ## extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    ## find the most popular month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of the Week:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used Start Station is: {start_station}.")

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f"The most commonly used End Station is: {end_station}.")

    # TO DO: display most frequent combination of start station and end station trip
    df['From - To'] = df['Start Station'] + " ----> " + df['End Station']
    journey = df['From - To'].mode()[0]
    print(f"The most frequent combination of start station and end station is: {journey}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum() / 60
    total_time = round(total_time, 2)
    total_time_hours = round((total_time / 60), 2)
    print(f"The total travel time is: {total_time} minutes or {total_time_hours} hours")

    # TO DO: display mean travel time
    mean_time = round((df['Trip Duration'].mean() / 60), 2)
    print(f"The average time for a Trip is: {mean_time} minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_usertype = df['User Type'].value_counts()
    print(f"\nCount of User Types:\n{count_usertype}\n")

    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts(dropna=False)
        print(f"Count of Gender:\n{count_gender}")
    except KeyError:
        print("Gender data is not available.\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_yearofbirth = int(df['Birth Year'].min())
        recent_yearofbirth = int(df['Birth Year'].max())
        mostcommon_yearofbirth = int(df['Birth Year'].mode()[0])
        print(f'Information about User´s Years of Birth:\nEarliest: {earliest_yearofbirth} \
        \nMost recent: {recent_yearofbirth} \nMost common: {mostcommon_yearofbirth}')
    except KeyError:
        print("Error: The 'Birth Date' data is not available.\n")

    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def individual_data (city):
    """Asks the user to display raw data."""

    pd.set_option('display.max_columns', None)
    df2 = pd.read_csv(CITY_DATA[city])
    i = 5
    while True:
        more_data = input("Would you like to see (more) raw data? yes or no \n")
        if more_data == 'yes':
            print(df2.head(i))
            i += 5
        else: 
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
