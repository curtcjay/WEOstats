import pandas as pd
import matplotlib

"""
This is a class for WEO indicators analysis by country, it has following functions:
1) Calculate the Growth rate of the indicator from year1 to year2
2) Calculate the Standard Deviation of the indicator from year1 to year2
3) Calculate the Average of the indicator from year1 to year2
4) Plot the time series from year1 to year

Attributes:
year1: a year from 1980 to 2015, int, default=1980
year2: a year from 1980 to 2015, int, default=1981
country: country from the available list of countries in the WEO, str, default = 'China'
indicator: indicator from the available list of indicators in the WEO, str, default = 'BCA'
df: a preprocessed dataframe with indicators data by year.

"""


def growth_rate(df, year1, year2, indc, country):
    """
    This function will return the growth rate for a given indicator given the beginnging year and end year
    Return:
    average: a DataFrame containing the average of the specified indicator over the specified years
    """
    df = df.ix[:, year1:year2]
    growth_r = df.pct_chage(axis=1)
    growth_r = pd.DataFrame(growth_r)  # convert the growth rate list to a dateframe
    growth_r.columns = ['Growth Rate of {} from {} to {}'.format(indc, year1, year2)]
    growth_r = growth_r.loc[[country]]
    return growth_r


def average(df, year1, year2, indc, country):
    """
    This function will return the average for a given indicator given the beginnging year and end year
    Return:
    average: a DataFrame containing the average of the specified indicator over the specified years
    """
    df = df.ix[:, year1:year2]
    avg = df.mean(axis=1)
    avg = pd.DataFrame(avg)  # convert the growth rate list to a dateframe
    avg.columns = ['Average of {} from {} to {}'.format(indc, year1, year2)]
    avg = avg.loc[[country]]
    return avg


def standard_deviation(df, year1, year2, indc, country):
    """
    This function will return the growth rate for a given indicator given the beginnging year and end year	
    Return:
    std: a dataframe containing the standard deviation of the specified indicator over the specified years
    """
    df = df.ix[:, year1:year2]
    std = df.std(axis=1)  # list containing growth rates for every country in specified years
    std = pd.DataFrame(std)  # convert the growth rate list to a dateframe
    std.columns = ['Standard Deviation of {} from {} to {}'.format(indc, year1, year2)]
    std = std.loc[[country]]
    return std


def time_series_plot(df, year1, year2, country, indc):
    """
    This function will return the times series figure for the selected indicator for given years and country
    Return:
    ax: the time series figure
    """
    df = df.ix[:, year1:year2]
    data = df.loc[country]
    data = pd.DataFrame(data)
    return data[country].plot(figsize=(10, 6), legend=True)
