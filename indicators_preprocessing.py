import pandas as pd

def indicators_preprocessing():
    """
    This function is to preprocess 1980 - 2015 indicators dataset.
    Return: a merged dataset containing 1980-2015 indicators data.
    """
    s_year = range(1980, 1991)
    #load indicators data into a dictionary
    dfs = {year:pd.read_csv("stats_"+str(year)+".csv",encoding = "ISO-8859-1") for year in s_year}
    
    for year in s_year:
        dfs[year] = dfs[year].set_index(['Country'])
    return pd.concat(dfs, axis=1, join='outer') #merge dataframes into a dataframe


def indicators_preprocessing_by_year(indc='indc'):
    """
    This function is to prepocess indicator data by year
    Return:
    indicators_by_year: a dataframe containing every year's indicators for each country from 1980 to 2015
    """
    df = indicators_preprocessing()
    df.columns = df.columns.get_level_values(1)
    indicators_by_year = df[indc]
    indicators_by_year.columns= range(1980,1991) #rename columns names with years
    return indicators_by_year


def indicators_preprocessing_for_table(indc='indc'):
    """
    This function is to prepocess indicator data by year
    Return:
    indicators_for_table: a dataframe containing every year's indicators for each country from 1980 to 2015 for the table tab
    """
    df = indicators_preprocessing()
    df.columns = df.columns.get_level_values(1)
    indicators_for_table = df[indc]
    indicators_for_table.columns= range(1980,1991)
    indicators_for_table['Country'] = df.index
    cols = indicators_for_table.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    indicators_for_table = indicators_for_table[cols]
    indicators_for_table = indicators_for_table.reset_index(drop = True)
    return indicators_for_table
