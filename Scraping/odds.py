# purpose of this code is to fetch NHL (National Hockey League) odds data from a specific sportsbook website for a range of dates. It iterates over each day in the given date range, makes an HTTP request to the website to retrieve the odds data for that day, parses the HTML response using BeautifulSoup, and then saves the data to HTML files.

# The purpose of fetching and saving the odds data could be for various reasons, such as analysis, data visualization, or building predictive models related to NHL matches.


# Import necessary libraries
from random import randint  # For generating random integers
from time import sleep  # For adding delays in requests
import calendar  # For calendar-related functionalities
from functools import reduce  # For functional programming operations
import timeit  # For timing code execution

from bs4 import BeautifulSoup  # For web scraping
import requests  # For making HTTP requests
import json  # For JSON parsing

# Define user-agent for HTTP requests
headers = {
    'User-Agent': 'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16'
}

# Function to calculate the number of days in a given month and year
def numberOfDays(year, month):
    days = calendar.monthcalendar(int(year), month)
    days = reduce(list.__add__, days)
    days = len([day for day in days if day != 0])
    return days

# The parseOdds function takes a start date, end year, end month, end day, and last date as input parameters. It then iterates over each day from the start date to the last date, making HTTP requests to fetch the odds data for each day and saving it to HTML files.

# Function to parse odds data from sportsbook website for a given date range
def parseOdds(startDate, endYear, endMonth, endDay, lastDate):
    startDate = startDate  # Start date (unused variable)
    endYear = endYear  # End year
    endMonth = endMonth  # End month
    endDay = endDay  # End day

    endDate = '%d%02d%02d' % (endYear, endMonth, endDay)  # Format end date

    # Loop until end date is reached
    while endDate != lastDate:
        url = 'https://classic.sportsbookreview.com/betting-odds/nhl-hockey/?date=' + endDate  # URL for odds data

        for attempt in range(2):  # Retry loop (maximum 2 attempts)
            try:
                # Make HTTP GET request to fetch odds data
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # Raise HTTPError for bad responses

                soup = BeautifulSoup(response.content, 'html.parser')  # Parse HTML response

                # Write odds data to HTML file
                with open('/Users/Milton/Developer/Hockey/data/Odds/' + endDate + '.html', 'w') as file:
                    file.write(response.text)

                print('Wrote ' + endDate + '.html')  # Print confirmation message

                # Update end date for next iteration
                if endDay == numberOfDays(endYear, endMonth):
                    endDay = 1
                    if endMonth == 12:
                        endMonth = 1
                        endYear += 1
                    else:
                        endMonth += 1
                else:
                    endDay += 1
                endDate = '%d%02d%02d' % (endYear, endMonth, endDay)  # Format updated end date

                # Break out of retry loop if successful
                break
            except requests.exceptions.RequestException as e:
                print(e)  # Print error message if request fails
        else:
            raise Exception('Reached error twice')  # Raise exception if request fails twice


# Dates + 1
# Call parseOdds function for each year in the date range
parseOdds('2023-10-04', 2023, 10, 4, '2024-4-10')
parseOdds('2022-10-12', 2022, 10, 12, '2023-04-10')
parseOdds('2021-10-07', 2021, 10, 7, '2022-04-10')
parseOdds('2020-10-08', 2020, 10, 8, '2021-04-10')
parseOdds('2019-10-01', 2019, 10, 1, '2020-04-10')
parseOdds('2018-10-06', 2018, 10, 6, '2019-04-10')
parseOdds('2017-10-07', 2017, 10, 7, '2018-04-10')
parseOdds('2016-10-07', 2016, 10, 7, '2017-04-10')
parseOdds('2015-10-01', 2015, 10, 1, '2016-04-10')
parseOdds('2014-10-01', 2014, 10, 1, '2015-04-10')
parseOdds('2013-9-29', 2013, 9, 29, '2014-04-13')
parseOdds('2012-10-01', 2012, 10, 1, '2013-04-10')
parseOdds('2011-10-06', 2011, 10, 6, '2012-04-07')
parseOdds('2010-10-07', 2010, 10, 7, '2011-04-10')
parseOdds('2009-10-01', 2009, 10, 1, '2010-04-11')
parseOdds('2008-10-01', 2008, 10, 1, '2009-04-12')
parseOdds('2007-9-29', 2007, 9, 29, '2008-04-06')
