import pandas as pd

def indicators_preprocessing():
    """
    This function is to preprocess 1980 - 2015 indicators dataset.
    Return: a merged dataset containing 1980-2015 indicators data.
    """
    s_year = range(1980, 1984)
    #load indicators data into a dictionary
    dfs = {year:pd.read_csv("stats_"+str(year)+".csv",encoding = "ISO-8859-1") for year in s_year}
    
    for year in s_year:
        dfs[year]['Economic Group'].fillna('N', inplace=True)
        dfs[year] = dfs[year].set_index(['Country']).drop('Economic Group', axis = 1)
    return pd.concat(dfs, axis=1, join='outer') #merge dataframes into a dataframe


def indicators_preprocessing_by_year(indc='indc'):
    """
    This function is to prepocess indicator data by year
    Return:
    indicators_by_year: a dataframe containing every year's indicators for each country from 2000 to 2015
    """
    df = indicators_preprocessing()
    df.columns = df.columns.get_level_values(1)
    indicators_by_year = df[indc]
    indicators_by_year.columns= range(1980,1984) #rename columns names with years
    #indicators_by_year['Country'] = df.index
    return indicators_by_year

	
	
	
	
	
